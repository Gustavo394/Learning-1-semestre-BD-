from operator import index
import pandas as pd

excel_header = ['Nome',	'Idade','CPF', 'Rua', 'Num', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'Estado', 'Afiliação']

nome = [input('Digite: ')]
idade = [input('Digite: ')]
cpf = [input('Digite: ')]
rua = [input('Digite: ')]
num = [input('Digite: ')]
comp = [input('Digite: ')]
bairro = [input('Digite: ')]
cep = [input('Digite: ')]
cidade = [input('Digite: ')]
estado = [input('Digite: ')]
afiliacao = [input('Digite: ')]

cadastro_df = pd.DataFrame(data = pd.read_excel('cadastro.xlsx', engine='openpyxl'), columns = excel_header)
cadastro_df = pd.DataFrame(cadastro_df.append(nome, idade, cpf, rua, num, comp, bairro, cep, cidade, estado, afiliacao))

writer = pd.ExcelWriter('file1.xlsx')
cadastro_df.to_excel(writer, sheet_name = 'Planilha1', index=True)


writer.save()
