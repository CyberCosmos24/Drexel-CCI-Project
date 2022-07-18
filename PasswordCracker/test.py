import random
import time

filename = "list.txt"
wordslength = 3

substitutions = {
	"a": ["A","@","4"],
	"b": ["B"],
	"c": ["C"],
	"d": ["D"],
	"e": ["E","3"],
	"f": ["F"],
	"g": ["G"],
	"h": ["H"],
	"i": ["I","1"],
	"j": ["J"],
	"k": ["K"],
	"l": ["L","1"],
	"m": ["M"],
	"n": ["N"],
	"o": ["O","0"],
	"p": ["P"],
	"q": ["Q"],
	"r": ["R"],
	"s": ["S","$"],
	"t": ["T"],
	"u": ["U"],
	"v": ["V"],
	"w": ["W"],
	"x": ["Z"],
	"y": ["Y"],
	"z": ["Z"]
}

with open(filename) as wordlist:
	words = wordlist.readlines()

	# For each word in the list
	for word in words:
		# Get the word lowercase
		raw_guess = word.lower()
		# Loop through all of the letters in the word
		for character in raw_guess:
			
		
