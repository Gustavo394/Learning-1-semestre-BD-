import pandas as pd

## Ler arquivo Excel
with pd.ExcelFile('exemplo.xlsx') as cad_reader:
    cadastro_df = pd.read_excel(cad_reader)

## Escrever um arquivo Excel
with pd.ExcelWriter('exemplo.xlsx', engine="xlsxwriter") as writer:
    cadastro_df.to_excel(writer)

## Ler e escrever um arquivo Excel
cadastro_df = pd.DataFrame(data = pd.read_excel('exemplo.xlsx'))
writer = pd.ExcelWriter('exemplo.xlsx')
cadastro_df.to_excel(writer, sheet_name = 'Planilha1', index=True)
writer.save()