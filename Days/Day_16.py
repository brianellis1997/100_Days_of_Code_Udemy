import pandas as pd

data = {
    'Pokemon Name': ['Pikachu', 'Squirtle', 'Charmander'],
    'Type' : ['Electric', 'Water', 'Fire']
}

table = pd.DataFrame(data)
print(table)

new_data = pd.Series({'Pokemon Name' : 'Bulbasor', 'Type': 'Water'})

table = pd.concat([table, new_data], ignore_index=True)
print(table)