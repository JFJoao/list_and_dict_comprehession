import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# Ex {"A": "Alfa", "B": "Bravo"}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
final_data_dic = {row.letter:row.code for (index, row) in data.iterrows()}
print(final_data_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Type the word: ").upper()
output_word = [final_data_dic[letter] for letter in word]
print(output_word)