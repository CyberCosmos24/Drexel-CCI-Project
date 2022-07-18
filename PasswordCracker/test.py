import time

filename = "list.txt"
wordslength = 3

# The options that each character can be substituted for
subs = {
	"a": ["a","A","@","4"],
	"b": ["b","B"],
	"c": ["c","C"],
	"d": ["d","D"],
	"e": ["e","E","3"],
	"f": ["f","F"],
	"g": ["g","G"],
	"h": ["h","H","#"],
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
	"z": ["z","Z"]
}

words = ["Apple"]

for word in words:
    word = word.lower()
    print("Trying " + word + " with various substitutions.")
    # Set the start of each combination to be the subs for the first letter
    combinations = subs[word[0]]
    temp = []
    # Loop through the remaining letters
    for i in range(1,5):
        print("Loop {} \n\n".format(i))
    	# Loop through the subs for this letter
        for j in range(0,len(combinations)):
        	# Loop throught the combinations in the array
            for sub in subs[word[i]]:
            	# Add a combo that is the current combo + the current sub
                temp.append(combinations[j] + sub)
                print(combinations[j])
        combinations = temp
    print("Done")
    print(combinations)
