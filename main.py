# For Day 26 I create a program that takes any string and converts it into the nato phonetic alphabet. Use this
# project to convert your name or anything else easily, so you can be precise when spelling to someone else.

# Import files needed
import pandas

# Create a data from using pandas to work with
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Using dict comprehension I create a dictionary for later use. It is understood that this can be done using ".to_dict"
# however, the guide wants it done this way for practice.
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


def convert():
    try:
        user_input = input("Enter your word to convert to NATO phonetics.\n").upper()
        # Create the list of nato phonetic code words and output them to the screen.
        nato_output = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Please input only letters in the alphabet!")
        convert()
    else:
        print(nato_output)


convert()
