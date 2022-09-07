import PySimpleGUI as sg
import csv, os

sg.theme('Topanga')

usuario = []
senha = []

class Petshop():
    def janela_login():
        menu_layout = [
            ['Cadastros', ['Novo', 'Consultar ou alterar']]
        ]
        layout = [
            [sg.Menu(menu_layout)],
            [sg.Text('Boas vindas ao petshop PET-REPET')],
            [sg.Image('petshop.png', expand_x=True, expand_y=True)],
            [sg.Text('Login:', size=(5), font=(20)), sg.Input('', expand_x=True, font=(20), key='-LOGIN-')],
            [sg.Text('Senha:', size=(5), font=(20)), sg.Input('', expand_x=True, font=(20), password_char='*', key='-SENHA-'), sg.Button('Ver', key='-VER-')],
            [sg.Button('Logar', expand_x=True, expand_y=True, font=(20), key='-LOGAR-')]
        ]
        return sg.Window('Login', layout=layout, margins=(10, 10), finalize=True)

    def janela_novo():
        novo_layout = [
            [sg.Text('Usuário:', size=(6), font=(20)), sg.Input('', expand_x=True, font=(20), key='-CAD_USUARIO-')],
            [sg.Text('Senha:', size=(6), font=(20)), sg.Input('', expand_x=True, font=(20), key='-CAD_SENHA-')],
            [sg.Button('Cadastrar', expand_x=True, font=(20), key='-CADASTRAR-')]
        ]
        return sg.Window('Novo cadastro', layout=novo_layout, finalize=True)

    def janela_consultar_alterar():

        with open('usuarios.csv', 'r') as consulta:
            reader = csv.reader(consulta)
            for linha in reader:
                if linha != '':
                    usuario.append(linha[0])
                    senha.append(linha[1])
                if linha == '':
                    break            
        consulta.close()        

        c_a_layout = [
            [sg.Text('Consultar e alterar usuário cadastrado', expand_x=True, font=(20))],
            [sg.Combo(usuario, expand_x=True, font=(20), key='-VISOR-')],
            [sg.Text('Usuário:', size=(6), font=(20)), sg.Input('', expand_x=True, font=(20), key='-C_A_USUARIO-')],
            [sg.Text('Senha:', size=(6), font=(20)), sg.Input('', expand_x=True, font=(20), key='-C_A_SENHA-')],
            [sg.Button('Consultar', expand_x=True, font=(20), key='-CONSULTAR-'), sg.Button('Alterar', expand_x=True, font=(20), key='-ALTERAR-')]
        ]
        return sg.Window('Consultar ou alterar cadastro', layout=c_a_layout, finalize=True)

    janela_l, janela_n, janela_c_a = janela_login(), None, None

    while True:
        window, eventos, valores = sg.read_all_windows()
        
        if window == janela_l and eventos == sg.WIN_CLOSED:
            break
        
        if window == janela_c_a and eventos == sg.WIN_CLOSED:
            janela_c_a.close()
            janela_l.un_hide()

        if window == janela_n and eventos == sg.WIN_CLOSED:
            janela_n.close()
            janela_l.un_hide()
        
        if eventos in ['-LOGAR-']:
            entrou = False
            if valores['-LOGIN-'] and valores['-SENHA-'] != '':
                with open('usuarios.csv', 'r') as validacao:
                    reader = csv.reader(validacao)
                    num = 0
                    for linha in reader:
                        if valores['-LOGIN-'] == linha[0] and valores['-SENHA-'] == linha[1]:
                            entrou = True
                            break                        
                    if entrou == True:
                        sg.popup_ok(f'Bem vindo {linha[0]}')
                    elif entrou == False:
                        sg.popup_ok('Usuário ou senha incorreto')
            else:
                sg.popup_ok('Usuário ou senha inválidos')

        if eventos in ['-VER-']:
            if valores['-SENHA-'] != '':
                sg.popup_quick_message('Senha digitada: '+ valores['-SENHA-'])
            else:                
                sg.popup_quick_message('Nenhuma senha foi digitada')

        if window == janela_l and eventos == 'Novo':
            janela_l.hide()
            janela_n = janela_novo()
        
        if eventos in ['-CADASTRAR-']:
            if valores['-CAD_USUARIO-'] and valores['-CAD_SENHA-'] != '':
                with open('usuarios.csv', 'a', newline='') as novo:
                    writer = csv.writer(novo)
                    writer.writerow([valores['-CAD_USUARIO-']] + [valores['-CAD_SENHA-']])
                    janela_n['-CAD_USUARIO-'].update(value='')
                    janela_n['-CAD_SENHA-'].update(value='')
                    usuario.clear()
                    senha.clear()
                novo.close()
                sg.popup_ok('Usuario cadastrado com sucesso')
            else:
                sg.popup_ok('Usuário ou senha inválidos')
        

        if window == janela_l and eventos == 'Consultar ou alterar':
            janela_l.hide()
            janela_c_a = janela_consultar_alterar()
        
        if eventos in ['-CONSULTAR-']:
            if valores['-VISOR-'] != '':
                num = 0
                for linha in usuario:
                    if linha == valores['-VISOR-']:
                        window['-C_A_USUARIO-'].update(value=linha)
                        window['-C_A_SENHA-'].update(value=senha[num])
                    num = num + 1
            else:
                sg.popup_ok('Selecione um usuário antes de tentar consultar')

        if eventos in ['-ALTERAR-']:
            if valores['-VISOR-'] != '':
                with open ('usuarios.csv', 'r') as alterar_r, open ('usuarios_temp.csv', 'w', newline='') as alterar_w:
                    reader = csv.reader(alterar_r)
                    writer = csv.writer(alterar_w)
                    num = 0
                    for linha in reader:
                        if valores['-VISOR-'] == linha[0]:
                            writer.writerow([valores['-C_A_USUARIO-']] + [valores['-C_A_SENHA-']])
                            sg.popup_ok('Usuário alterado com sucesso')
                            usuario.clear()
                            senha.clear()
                            janela_c_a.close()
                        else:
                            writer.writerow(linha)
                        num = num + 1
                        print(num)
                os.remove('usuarios.csv')
                os.rename('usuarios_temp.csv', 'usuarios.csv')                
                janela_c_a = janela_consultar_alterar()
            else:
                sg.popup_ok('Selecione um usuário antes de tentar alterar')
        
Petshop()