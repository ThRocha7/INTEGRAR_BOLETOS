import pandas as pd

df = pd.read_excel('Pasta1.xlsx')

print(str(df.loc[0,'Agencia']))
