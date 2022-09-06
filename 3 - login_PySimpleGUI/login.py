from PySimpleGUI import PySimpleGUI as sg
import csv

sg.theme('Topanga')

menu_layout = [
    ['Login', ['Instruções']]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('A informação necessária para logar está acima no menu "Login"', font=(20))],
    [sg.Text('Login:', size=(6), font=(20)), sg.Input('', expand_x=True, font=(20), key='-LOGIN-')],
    [sg.Text('Senha:', size=(6), font=(20)), sg.Input('', expand_x=True, font=(20), password_char='*', key='-SENHA-'), sg.Button('Ver', key='-VER-')],
    [sg.Button('Logar', expand_x=True, font=(20), key='-LOGAR-')]
]

class Login():
    def __init__(janela):
        janela.window = sg.Window('Login', layout=layout, margins=(10,10))
        with open('usuario.csv', 'r') as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=',')
            for i, linha in enumerate(arquivo_csv):
                if i == 1:
                    janela.login = str(linha[i])
                    janela.senha = str(linha[i])
                    print('Login: ' + janela.login)
                    print('Senha: ' + janela.senha)
        janela.window.read(timeout=1)

    def about(janela):
        sg.popup_ok('Login: ' + janela.login, 'Senha: ' + janela.senha)
    
    def logar(janela):
        if (janela.valores['-LOGIN-'] and janela.valores['-SENHA-']) == '':
            sg.popup_ok('Usuário ou senha inválidos!')
        elif (janela.valores['-LOGIN-'] == janela.login) and (janela.valores['-SENHA-'] == janela.senha):
            sg.popup_ok('Bem-vindo ' + janela.login + ' você logou!')
        else:
            sg.popup_ok('Usuário ou senha incorretos, tente novamente!')

    def start(janela):
        while True:
            eventos, janela.valores = janela.window.read()
            if eventos in (None, 'Exit', sg.WINDOW_CLOSED):
                break

            if eventos in ('Instruções'):
                janela.about()

            if eventos in ['-VER-']:
                sg.popup_quick_message('Senha: ' + janela.valores['-SENHA-'])

            if eventos in ['-LOGAR-']:
                janela.logado = janela.logar()
                
Login().start()