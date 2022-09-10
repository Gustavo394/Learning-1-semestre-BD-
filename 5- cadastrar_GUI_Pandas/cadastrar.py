import PySimpleGUI as sg
import pandas as pd

def __init__():

    layout = [
        [sg.Text('Nome', font=('Arial')), sg.Input('', size=(28), font=('Arial'), key='-NOME-'),
        sg.Text('Idade', font=('Arial')), sg.Input('', size=(3), font=('Arial'), key='-IDADE-')],
        [sg.Text('CPF', font=('Arial')), sg.Input('', size=(20), font=('Arial'), key='-CPF-')],
        [sg.Text('Endereço: ', font=('Arial')),
        sg.Text('Rua', font=('Arial')), sg.Input('', size=(20), font=('Arial'), key='-RUA-'),
        sg.Text('Nº', font=('Arial')), sg.Input('', size=(5), font=('Arial'), key='-NUM-')],
        [sg.Text('Complemento', font=('Arial')), sg.Input('', size=(25), font=('Arial'), key='-COMP-')],
        [sg.Text('Bairro', font=('Arial')), sg.Input('', size=(21), font=('Arial'), key='-BAIRRO-'),
        sg.Text('CEP', font=('Arial')), sg.Input('', size=(10), font=('Arial'), key='-CEP-')],
        [sg.Text('Cidade', font=('Arial')), sg.Input('', size=(35), font=('Arial'), key='-CDD-')],
        [sg.Text('Estado', font=('Arial')), sg.Input('', size=(35), font=('Arial'), key='-ESTADO-')],
        [sg.Text('Filiação', font=('Arial')), sg.Input('', size=(35), font=('Arial'), key='-FILIACAO-')],
        [sg.Button('Salvar', expand_x=True, font=('Arial'), key='-SALVAR-')],
    ]
    return sg.Window('Registro', layout=layout, margins=(10, 10), finalize=True)

cadastro = __init__()

while True:
    excel_header = ['Nome', 'Idade', 'CPF', 'Rua', 'Numero', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'Estado', 'Filiação']
    cadastro_df = pd.DataFrame(data = pd.read_excel('arquivo.xlsx', engine='openpyxl'), columns=excel_header)
    window, eventos, valores = sg.read_all_windows()

    if window == cadastro and eventos == sg.WINDOW_CLOSED:
        break
    
    if window == cadastro and eventos in ['-SALVAR-']:
        print(window, eventos, valores)
        l = cadastro_df['Nome'].count()
        cadastro_df.loc[l+1] = ([valores['-NOME-']] + [valores['-IDADE-']] + [valores['-CPF-']]
            + [valores['-RUA-']] + [valores['-NUM-']] + [valores['-COMP-']] + [valores['-BAIRRO-']]
            + [valores['-CEP-']] + [valores['-CDD-']] + [valores['-ESTADO-']] + [valores['-FILIACAO-']])
            
        writer = pd.ExcelWriter('arquivo.xlsx')
        cadastro_df.to_excel(writer)
        writer.save()
        sg.popup_quick('Usuário cadastrado com sucesso!')
