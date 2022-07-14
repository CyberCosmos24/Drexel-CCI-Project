import itertools
import string
import sys
import hashlib

# The function to guess the password by brute force
def guess(algo, password, number):
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	attempts = 0
	for password_length in range(1,int(number)+1):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			raw_guess = ''.join(guess)
			h = hashlib.new("sha256")
			h.update(raw_guess.encode('utf-8'))
			guess = h.hexdigest()
			if guess == password:
				return 'Original Password is \'{}\' found in {} guesses.'.format(raw_guess, attempts)
			else:
				print('Guess #{} is {} hashed as {}.'.format(attempts, raw_guess, h.hexdigest()))

# Print out the supported hash algorithms for this platform
algoList = "Supported Hash Algorithms:"
for algo in hashlib.algorithms_available:
	algoList += "  " + algo.upper()
print (algoList)

# Keep asking until the user enters a supported hash algorithm
algorithm = ""
while not algorithm.lower() in hashlib.algorithms_available:
    algorithm = input("Enter a supported algorithm:")
    
# Get the hash to crack and the max length to stop at
hashToCrack = input("Hash to Crack: ")
maxPasswordLength = input("Max Password Length: ")
# Run the guesser
print(guess(algorithm.lower(), hashToCrack, maxPasswordLength))
