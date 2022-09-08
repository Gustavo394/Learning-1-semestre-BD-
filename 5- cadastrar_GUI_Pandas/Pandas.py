import pandas as pd

dataframe = pd.DataFrame()

cadastro_df = pd.read_excel('cadastro.xlsx')

##nome= vendas_df['Nome']
##print(nome)

##print(vendas_df.loc[3])

cadastro = cadastro_df.loc[cadastro_df['Nome'] == 'Gustavo']

print(cadastro)
