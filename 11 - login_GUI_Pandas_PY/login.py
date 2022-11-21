import PySimpleGUI as sg
import pandas as pd

sg.theme('Topanga')
sg.set_options(font=('Arial', 20))

menu_layuout = [
    ['Menu', ['Deslogar', 'Menu inicial']]
]

layout_login = [
    [sg.Text('Login'), sg.Input(key='ID_LOGIN', expand_x=True, size=(30, 1))],
    [sg.Text('Senha'), sg.Input(key='ID_SENHA', expand_x=True, size=(24, 1), password_char='#'), sg.Checkbox('\U0001f441\uFE0F', size=(2, 1), enable_events=True, key='ID_VER')],
    [sg.Button('Logar', expand_x=True, key='ID_LOGAR'), sg.Button('Sair', expand_x=True, key='ID_SAIR')]
]

layout_logado = [
    [sg.Menu(menu_layuout)],
    [sg.Text(key='ID_USUARIO')],
    [sg.Button('Consultar', key='ID_CONSULTAR'), sg.Button('Cadastrar', key='ID_CADASTRAR'), sg.Button('Sair', key='ID_SAIR')],
]

class App():
    def __init__(self):
        self.window = sg.Window('Login', layout=layout_login, size=(1280, 720), margins=(10, 10), finalize=True)
        self.window.read(timeout=0)

    def login(self):
        if self.valores['ID_LOGIN'] and self.valores['ID_SENHA'] != '':
            for x in range(int(self.df['Login'].count())):
                if str(self.df.at[x, 'Login']) == str(self.valores['ID_LOGIN']) and str(self.df.at[x, 'Senha']) == str(self.valores['ID_SENHA']):
                    self.window.close()
                    self.window = sg.Window('Login', layout=layout_logado, size=(1280, 720), margins=(10, 10), finalize=True)
                    self.window.read(timeout=0)
                    return
            if True:
                sg.popup('Login ou senha inválidos')
        else:
            sg.popup('Preencha todos os campos')

    def deslogar(self):
        self.window = sg.Window('Login', layout=layout_login, size=(1280, 720), margins=(10, 10), finalize=True)
        self.window.read(timeout=0)
        sg.popup('Nice')

    def start(self):
        while True:
            eventos, self.valores = self.window.read()
            excel_header = ['Login', 'Senha', 'Nome', 'CPF']
            self.df = pd.DataFrame(data = pd.read_excel('11 - a/arquivo.xlsx', engine='openpyxl'), columns=excel_header)

            if eventos in (None, 'ID_SAIR', sg.WIN_CLOSED):
                break

            if eventos in ['ID_VER']:
                if self.valores['ID_VER'] == True:
                    self.window['ID_SENHA'].update(password_char='')
                else:
                    self.window['ID_SENHA'].update(password_char='#')

            if eventos in ('Deslogar'):
                self.deslogar()

            if eventos in ['ID_LOGAR']:
                self.login()

App().start()