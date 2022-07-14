import itertools
import string

def guess(passLength):
	chars = string.ascii_letters + string.digits + string.punctuation
	attempts = 0
	for password_length in range(1,int(passLength)+1):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			guess = ''.join(guess)
			print(guess)
length = input("Max Password Length: ")
print("Sending all passwords up to {} characters".format(length)) 
print(guess(length))
