import PySimpleGUI as sg
import pandas as pd

sg.theme('Topanga')
sg.set_options(font=('Arial', 20))

layout = [
    [sg.Text('Login'), sg.Input(key='ID_LOGIN')],
    [sg.Text('Senha'), sg.Input(key='ID_SENHA'), sg.Checkbox('\U0001f441\uFE0F')],
]

class App():
    def __init__(self):
        self.window = sg.Window('Login', layout=layout, margins=(10, 10), finalize=True)
        self.window.read()

    def start(self):
        while True:
            eventos, self.valores = self.window.read()

            if eventos in (None, sg.WIN_CLOSED):
                break

App().start()