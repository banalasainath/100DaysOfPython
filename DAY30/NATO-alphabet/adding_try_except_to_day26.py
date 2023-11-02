import pandas

# TODO 1. Create a dictionary in this format:
df = pandas.read_csv('nato_phonetic_alphabet.csv')
df_dict = {value.letter: value.code for (index, value) in df.iterrows()}


# print(df_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

## First Approach
# wrong_input = True
# # Iterating until a correct word is entered
# while wrong_input:
#     user_input = input("Enter the word: ")
#     try:
#         list_of_letter_codes = [df_dict[letter.upper()] for letter in user_input]
#     except KeyError:
#         print("Sorry, Please enter the word, only with Alphabets")
#     else:
#         print(list_of_letter_codes)
#           wrong_input = False

# Shown Approach
def print_a_word_for_each_letter():
    user_input = input("Enter the word: ")
    try:
        list_of_letter_codes = [df_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, Please enter the word, only with Alphabets")
        print_a_word_for_each_letter()
    else:
        print(list_of_letter_codes)


# Calling the first time
print_a_word_for_each_letter()
