import itertools # For efficient looping
import string # For string manipulation and characters

# Run through all of the guesses from the min length to the max length
def guess(minPassLength, maxPassLength):
	# All of the characters
	chars = string.ascii_letters + string.digits + string.punctuation
	# Counter to track how many guesses we've made
	attempts = 0
	# Loop through the possible lengths
	for password_length in range(minPassLength,maxPassLength+1):
		# Loop through all of the guess options
		for guess in itertools.product(chars, repeat=password_length):
			# increase the attempts counter
			attempts += 1
			# Create the guess
			guess = ''.join(guess)
			# Print out the guess
			print(guess)

### Get the min length and make sure it's a number
ml = "" # The string the user inputs
# While the input isn't a number or is less than 1, ask again
while not ml.is_numeric() or int(ml) < 1:
	ml = input("Min Password Length: ")
min_length = int(ml) # The number we get from the user input

# Get the max length and make sure it's a number
l = "" # The string the user inputs
# While the input isn't a number or is less than the min length, ask again
while not length.is_numeric or int(length) < min_length:
	length = input("Max Password Length: ")
length = 0 # The number we get from the user input

# Let the user know what we're doing
print("Sending all passwords from {} characters to {} characters".format(min_length, length)) 
# Go through all of the guesses
guess(min_length, length)
