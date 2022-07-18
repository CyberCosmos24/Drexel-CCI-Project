import itertools # For efficient looping
import string # For string manipulation and characters
import hashlib # For hashing the password guesses

# The function to guess the password by brute force and hash it
def guess(algo, hashedPassword, number, noise):
	# Get the possible options
	chars = string.ascii_letters + string.digits + string.punctuation
	# The counter for the attempts we've made
	attempts = 0
	# Loop through the password lengths
	for password_length in range(1,int(number)+1):
		# Loop through all of the guess options for this length
		for guess in itertools.product(chars, repeat=password_length):
			# Increment the counter
			attempts += 1
			# Create the password guess
			raw_guess = ''.join(guess)
			# Set the hashing algorithm
			h = hashlib.new(algo)
			# Hash the guess
			h.update(raw_guess.encode('utf-8'))
			guess = h.hexdigest()
			# Check if the hashed guess matches the hashed password
			if guess == hashedPassword:
			    print("Original Password is {} found in {} guesses.".format(raw_guess, attempts))
			    return True
			# Otherwise print out if verbose is enabled
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

# Keep asking for the min password length until it's a number >= 2
mPL = ""
while not mPL.isnumeric or int(mPL) < 2:
    mPL = input("Min Password Length (min 2): ")
minPasswordLength = int(mPL)

# Keep asking for the min password length until it's a number >= the min password length
mPL = ""
while not mPL.isnumeric or int(mPL) < minPasswordLength:
    mPL = input("Max Password Length (min {}): ".format(minPasswordLength))
maxPasswordLength = int(mPL)

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
# Run the guesser normally with the input algorithm
elif not guess(algorithm.lower(), hashToCrack, maxPasswordLength, noise.lower()):
    print("Password not found.")
