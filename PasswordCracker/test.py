import random
import time
import json

# Try words starting with each letter in this order. These are all sections in the word list
word_order = ["common", "s", "a", "t", "c", "b", "d", "e", "f", "w", "g", "h", "i", \
          "l", "p", "r", "m", "u", "n", "o", "j", "k", "x", "v", "y", "q", "z"]

# Load the word file into words_list array
with open("words.txt") as word_holder:
	words_list = json.load(word_holder)[0]
	print(len(words_list))

# Currently trying words starting with this letter in word list    
current_letter = word_order[0]
# Index of current word withing its letter's section
current_letter_index = 0

# Number of guesses for current password
guesses = 0
# Current guess from generate() function
current_guess = ""
# Number of guesses for all passwords
all_guesses = 0
# Number of passwords to crack (bulk password runs only work with brute force, not dictionary)
reps = [0, 1]
# Flag to stop guessing when attempt is sucessfull
status = "ongoing"

# Length to start guessing, will increment as all combinations are tried
password_length_to_start = 1
# Current guessing length
password_length = password_length_to_start

# String to hold the target password
target_password = ""

# Indexes for each character in a password
digits = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

# Select a password guess from the word list
def generate_dictionary_word():
    global target_password, current_guess, status, current_letter, current_letter_index, guesses, all_guesses
    # Retrieve current word from word list array
    if len(words_list[current_letter]) > 0:
        current_guess = words_list[current_letter][current_letter_index]
    # Prepare for next guess
    # Move to next index in the current letter array if not at end
    if current_letter_index < (len(words_list[current_letter]) - 1):
        current_letter_index += 1

    # If all words from that letter were tried    
    else:
        # Change to the next letter if any remaining
        if word_order.index(current_letter) < (len(word_order) - 1):
            current_letter = word_order[word_order.index(current_letter) + 1]
            # Start from beginning of new letter section
            current_letter_index = 0
            print(current_letter)
            
        else:
            #All words from all letters tried, bad luck
            status = "not_found"
            print("DONE: " + current_letter)
            all_guesses += (guesses + 1)
            guesses = 0

### MAIN LOOP
# Get the starting time to compare to end time for bulk runs  
total_time = 0.0

# Until the quota of passwords have been cracked (Bulk runs)
## or the user enters an empty password (single runs)
while reps[0] < reps[1]:
	status = "ongoing"

    
	# Reset the indexes for the all_words array to zero
	current_letter = word_order[0]
	current_letter_index = 0

	target_password = str(input("Enter a password to test\n"))

	# Leaving empty will exit main loop
	if target_password == "":
		reps[0] += 1
		status = "stopped"
		print(status)

	# Get the starting time for this run  
	this_time = time.time()
	guesses = 0
	# Start guessing until correct
	while status == "ongoing":
		# Generate a new guess
		guesses += 1
		generate_dictionary_word()
		if current_guess == target_password:
			elapsed = time.time() - this_time
			status = "Cracked"
			print(status + ": " + current_guess)
			print(str(guesses) + " guesses, " + str(elapsed) + " seconds.\n___________\n")
			all_guesses += guesses
			total_time += elapsed
