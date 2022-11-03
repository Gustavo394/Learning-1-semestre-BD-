excel_header = ['Nome']
df = pd.DataFrame(data = pd.read_excel('exemplo.xlsx', engine='openpyxl'), columns=excel_header)
df.at[0, 'Nome'] = input('')
writer = pd.ExcelWriter('arquivo.xlsx')
df.to_excel(writer)
writer.save()

print(df)

excel_header = ['Nome']
df = pd.DataFrame(data = pd.read_excel('exemplo.xlsx', engine='openpyxl'), columns=excel_header)
l = df['Nome'].count()
df.loc[l+1] = input('')
writer = pd.ExcelWriter('arquivo.xlsx')
df.to_excel(writer)
writer.save()

print(df)