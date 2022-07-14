import itertools
import string
import sys
import hashlib

# The algorithms that hashlib supports
acceptedAlgos = ["sha1","sha224","sha256","sha384","sha512"]

# The function to guess the password by brute force
def guess(algo, password, number):
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	attempts = 0
	for password_length in range(1,9):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			raw_guess = ''.join(guess)
			h = hashlib.new(algo)
			h.update(password)
			guess = h.hexdigest()
			if guess == password:
				return 'Original Password is {} found in {} guesses.'.format(raw_guess, attempts)
			else:
				print('Guess #{} is {} hashed as {}.'.format(attempts, raw_guess, guess))

# If the user entered enough arguments
if len(sys.argv) >= 4:
	# If the user entered a supported hash algorithm
	if sys.argv[1] in acceptedAlgos:
		# python3 bh.py algo hash len -- Run the guesser
		print(guess(sys.argv[1].lower(), sys.argv[2], sys.argv[3]))
	# If the user didn't enter a supported hash algorithm
	else:
		# Print the supported hash algorithms
		print('Hash algorithm not supported. Enter one of these: ')
		for algo in acceptedAlgos:
			print(algo)
# If the user didn't enter enough arguments
else:
	print('Enter the hash algorithm then the hash to crack and then the max length of the password as arguments.')
