import pandas as pd

excel_header = ['Nome',	'Idade']

nome = [str(input('Digite seu nome: '))]
idade = [str(input('Digite sua idade: '))]

cadastro_df = pd.DataFrame(data = pd.read_excel('exemplo.xlsx', engine='openpyxl'), columns=excel_header)

## Contar o número de linhas da coluna Nome
l = cadastro_df['Nome'].count()
print(l)

# Adicionar mais uma linha com as informações recebidas
cadastro_df.loc[l+1] = nome + idade

writer = pd.ExcelWriter('exemplo.xlsx')

cadastro_df.to_excel(writer, sheet_name = 'Planilha1', index=True)

# Salvar no arquivo
writer.save()