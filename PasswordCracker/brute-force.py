import itertools
import string
import sys

def guess(password):
	chars = string.ascii_lowercase + string.digits
	attempts = 0
	for password_length in range(1,9):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			guess = ''.join(guess)
			if guess == password:
				return 'Password is {} found in {} guesses.'.format(guess, attempts)
			else:
				print('{} guesses'.format(attempts))
n = len(sys.argv)
if n > 1:
	print(guess(sys.argv[1]))
else:
	print('Enter the password to crack as an argument.')
