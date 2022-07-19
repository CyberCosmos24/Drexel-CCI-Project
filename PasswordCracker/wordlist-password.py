# coding: utf-8
# Your code here!
import time
import math

filename = "list.txt"

# The options that each character can be substituted for in medium and slow modes
subs_ms = { # Avg 137/42 = 3.25
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
	"x": ["x","X"],
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
	"*": ["*",".",",","u","k","s","c","h","i","f","t","b","n"],
	"?": ["?"] # 137
}

# The substitutions for fast mode - a slimmer set with far fewer options
subs_f = {
	"a": ["a","A","@","4"],
	"b": ["b","B"],
	"c": ["c","C"],
	"d": ["d","D"],
	"e": ["e","E","3"],
	"f": ["f","F"],
	"g": ["g","G"],
	"h": ["h","H"],
	"i": ["i","I","1"],
	"j": ["j","J"],
	"k": ["k","K"],
	"l": ["l","L","1"],
	"m": ["m","M"],
	"n": ["n","N"],
	"o": ["o","O","0"],
	"p": ["p","P"],
	"q": ["q","Q"],
	"r": ["r","R"],
	"s": ["s","S","$","5"],
	"t": ["t","T"],
	"u": ["u","U"],
	"v": ["v","V"],
	"w": ["w","W"],
	"x": ["x","Z"],
	"y": ["y","Y"],
	"z": ["z","Z","2"],
	".": ["."],
	",": [","],
	"_": ["_"],
	"-": ["-"],
	" ": [" "],
	"=": ["="],
	"+": ["+"],
	"\\": ["\\"],
	"/": ["/"],
	"|": ["|"],
	">": [">"],
	"<": ["<"],
	":": [":"],
	";": [";"],
	"*": ["*"],
	"#": ["#"],
	"0": ["0"],
	"1": ["1"],
    "2": ["2"],
    "3": ["3"],
    "4": ["4"],
    "5": ["5"],
    "6": ["6"],
    "7": ["7"],
    "8": ["8"],
    "9": ["9"]
}

# The very fast mode has no substitutions

# Get the words from the wordlist
words = []
with open("words.txt") as wordlist:
    words = wordlist.readlines()

# TODO: A function to spit out the password options for slow speed

# A function to check with the password options for medium speed
def medium_crack(password):
    counter = 0
    # Loop through the words
    for word in words:
		# Change the word to lowercase and remove any newlines
        word = word.lower().strip('\n')
		#print("Trying " + word + " with various substitutions.")
		# Set the start of each combination to be the subs for the first letter
        combinations = subs_ms[word[0]]
		# Init a temp array to hold guesses each letter
        temp = []
		# Loop through the remaining letters
        for i in range(1,len(word)):
			# Loop through the combinations in the array
            for j in range(0,len(combinations)):
				# Loop through the substitutions for this letter
                for sub in subs_ms[word[i]]:
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
                else:
                    print("The password is: {}. It is a variation on one of the top 10 most common passwords.".format(c))
                    return True
                print("The password is: {}. It is a variation on one of the top {} most common passwords.".format(c, counter))
                return True
            #print(c)
		# Clear the array for the next word
        combinations = []
    return False

# A function to check with the password options for fast speed
def fast_crack(password):
    counter = 0
    # Loop through the words
    for word in words:
		# Change the word to lowercase and remove any newlines
        word = word.lower().strip('\n')
		#print("Trying " + word + " with various substitutions.")
		# Set the start of each combination to be the subs for the first letter
        combinations = subs_f[word[0]]
		# Init a temp array to hold guesses each letter
        temp = []
		# Loop through the remaining letters
        for i in range(1,len(word)):
			# Loop through the combinations in the array
            for j in range(0,len(combinations)):
				# Loop through the substitutions for this letter
                for sub in subs_f[word[i]]:
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
                else:
                    print("The password is: {}. It is a variation on one of the top 10 most common passwords.".format(c))
                    return True
                print("The password is: {}. It is a variation on one of the top {} most common passwords.".format(c, counter))
                return True
            #print(c)
		# Clear the array for the next word
        combinations = []
    return False

# A function to check with the 10,000 most common passwords
def very_fast_crack(password):
    counter = 0
    for word in words:
        if password == word:
            if counter > 100:
                counter = math.ceil(counter / 100) * 100
            elif counter > 10:
                counter = math.ceil(counter / 10) * 10
            else:
                print("The password is: {}. It is a variation on one of the top 10 most common passwords.".format(word))
                return True
            print("The password is: {}. It is a variation on one of the top {} most common passwords.".format(word, counter))
            return True
    return False
# Get the users password and try to crack it
password = input("Enter the password you'd like to crack: ")
print("\n")
## Get which mode to use ##
# The mode the user inputs
mode = ""

print("|  Option   | Key | Password Variations | Time Est |")
print("|-----------|-----|---------------------|----------|")
print("|   Slow    |  S  |     50 Million+     | ~45 Min. |")
print("|  Medium   |  M  |     ~8 Million      | ~30 Min. |")
print("|   Fast    |  F  |     ~5 Million      | ~15 Min. |")
print("| Very Fast |  V  |     10 Thousand     |  1 Min.  |\n")
# The accepted modes
accModes = ["slow","s","medium","m","fast","f","very fast","veryfast","very","v"]
# While the mode is not accepted
while not mode in accModes:
    mode = input("What mode would you like to use (S,M,F,V): ").lower()
print("\n")
# We have the mode -- setup
start = time.time()

if mode == "slow" or mode == "s":
    # Slow mode
    print("Starting slow mode")
elif mode == "medium" or mode == "m":
    # Medium mode
    print("Starting medium mode")
    if medium_crack(password):
        print("It was found after {} seconds".format(time.time() - start))
    else:
        print("Password not found after {} seconds.".format(time.time() - start))
elif mode == "fast" or mode == "f":
    # Fast mode
    print("Starting fast mode")
    if fast_crack(password):
        print("It was found after {} seconds".format(time.time() - start))
    else:
        print("Password not found after {} seconds.".format(time.time() - start))
elif mode == "very" or mode == "very fast" or mode == "veryfast" or mode == "v":
    # Very fast  mode
    print("Starting very fast mode")
    if very_fast_crack(password):
        print("It was found after {} seconds".format(time.time() - start))
    else:
        print("Password not found after {} seconds.".format(time.time() - start))
