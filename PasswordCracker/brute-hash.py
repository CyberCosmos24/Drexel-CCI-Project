import itertools
import string
import sys
import hashlib

def guess(algo, password, number):
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	attempts = 0
	for password_length in range(1,9):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			raw_guess = ''.join(guess)
			if algo == "sha256":
				guess = hashlib.sha256(raw_guess.encode('utf-8')).hexdigest()
				if guess == password:
					return 'Password is {} found in {} guesses.'.format(raw_guess, attempts)
				else:
					print('{} guesses'.format(attempts))
			else:
				return 'Hash algorithm not supported. Enter \'sha256\''
n = len(sys.argv)
if n == 4:
	print(guess(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
	print('Enter the hash algo then the password to crack and then the max length of the password as arguments.')
