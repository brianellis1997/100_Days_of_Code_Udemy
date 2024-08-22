import pandas as pd
df = pd.read_csv('Squirrel_Data.csv')

fur_colors = df['Primary Fur Color'].value_counts().reset_index().rename(columns={'Primary Fur Color': "Fur Color", "count": "Count"})
# print(fur_colors)
fur_colors.to_csv("squirrel_count.csv")