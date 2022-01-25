# For Day 26 I create a program that takes any string and converts it into the nato phonetic alphabet. Use this
# project to convert your name or anything else easily, so you  can be precise when spelling to someone else.

# Import files needed
import pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_data_frame)
# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your word to convert to NATO phonetics.\n").upper()

nato_output = [nato_dict[letter] for letter in user_input]
print(nato_output)
