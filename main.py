# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd

ifile = 'nato_phonetic_alphabet.csv'
df = pd.read_csv(ifile)

nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}

user = input("Enter the word:: ").upper()

list1 = [nato_dict[c] for c in user]

print(list1)



