import itertools
import string
import sys
import hashlib

# The function to guess the password by brute force
def guess(algo, hashedPassword, number, noise):
	chars = string.ascii_letters + string.digits + string.punctuation
	attempts = 0
	for password_length in range(1,int(number)+1):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			raw_guess = ''.join(guess)
			h = hashlib.new(algo)
			h.update(raw_guess.encode('utf-8'))
			guess = h.hexdigest()
			if guess == hashedPassword:
			    print("Original Password is {} found in {} guesses.".format(raw_guess, attempts))
			    return True
			elif noise == "verbose":
				print('Guess #{} is {} hashed as {}.'.format(attempts, raw_guess, h.hexdigest()))
	return False
allOption = "UNKNOWN"
# Print out the supported hash algorithms for this platform
algoList = "Supported Hash Algorithms:"
for algo in hashlib.algorithms_available:
	algoList += " " + algo.upper()
print (algoList)

# Keep asking until the user enters a supported hash algorithm
algorithm = ""
while not algorithm.lower() in hashlib.algorithms_available and not algorithm.lower() == allOption.lower():
    algorithm = input("Enter a supported algorithm or {}:".format(allOption))
    
# Get the hash to crack
hashToCrack = input("Hash to Crack: ")

# Keep asking for the password length until in proper range
maxPasswordLength = 0
while maxPasswordLength < 2:
    maxPasswordLength = int(input("Max Password Length (min 2): "))

# Get how much output we should send
noise = ""
while not (noise.lower() == "min" or noise.lower() == "verbose"):
    noise = input("Ouput Level (min, verbose):")

# Try all of the algorithm options
if algorithm.lower() == allOption.lower():
    # Try all of the algorithms
    for algo in hashlib.algorithms_available:
        print ("Trying algorithm {}".format(algo.upper()))
        if guess(algo, hashToCrack, maxPasswordLength, noise.lower()):
            break
        else:
            print("Password not found.")
# Run the guesser normally
elif not guess(algorithm.lower(), hashToCrack, maxPasswordLength, noise.lower()):
    print("Password not found.")
