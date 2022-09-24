import PySimpleGUI as sg
import pandas as pd

def __init__():
    layout = [        
        [sg.Text('CPF', font=('Arial', 20)), sg.Input('', size=(28), font=('Arial', 20), key='-LOGCPF-')],
        [sg.Button('Logar', expand_x=True, font=('Arial', 20), key='-LOGAR-')],
    ]
    return sg.Window('Logar', layout=layout, margins=(10, 10), finalize=True)

def fun_logado():
    layout_logado = [
        [sg.Text(f'Usuario: {nome}')],
        [sg.Button('Cadastrar', expand_x=True, font=('Arial', 20), key='-CAD-'),
        sg.Button('Sair', expand_x=True, font=('Arial', 20), key='-SAIR-')],
    ]
    return sg.Window('Bem Vindo', layout=layout_logado, margins=(10, 10), finalize=True)

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
        [sg.Button('Salvar', expand_x=True, font=('Arial', 20), key='-SALVAR-'),
        sg.Button('Cancelar', expand_x=True, font=('Arial', 20), key='-CANCELAR-'),],
    ]
    return sg.Window('Registro', layout=layout_cadastro, margins=(10, 10), finalize=True)

inicio, logado, cadastro = __init__(), None, None

while True:
    excel_header = ['Nome', 'Idade', 'CPF', 'Rua', 'Numero', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'Estado', 'Filiação']
    cadastro_df = pd.DataFrame(data = pd.read_excel('4 - cadastrar_GUI_Pandas/arquivo.xlsx', engine='openpyxl'), columns=excel_header)
    window, eventos, valores = sg.read_all_windows()

    if window == inicio and eventos == sg.WINDOW_CLOSED:
        break

    if window == inicio and eventos in ['-LOGAR-']:
        if valores['-LOGCPF-'] == '':
            sg.popup_ok('CPF não informado')
        else:
            encontrado = False
            l = 0
            for cpf in cadastro_df['CPF']:
                if cpf == int(valores['-LOGCPF-']):
                    encontrado = True
                    nome = cadastro_df.loc[l].at['Nome']
                    break
                l = l + 1
            if encontrado == True:
                window.close()
                sg.popup_ok(f'Boas vindas {nome}!')
                logado = fun_logado()
            elif encontrado == False:
                sg.popup_ok('CPF não encontrado')

    if window == logado and eventos in ['-SAIR-']:
        logado.close()
        inicio = __init__()

    if window == logado and eventos in ['-CAD-']:
        logado.hide()
        cadastro = fun_cadastro()

    if window == logado and eventos == sg.WINDOW_CLOSED:
        break

    if window == cadastro and eventos == sg.WINDOW_CLOSED:
        cadastro.close()
        logado.un_hide()
    
    if window == cadastro and eventos in ['-SALVAR-']:
        if valores['-NOME-'] and valores['-IDADE-'] and valores['-CPF-'] and valores['-RUA-'] and valores['-NUM-'] and valores['-COMP-'] and valores['-BAIRRO-'] and valores['-CEP-'] and valores['-CDD-'] and valores['-ESTADO-'] and valores['-FILIACAO-'] != '':
            salvar = True
            for ver in cadastro_df['CPF']:
                if valores['-CPF-'] == str(ver):
                    salvar = False
                    break
            if salvar == True:
                l = cadastro_df['Nome'].count()
                cadastro_df.loc[l+1] = ([valores['-NOME-']] + [valores['-IDADE-']] + [valores['-CPF-']]
                    + [valores['-RUA-']] + [valores['-NUM-']] + [valores['-COMP-']] + [valores['-BAIRRO-']]
                    + [valores['-CEP-']] + [valores['-CDD-']] + [valores['-ESTADO-']] + [valores['-FILIACAO-']])
                writer = pd.ExcelWriter('4 - cadastrar_GUI_Pandas/arquivo.xlsx')
                cadastro_df.to_excel(writer)
                writer.save()
                cadastro.close()
                cadastro = fun_cadastro()
                sg.popup_ok('Usuário cadastrado com sucesso!')
            else:
                sg.popup_ok('CPF já cadastrado')
        else:
            sg.popup_ok('Todos os campos precisam ser preenchidos')
    
    if window == cadastro and eventos in ['-CANCELAR-']:
        cadastro.close()
        logado.un_hide()