import pandas as pd

nome = input('Digite seu nome')

with pd.ExcelFile('cadastro.xlsx') as cad_reader:
    cadastro_df = pd.read_excel(cad_reader)
    print(cadastro_df)

with pd.ExcelWriter("cadastro.xlsx", engine="xlsxwriter") as writer:
    cadastro_df.to_excel(writer, sheet_name='Nome')
    cad_write = pd.DataFrame(nome)
    writer.save()   


"""
with open('cadastro.csv', 'a', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([valores['-NOME-']] + [valores['-IDADE-']] + [valores['-CPF-']]
            + [valores['-RUA-']] + [valores['-NUM-']] + [valores['-COMP-']] + [valores['-BAIRRO-']]
            + [valores['-CEP-']] + [valores['-CDD-']] + [valores['-ESTADO-']] + [valores['-AFILIACAO-']])
            sg.popup_quick('Usuário cadastrado com sucesso!')
            arquivo.close()
"""