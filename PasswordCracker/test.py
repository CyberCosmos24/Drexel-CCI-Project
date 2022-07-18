import random
import time

#filename = "list.txt"
wordslength = 3

# The options that each character can be substituted for
substitutions = {
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
	"s": ["s","S","$"],
	"t": ["t","T"],
	"u": ["u","U"],
	"v": ["v","V"],
	"w": ["w","W"],
	"x": ["x","Z"],
	"y": ["y","Y"],
	"z": ["z","Z"]
}

#with open(filename) as wordlist:
if True:
	#words = wordlist.readlines()
	words = ["Apple"]
	# For each word in the list
	for word in words:
		# Get the word lowercase
		raw_guess = list(word.lower())
		# Loop through all of the letters in the word
		#curChar = 0
		#oldI = 0
		for i in range(1,len(raw_guess)+1):
			print("Outer \n")
			for c in range(0,i):
				new_guess = list(raw_guess)
				print("Inner \n")
				for switchChar in substitutions[raw_guess[c]]:
					#new_guess = list(raw_guess)
					new_guess[c] = switchChar
					print("".join(new_guess))
				#curChar += 1
			#oldI = i

