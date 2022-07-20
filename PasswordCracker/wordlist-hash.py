# IMPORTANT: If you want to run this script by itself, you MUST change where it opens the files from (currently it is setup to open the files from the core directory)
# That is, change: with open("PasswordCracker/let.txt") -> with open("let.txt")
# And change:     with open("PasswordCracker/num.txt") -> with open("num.txt")

import time
import math
import string
import itertools

# VERY SLOW INFO
# Avg options per character = 137/42 = 3.25 guesses/character
# Avg letter per password = 8 letters/word
# Avg Max Time per Word = 3.25 ^ 16 = 154,929,400 guesses/word
# Guesses total = 1,549,294,000,000
# Time total (at 300,000 guesses/sec) = Days

# SLOW INFO
# Avg options per character = 137/42 = 3.25 guesses/character
# Avg letter per password = 8 letters/word
# Avg Max Time per Word = 3.25 ^ 8 = 12,450 guesses/word
# Total guesses = 12,450 * 10,000 = 124,500,000
# Total time (at 300,000 guesses/sec) = ~7 min

# MEDIUM INFO
# Avg options per character = 87/53 = 1.6 guesses/character
# Avg letter per password = 8 letters/word
# Avg options per password = 1.6 ^ 16 = 1845 guesses/word (bc two password strung together)
# Guesses total = 1845 * 10,000 = 18,450,000
# Total time (at 300,000 guesses/sec) = <2 min

# FAST INFO
# The avg options per character = 87/53 = 1.6 guesses/character
# Avg letter per password = 8 letters/word
# The avg options per word = 1.6 ^ 8 = 43
# est options total = 43 * 10,000 = 430,000 guesses
# Total time (at 300,000 guesses/sec) = ~1.43 seconds

# This is the number of brute force letters to add to the end of each password
# It must be declared here so the functions can access it. It is set in the input section
num = 0

# The options that each character can be substituted for in slow and very slow modes
subs_s = { 
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

# The substitutions for fast mode - a slimmer set with far fewer options for fast and medium modes
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
	"x": ["x","X"],
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
	"9": ["9"],
	"?": ["?"],
	"!": ["!"],
	"@": ["@"],
	"#": ["#"],
	"$": ["$"],
	"%": ["%"],
	"^": ["^"],
	"&": ["&"],
	"(": ["("],
	")": [")"] # 97
}


# Import the wordlists (see note at top about file access)

# To run this file directly change:     with open("PasswordCracker/let.txt") -> with open("let.txt")
words_let = []
with open("PasswordCracker/let.txt") as wordlist:
    words_let = wordlist.readlines()

# To run this file directly change:     with open("PasswordCracker/num.txt") -> with open("num.txt")
words_num = []
with open("PasswordCracker/num.txt") as wordlist:
    words_num = wordlist.readlines()



# A function to test a guess with brute force letters after it
def test_password(password, guess, num_bf):
    # All of the character otpions for brute forcing
    chars = string.ascii_letters + string.digits + string.punctuation
    for addition in itertools.product(chars, repeat=num_bf):
			# Create the addition
            addition = ''.join(addition)
			# Combine it with the guess
            new_guess = guess + addition
			# Check the guess
            if new_guess == password:
                return True, new_guess
	# None of the guesses worked
    return False, "Failed"
def check_password(c,password,counter,bf):
    # If no brute force letters should be added, just check the password
    if bf == 0:
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
    # If some brute force letters should be added, check the password with them
    else:
        # Get whether the password worked and if it did the correct password
        worked,correct = test_password(password, c, bf)
        if worked:
            print("The password is: {}. {} brute force letter(s) needed to be added to crack it.".format(correct, bf))
            return True

# A function to check the password options for slow speed and double up passwords
def very_slow_crack(password):
    # First run slow_crack to go through the one word options - if it succeeds, it will log out info and we're done
    if slow_crack(password):
        return True
    # If it fails, we go to two word options
    counter = 0
    # Loop through the words
    for wordo in words_let:
        # Loop throught the words again so we can string two words together
        for wordi in words_let:
    		# Change the word to lowercase and remove any newlines
            wordi = wordi.lower().strip('\n')
    		#print("Trying " + word + " with various substitutions.")
    		# Set the start of each combination to be the subs for the first letter
            wordiCombos = subs_s[wordi[0]]
    		# Init a temp array to hold guesses each letter
            wordiTemp = []
    		# Loop through the remaining letters
            for i in range(1,len(wordi)):
    			# Loop through the combinations in the array
                for j in range(0,len(wordiCombos)):
    				# Loop through the substitutions for this letter
                    for sub in subs_s[wordi[i]]:
    					# Add a combo that is the current combo + the current substitution
                        wordiTemp.append(wordiCombos[j] + sub)
    			# Store the current combinations and clear the temp array
                wordiCombos = wordiTemp
                wordiTemp = []

            counter += 1
            
            # Change the word to lowercase and remove any newlines
            wordo = wordo.lower().strip('\n')
    		# Set the start of each combination to be the subs for the first letter
            wordoCombos = subs_s[wordo[0]]
    		# Init a temp array to hold guesses each letter
            wordoTemp = []
    		# Loop through the remaining letters
            for i in range(1,len(wordo)):
    			# Loop through the combinations in the array
                for j in range(0,len(wordoCombos)):
    				# Loop through the substitutions for this letter
                    for sub in subs_s[wordo[i]]:
    					# Add a combo that is the current combo + the current substitution
                        wordoTemp.append(wordoCombos[j] + sub)
    			# Store the current combinations and clear the temp array
                wordoCombos = wordoTemp
                wordoTemp = []
            # Increase the counter
            counter += 1
    		# Combine all of the attempts
            for wo in wordoCombos:
                for wi in wordiCombos:
                    c = wo+wi
                    # Check each password
                    if check_password(c,password,counter,bf):
                        return True
    		# Clear the combo arrays for the next word
            wordoCombos = []
            wordiCombos = []
        return False

# A function to check with the password options for slow speed
def slow_crack(password):
    counter = 0
    # Test the password with up to num brute force letters after it (could be 0)
    for bf in range(0,num+1):
        print("Trying passwords with {} brute force letter(s) on the end.".format(bf))
        # Loop through the words
        for word in words_let:
    		# Change the word to lowercase and remove any newlines
            word = word.lower().strip('\n')
    		#print("Trying " + word + " with various substitutions.")
    		# Set the start of each combination to be the subs for the first letter
            combinations = subs_s[word[0]]
    		# Init a temp array to hold guesses each letter
            temp = []
    		# Loop through the remaining letters
            for i in range(1,len(word)):
    			# Loop through the combinations in the array
                for j in range(0,len(combinations)):
    				# Loop through the substitutions for this letter
                    for sub in subs_s[word[i]]:
    					# Add a combo that is the current combo + the current substitution
                        temp.append(combinations[j] + sub)
    			# Store the current combinations and clear the temp array
                combinations = temp
                temp = []
            counter += 1
    		# Output the passwords created from this word
            for c in combinations:
                # Check each password
                if check_password(c,password,counter,bf):
                    return True
    		# Clear the array for the next word
            combinations = []
    return False

# A function to check the password options for fast speed and double up passwords
def medium_crack(password):
    # First run fast_crack to check the one word options
    print("Trying one word options...")
    if fast_crack(password):
        return True
    print("Trying two word options...")
    # If it fails, we go to two word options
    counter = 0
    # Test the password with up to num brute force letters after it (could be 0)
    for bf in range(0,num+1):
        print("Trying passwords with {} brute force letter(s) on the end.".format(bf))
        # Loop through the words
        for wordo in words_num:
            # Loop throught the words again so we can string two words together
            for wordi in words_num:
        		# Change the word to lowercase and remove any newlines
                wordi = wordi.lower().strip('\n')
        		#print("Trying " + word + " with various substitutions.")
        		# Set the start of each combination to be the subs for the first letter
                wordiCombos = subs_f[wordi[0]]
        		# Init a temp array to hold guesses each letter
                wordiTemp = []
        		# Loop through the remaining letters
                for i in range(1,len(wordi)):
        			# Loop through the combinations in the array
                    for j in range(0,len(wordiCombos)):
        				# Loop through the substitutions for this letter
                        for sub in subs_f[wordi[i]]:
        					# Add a combo that is the current combo + the current substitution
                            wordiTemp.append(wordiCombos[j] + sub)
        			# Store the current combinations and clear the temp array
                    wordiCombos = wordiTemp
                    wordiTemp = []
    
                counter += 1
                
                # Change the word to lowercase and remove any newlines
                wordo = wordo.lower().strip('\n')
        		# Set the start of each combination to be the subs for the first letter
                wordoCombos = subs_f[wordo[0]]
        		# Init a temp array to hold guesses each letter
                wordoTemp = []
        		# Loop through the remaining letters
                for i in range(1,len(wordo)):
        			# Loop through the combinations in the array
                    for j in range(0,len(wordoCombos)):
        				# Loop through the substitutions for this letter
                        for sub in subs_f[wordo[i]]:
        					# Add a combo that is the current combo + the current substitution
                            wordoTemp.append(wordoCombos[j] + sub)
        			# Store the current combinations and clear the temp array
                    wordoCombos = wordoTemp
                    wordoTemp = []
                # Increase the counter
                counter += 1
        		# Combine all of the attempts
                for wo in wordoCombos:
                    for wi in wordiCombos:
                        # Combine to make password and check
                        c = wo+wi
                        # Check each password
                        if check_password(c,password,counter,bf):
                            return True
        		# Clear the combo arrays for the next word
                wordoCombos = []
                wordiCombos = []
    return False

# A function to check with the password options for fast speed
def fast_crack(password):
    counter = 0
    # Test the password with up to num brute force letters after it (could be 0)
    for bf in range(0,num+1):
        print("Trying passwords with {} brute force letter(s) on the end.".format(bf))
        # Loop through the words
        for word in words_num:
    		# Change the word to lowercase and remove any newlines
            word = word.lower().strip('\n')
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
    		# Output the passwords created from this word
            for c in combinations:
                # Check each password
                if check_password(c,password,counter,bf):
                    return True
            combinations = []
    return False

def format_time(time):
    # Round the time to be nicer if it's big enough
    if time >= 0.0001:
        time = round(time*10000)/10000
    if time > 86400:
        time /= 86400
        return "~" + str(time) + " days"
    elif time > 3600:
        time /= 3600
        return "~" + str(time) + " hours"
    elif time > 60:
        time /= 60
        return "~" + str(time) + " minutes"
    else:
        return "~" + str(time) + " seconds"
    
# START AREA
print("Welcome to the password cracking test tool!")
print("Note that the order of operations for this tool is as follows: ")
print("    1) Try one-word passwords with substitutions")
print("    2) Try one-word passwords with substitutions and Brute Force letters")
print("    3) Try two-word passwords with substitutions")
print("    4) Try two-word passwords with substitutions and Brute Force letters")
print("(Not all of these trials are used by every speed of password cracking.)")

# Get the users hash
password = input("Enter the hash you'd like to crack: ")
print("\n")


# Get the users hash type
password = input("Enter the hash algorithm to use: ")
print("\n")

## Get which mode to use ##
# The mode the user inputs
mode = ""

print("|  Option   | Key | Password Variations | Time Est  |")
print("|-----------|-----|---------------------|-----------|")
print("| Very Slow |  V  |    15.5+ Billion    |   Days    |")
print("|   Slow    |  S  |    124.5 Million    |  ~7 Min.  |") 
print("|  Medium   |  M  |    18.45 Million    |  ~2 Min.  |")
print("|   Fast    |  F  |    430 Thousand     |  ~2 Sec.  |")

# The accepted modes
accModes = ["slow","s","medium","m","fast","f","very slow","veryslow","very","v","vs"]
# While the mode is not accepted
while not mode in accModes:
    mode = input("What mode would you like to use (V,S,M,F): ").lower()
print("\n")

print("NOTE: Adding brute force letters can significantly increase crack time.")
# The input from the user
inputNum = ""
# While the inputNum is not accepted (it will only be accepted for 0 and above)
while not inputNum.isnumeric():
    inputNum = input("How many Brute Force letters do you want to add onto the end: ")
print("\n")
# The number of bf letters
num = int(inputNum)



# We have the mode and the salt info -- setup
start = time.time()

if mode == "slow" or mode == "s":
    # Slow mode
    print("Starting Slow Mode")
    if slow_crack(password):
        print("It was found after {}.".format(format_time(time.time() - start)))
    else:
        print("Password not found after {}.".format(format_time(time.time() - start)))
elif mode == "medium" or mode == "m":
    # Medium mode
    print("Starting Medium Mode")
    if medium_crack(password):
        print("It was found after {}.".format(format_time(time.time() - start)))
    else:
        print("Password not found after {}.".format(format_time(time.time() - start)))
elif mode == "fast" or mode == "f":
    # Fast mode
    print("Starting Fast Mode")
    if fast_crack(password):
        print("It was found after {}.".format(format_time(time.time() - start)))
    else:
        print("Password not found after {}.".format(format_time(time.time() - start)))
elif mode == "very" or mode == "very slow" or mode == "veryslow" or mode == "v" or mode == "vs":
    # Very fast  mode
    print("Starting Very Slow Mode")
    if very_slow_crack(password):
        print("It was found after {}.".format(format_time(time.time() - start)))
    else:
        print("Password not found after {}.".format(format_time(time.time() - start)))
