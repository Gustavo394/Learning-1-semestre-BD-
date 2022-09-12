from fileinput import close
from multiprocessing.resource_sharer import stop
from operator import index, indexOf
import PySimpleGUI as sg
import pandas as pd

def __init__():
    layout = [        
        [sg.Text('CPF', font=('Arial', 20)), sg.Input('', size=(28), font=('Arial', 20), key='-LOGCPF-')],
        [sg.Button('Logar', expand_x=True, font=('Arial', 20), key='-LOGAR-')],
    ]
    return sg.Window('Logar', layout=layout, margins=(10, 10), finalize=True)

def fun_cadastro():
    layout_cadastro = [
        [sg.Text('Nome', font=('Arial', 20)), sg.Input('', size=(28), font=('Arial', 20), key='-NOME-'),
        sg.Text('Idade', font=('Arial', 20)), sg.Input('', size=(3), font=('Arial', 20), key='-IDADE-')],
        [sg.Text('CPF', font=('Arial', 20)), sg.Input('', size=(20), font=('Arial', 20), key='-CPF-')],
        [sg.Text('Endereço: ', font=('Arial', 20)),
        sg.Text('Rua', font=('Arial', 20)), sg.Input('', size=(20), font=('Arial', 20), key='-RUA-'),
        sg.Text('Nº', font=('Arial', 20)), sg.Input('', size=(5), font=('Arial', 20), key='-NUM-')],
        [sg.Text('Complemento', font=('Arial', 20)), sg.Input('', size=(25), font=('Arial', 20), key='-COMP-')],
        [sg.Text('Bairro', font=('Arial', 20)), sg.Input('', size=(21), font=('Arial', 20), key='-BAIRRO-'),
        sg.Text('CEP', font=('Arial', 20)), sg.Input('', size=(10), font=('Arial', 20), key='-CEP-')],
        [sg.Text('Cidade', font=('Arial', 20)), sg.Input('', size=(35), font=('Arial', 20), key='-CDD-')],
        [sg.Text('Estado', font=('Arial', 20)), sg.Input('', size=(35), font=('Arial', 20), key='-ESTADO-')],
        [sg.Text('Filiação', font=('Arial', 20)), sg.Input('', size=(35), font=('Arial', 20), key='-FILIACAO-')],
        [sg.Button('Salvar', expand_x=True, font=('Arial', 20), key='-SALVAR-')],
    ]
    return sg.Window('Registro', layout=layout_cadastro, margins=(10, 10), finalize=True)

inicio, cadastro = __init__(), None

while True:
    excel_header = ['Nome', 'Idade', 'CPF', 'Rua', 'Numero', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'Estado', 'Filiação']
    cadastro_df = pd.DataFrame(data = pd.read_excel('arquivo.xlsx', engine='openpyxl'), columns=excel_header)
    window, eventos, valores = sg.read_all_windows()

    if window == inicio and eventos == sg.WINDOW_CLOSED:
        break

    if window == inicio and eventos in ['-LOGAR-']:
        if valores['-LOGCPF-'] == '':
            sg.popup_quick('CPF não informado')
        elif valores['-LOGCPF-'] in str(cadastro_df['CPF']):
            window.close()
            sg.popup_ok('Bem vindo!')
            cadastro = fun_cadastro()
        else:
            sg.popup_quick('CPF não encontrado')

    if window == cadastro and eventos == sg.WINDOW_CLOSED:
        cadastro.close()
        inicio = __init__()
    
    if window == cadastro and eventos in ['-SALVAR-']:
        if valores['-NOME-'] and valores['-IDADE-'] and valores['-CPF-'] and valores['-RUA-'] and valores['-NUM-'] and valores['-COMP-'] and valores['-BAIRRO-'] and valores['-CEP-'] and valores['-CDD-'] and valores['-ESTADO-'] and valores['-FILIACAO-'] != '':
            l = cadastro_df['Nome'].count()
            cadastro_df.loc[l+1] = ([valores['-NOME-']] + [valores['-IDADE-']] + [valores['-CPF-']]
                + [valores['-RUA-']] + [valores['-NUM-']] + [valores['-COMP-']] + [valores['-BAIRRO-']]
                + [valores['-CEP-']] + [valores['-CDD-']] + [valores['-ESTADO-']] + [valores['-FILIACAO-']])
                
            writer = pd.ExcelWriter('arquivo.xlsx')
            cadastro_df.to_excel(writer)
            writer.save()
            cadastro.close()
            cadastro = fun_cadastro()
            sg.popup_quick('Usuário cadastrado com sucesso!')
        else:
            sg.popup('Vazio')
        