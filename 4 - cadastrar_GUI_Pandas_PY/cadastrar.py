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
        [sg.Button('Consultar', expand_x=True, font=('Arial', 20), key='-CONS-'),
        sg.Button('Cadastrar', expand_x=True, font=('Arial', 20), key='-CAD-'),
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

def fun_consultar():
    layout_consultar = [
        [sg.Text('Consulta', font=('Arial', 20)),
        sg.Combo(consulta, size=(34, 5), font=('Arial', 20), key='-LIST-')],        
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
        [sg.Button('Consultar', expand_x=True, font=('Arial', 20), key='-CONSULTAR-'),
        sg.Button('Alterar', expand_x=True, font=('Arial', 20), key='-ALTERAR-'),
        sg.Button('Voltar', expand_x=True, font=('Arial', 20), key='-VOLTAR-')],
    ]
    return sg.Window('Consultar', layout=layout_consultar, margins=(10, 10), finalize=True)

inicio, logado, cadastro, consultar, alterar = __init__(), None, None, None, None
consulta = []


while True:
    excel_header = ['Nome', 'Idade', 'CPF', 'Rua', 'Numero', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'Estado', 'Filiação']
    cadastro_df = pd.DataFrame(data = pd.read_excel('arquivo.xlsx', engine='openpyxl'), columns=excel_header)
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

    if window == logado and eventos in ['-CAD-']:
        logado.hide()
        cadastro = fun_cadastro()

    if window == logado and eventos in ['-CONS-']:
        for linha in cadastro_df['Nome']:
                if linha != '':
                    consulta.append(linha)
                if linha == '':
                    break
        logado.hide()
        consultar = fun_consultar()

    if window == logado and eventos == sg.WINDOW_CLOSED or eventos in ['-SAIR-']:
        logado.close()
        inicio = __init__()

    if window == cadastro and eventos == sg.WINDOW_CLOSED or eventos in ['-CANCELAR-']:
        cadastro.close()
        logado.un_hide()
    
    if window == consultar and eventos == sg.WINDOW_CLOSED or eventos in ['-VOLTAR-']:
        consulta.clear()
        consultar.close()
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
                writer = pd.ExcelWriter('arquivo.xlsx')
                cadastro_df.to_excel(writer)
                writer.save()
                cadastro.close()
                cadastro = fun_cadastro()
                sg.popup_ok('Usuário cadastrado com sucesso!')
            else:
                sg.popup_ok('CPF já cadastrado')
        else:
            sg.popup_ok('Todos os campos precisam ser preenchidos')

    if window == consultar and eventos in ['-CONSULTAR-']:
        n = 0
        for linha in cadastro_df['Nome']:
            if linha == valores['-LIST-']:
                window['-NOME-'].update(value=cadastro_df.loc[n].at['Nome'])
                window['-IDADE-'].update(value=cadastro_df.loc[n].at['Idade'])
                window['-CPF-'].update(value=cadastro_df.loc[n].at['CPF'])
                window['-RUA-'].update(value=cadastro_df.loc[n].at['Rua'])
                window['-NUM-'].update(value=cadastro_df.loc[n].at['Numero'])
                window['-COMP-'].update(value=cadastro_df.loc[n].at['Complemento'])
                window['-BAIRRO-'].update(value=cadastro_df.loc[n].at['Bairro'])
                window['-CEP-'].update(value=cadastro_df.loc[n].at['CEP'])
                window['-CDD-'].update(value=cadastro_df.loc[n].at['Cidade'])
                window['-ESTADO-'].update(value=cadastro_df.loc[n].at['Estado'])
                window['-FILIACAO-'].update(value=cadastro_df.loc[n].at['Filiação'])
                break
            n += 1

    if window == consultar and eventos in ['-ALTERAR-']:
        n = 0
        for linha in cadastro_df['CPF']:
            if valores['-CPF-'] == '':
                sg.popup_ok('Campo vazio')
            elif valores['-CPF-'] == str(linha):
                cadastro_df.at[n, 'Nome'] = valores['-NOME-']
                cadastro_df.at[n, 'Idade'] = valores['-IDADE-']
                cadastro_df.at[n, 'CPF'] = valores['-CPF-']
                cadastro_df.at[n, 'Rua'] = valores['-RUA-']
                cadastro_df.at[n, 'Numero'] = valores['-NUM-']
                cadastro_df.at[n, 'Complemento'] = valores['-COMP-']
                cadastro_df.at[n, 'Bairro'] = valores['-BAIRRO-']
                cadastro_df.at[n, 'CEP'] = valores['-CEP-']
                cadastro_df.at[n, 'Cidade'] = valores['-CDD-']
                cadastro_df.at[n, 'Estado'] = valores['-ESTADO-']
                cadastro_df.at[n, 'Filiação'] = valores['-FILIACAO-']
                writer = pd.ExcelWriter('arquivo.xlsx')
                cadastro_df.to_excel(writer)
                writer.save()
                consultar.close()
                consultar = fun_consultar()
                sg.popup_ok('Alterado com sucesso!')
                break
            n +=  1


        excel_header = ['Nome']
        df = pd.DataFrame(data = pd.read_excel('exemplo.xlsx', engine='openpyxl'), columns=excel_header)
        df.at[0, 'Nome'] = input('')
        writer = pd.ExcelWriter('arquivo.xlsx')
        df.to_excel(writer)
        writer.save()
        print(cadastro_df)


        excel_header = ['Nome']
        df = pd.DataFrame(data = pd.read_excel('exemplo.xlsx', engine='openpyxl'), columns=excel_header)
        l = df['Nome'].count()
        df.loc[l+1] = input('')
        writer = pd.ExcelWriter('arquivo.xlsx')
        df.to_excel(writer)
        writer.save()
