# IMPORTANT: If you want to run this script by itself, you MUST change where it opens the files from (currently it is setup to open the files from the core directory)
# That is, change: with open("PasswordCracker/let.txt") -> with open("let.txt")
# And change:     with open("PasswordCracker/num.txt") -> with open("num.txt")

import time
import math
import string

# This is the number of brute force letters to add to the end of each password
# It must be declared here so the functions can access it. It is set in the input section
num = 0

# The options that each character can be substituted for in slow and very slow modes
subs_r = { 
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
	"?": ["?"], #137
	"@": ["#","a","A"],
	"#": ["#","h","H"],
	"$": ["$","s","S"],
	"0": ["0","o","O"],
	"1": ["1","i","I","l","L"],
	"2": ["2","s","S","5"],
	"3": ["3","e","E"],
	"4": ["4","a","A"],
	"5": ["5","s","S"],
	"6": ["6","s","S"],
	"7": ["7","1","i","I","l","L"],
	"8": ["8","s","S"],
	"9": ["9","g","G"],
	"&": ["&","8"]
}
# Import the wordlists (see note at top about file access)

# To run this file directly change:     with open("PasswordCracker/let.txt") -> with open("let.txt")
words_let = []
with open("let.txt") as wordlist:
    words_let = wordlist.readlines()

# To run this file directly change:     with open("PasswordCracker/num.txt") -> with open("num.txt")
words_num = []
with open("num.txt") as wordlist:
    words_num = wordlist.readlines()


# Check a password to check if it's in the top 10,000 most common passwords
def check_common(password):
    password = password.lower().strip('\n')
	# Set the start of each combination to be the subs for the first letter
    combinations = subs_r[password[0]]
	# Init a temp array to hold guesses each letter
    temp = []
	# Loop through the remaining letters
    for i in range(1,len(password)):
		# Loop through the combinations in the array
        for j in range(0,len(combinations)):
			# Loop through the substitutions for this letter
            for sub in subs_r[password[i]]:
				# Add a combo that is the current combo + the current substitution
                temp.append(combinations[j] + sub)
		# Store the current combinations and clear the temp array
        combinations = temp
        temp = []
    for c in combinations:
        # Check each combinations to see if it is one of the most common passwords
        if c+"\n" in words_let:
            print(".")
            return True, words_let.index(c+"\n")
    combinations = []
    return False, 0

# Format the time in hrs mins secs etc.
def format_time(time):
    # Round the time to be nicer if it's big enough

    if time > 3110400000:
        time /= 3110400000
        time = round(time, 1)
        return "~" + str(time) + " centuries"        
    elif time > 31104000:
        time /= 31104000
        time = round(time, 1)
        return "~" + str(time) + " years"
    elif time > 86400:
        time /= 86400
        time = round(time, 1)
        return "~" + str(time) + " days"
    elif time > 3600:
        time /= 3600
        time = round(time, 1)
        return "~" + str(time) + " hours"
    elif time > 60:
        time /= 60
        time = round(time, 1)
        return "~" + str(time) + " minutes"
    else:
        if time >= 0.001:
            time = round(time*1000)/1000
        return "~" + str(time) + " seconds"

# Calculate the time it would take a wordlist attack to crack this password
timePerPassWL = 0.000438084
def calculate_wl_time(index):
    return float(index) * timePerPassWL

# Calculate the time it would take a brute force attack to crack this password
possibleChars = 94
guessesPerSecond = 1000000
def calculate_bf_time(password):
    length = len(password)
    totalGuesses = 94 ** length
    return totalGuesses / guessesPerSecond

# Test the password for words inside it
def break_up_password(password):
    n = len(password)
    parts = []
    indices = []
    while True:
        for i in range(1,n):
            print(".")
            passW = []
            # Construct the word up to the current letter
            for j in range(0,i):
                passW.append(password[j])
            # Check if its in the dictionary
            cracked, index = check_common(''.join(passW))
            # If it is cracked
            if cracked:
                parts.append(''.join(passW))
                indices.append(index)
                # If we're at the end of the password, we're done
                if i == len(password):
                    # Return the parts we've found, the indices of the parts, and an empty string (there's nothing remaining)
                    return parts, indices, ""
                # If there's more password left
                else:
                    # Set the password to be the remainder of the password
                    passW = []
                    for j in range(i,len(password)):
                        passW.append(password[j])
                    password = ''.join(passW)
                    # Start over with the new section of the password
                    break
            # If it isn't cracked
            else:
                # If we're at the end of the password
                if i == len(password):
                    # Return the parts we've found, the indices of the parts, and what's left of the password
                    return parts, indices, password

## START AREA

# Greeting
print("Welcome to the password security test tool.\n")
# Get the users password
password = input("Enter the password you'd like to test: ")
print("")


## First check if the whole password is common
cracked, index = check_common(password)
if cracked:
    t = format_time(calculate_wl_time(index))
    print("Feedback:")
    print("    '{}' is a variation of one of the most common passwords. A wordlist attack could easily crack it.".format(password))
    print("    '{}' could be cracked in {} on standard household hardware.".format(password, t))
# If it isn't, switch to a breakdown approach
else:
    print("Password isn't one of the most common passwords. Switching to breaking it down now...")
    # Get the parts of the password that can be broken up into words
    parts, indices, remainder = break_up_password(password)
    if len(parts) > 0:
        print(str(parts))
        total_time = 0
        # Loop through the parts and indices
        for i in range(0,len(parts)):
            local_time = calculate_wl_time(indices[i])
            total_time += local_time
            print("Part {} could be found in {}.".format(parts[i], format_time(local_time)))
        print("\n{} could be cracked in {}.".format(password,format_time(total_time)))
    else:
        remainder = password
    # Calculate the time to brute force what's left of the password (could be the whole password)
    t = format_time(calculate_bf_time(remainder))
    print("    '{}' is not one one of the most common passwords. Thus, a Brute Force method would be needed.".format(remainder))
    print("    '{}' could be cracked in {} on standard household hardware.".format(remainder, t))
