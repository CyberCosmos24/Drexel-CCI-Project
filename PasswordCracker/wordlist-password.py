import time
import math

filename = "list.txt"

# The options that each character can be substituted for
subs = {
	"a": ["a","A","@","4"],
	"b": ["b","B"],
	"c": ["c","C"],
	"d": ["d","D"],
	"e": ["e","E","3"],
	"f": ["f","F"],
	"g": ["g","G","9","6"],
	"h": ["h","H","#"],
	"i": ["i","I","1","7"],
	"j": ["j","J"],
	"k": ["k","K"],
	"l": ["l","L","1","7"],
	"m": ["m","M"],
	"n": ["n","N"],
	"o": ["o","O","0"],
	"p": ["p","P"],
	"q": ["q","Q","?"],
	"r": ["r","R"],
	"s": ["s","S","$","5","6","8"],
	"t": ["t","T"],
	"u": ["u","U"],
	"v": ["v","V"],
	"w": ["w","W"],
	"x": ["x","Z"],
	"y": ["y","Y"],
	"z": ["z","Z","2"],
	".": [".","*",","],
	",": [",",".","*"],
	"_": ["_","-"," ","=","+"],
	"-": ["-","_"," ","=","+"],
	" ": [" ","_","-","=","+"],
	"=": ["=","_","-"," ","+"],
	"+": ["+","_","-"," ","="],
	"\\": ["\\","/","|","<"],
	"/": ["/","\\","|",">"],
	"|": ["|","\\","/"],
	">": [">","<","/","="],
	"<": ["<",">","\\","="],
	":": [":",";"],
	";": [";",":"],
	"*": ["*",".",",","u","k","s","c","h","i","f","t","b","n"]
}

# Get the words from the wordlist
words = []
with open("words.txt") as wordlist:
    words = wordlist.readlines()

# A function to spit out the password options
def find_password(password):
	counter = 0
	# Loop through the words
	for word in words:
		# Change the word to lowercase and remove any newlines
		word = word.lower().strip('\n')
		#print("Trying " + word + " with various substitutions.")
		# Set the start of each combination to be the subs for the first letter
		combinations = subs[word[0]]
		# Init a temp array to hold guesses each letter
		temp = []
		# Loop through the remaining letters
		for i in range(1,len(word)):
			# Loop through the combinations in the array
			for j in range(0,len(combinations)):
				# Loop through the substitutions for this letter
				for sub in subs[word[i]]:
					# Add a combo that is the current combo + the current substitution
					temp.append(combinations[j] + sub)
			# Store the current combinations and clear the temp array
			combinations = temp
			temp = []
		counter += 1
		# Output the passwords created from this word
		for c in combinations:
			if c == password:
				if counter > 100:
					counter = math.ceil(counter / 100) * 100
				elif counter > 10:
					counter = math.ceil(counter / 10) * 10
				print("The password is: {}. It is in the top {} most common passwords.".format(c, counter))
				return True
			print(c)
		# Clear the array for the next word
		combinations = []
	return False

# Get the users password and try to crack it
password = input("Enter the password you'd like to crack: ")
start = time.time()
if find_password(password):
	found_time = time.time() - start
	print("It was found after {} seconds".format(found_time))
else:
	print("Password not found. It's pretty secure.")
# wl = "0"
# while not wl.isnumeric or not int(wl) > 1:
# 	wl = input("Enter the maximum number of words you'd like to string together: ")
# words_length = int(wl)