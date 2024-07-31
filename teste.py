# import pandas as pd

# df = pd.read_excel('planilha_padrao_julius.xlsx')

# print(df.loc[0,'fornecedor'])
b = 0

for i in range(5):
    a = input('a')
    if a == '1':
        print('reiniciar')
        continue
    else:
        print('não reiniciar')

    b = b + 1

print(b)
