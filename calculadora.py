from PySimpleGUI import PySimpleGUI as sg

sg.theme('Topanga')

layout = [
    [sg.Input('0', size=(int(15), 1), font=(20), key='-OUT-'),sg.Button('<<', font=(20)), sg.Button('C', font=(20))],
    [sg.Button('7', font=(20)), sg.Button('8', font=(20)), sg.Button('9', font=(20)), sg.Button('+', font=(20))],
    [sg.Button('4', font=(20)), sg.Button('5', font=(20)), sg.Button('6', font=(20)), sg.Button('-', font=(20))],
    [sg.Button('1', font=(20)), sg.Button('2', font=(20)), sg.Button('3', font=(20)), sg.Button('*', font=(20))],
    [sg.Button('0', font=(20)), sg.Button(',', font=(20)), sg.Button('/', font=(20)), sg.Button('=', font=(20))],
]

class App():
    def __init__(janela):
        janela.window = sg.Window('Calculadora', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=False)
        janela.resultadoado = 0
        janela.operacao = ''
        janela.window.read(timeout=1)
        for i in range(0, 5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)
    
    def igual(janela):
        if janela.operacao == '+':
            return float(janela.resultado) + float(janela.valores['-OUT-'])
        if janela.operacao == '-':
            return float(janela.resultado) - float(janela.valores['-OUT-'])
        if janela.operacao == '*':
            return float(janela.resultado) * float(janela.valores['-OUT-'])
        if janela.operacao == '/':
            return float(janela.resultado) / float(janela.valores['-OUT-'])

    def start(janela):
        while True:
            eventos, janela.valores = janela.window.read()
            if eventos in (None, 'Exit', sg.WINDOW_CLOSED):
                break
            if eventos in ('1'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='1')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '1')
            if eventos in ('2'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='2')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '2')
            if eventos in ('3'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='3')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '3')
            if eventos in ('4'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='4')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '4')
            if eventos in ('5'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='5')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '5')
            if eventos in ('6'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='6')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '6')
            if eventos in ('7'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='7')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '7')
            if eventos in ('8'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='8')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '8')
            if eventos in ('9'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='9')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '9')
            if eventos in ('0'):
                if janela.valores['-OUT-'] == '0':
                    janela.window['-OUT-'].update(value='0')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'] + '0')

            if eventos in ('C'):
                janela.resultado = 0
                janela.window['-OUT-'].update(value=janela.resultado)
            if eventos in ('<<'):
                if (janela.valores['-OUT-'] == '0'):
                    janela.window['-OUT-'].update(value='0')
                elif (janela.valores['-OUT-'][:-1] == ''):
                    janela.window['-OUT-'].update(value='0')
                else:
                    janela.window['-OUT-'].update(value=janela.valores['-OUT-'][:-1])

            if eventos in ('+'):
                if janela.operacao != '':
                    janela.resultado = janela.igual()
                else:
                    janela.operacao = '+'
                    janela.resultado = janela.valores['-OUT-']
                janela.window['-OUT-'].update(value='0')
            if eventos in ('-'):
                if janela.operacao != '':
                    janela.resultado = janela.igual()
                else:
                    janela.operacao = '-'
                    janela.resultado = janela.valores['-OUT-']
                janela.window['-OUT-'].update(value='0')
            if eventos in ('*'):
                if janela.operacao != '':
                    janela.resultado = janela.igual()
                else:
                    janela.operacao = '*'
                    janela.resultado = janela.valores['-OUT-']
                janela.window['-OUT-'].update(value='0')
            if eventos in ('/'):
                if janela.operacao != '':
                    janela.resultado = janela.igual()
                else:
                    janela.operacao = '/'
                    janela.resultado = janela.valores['-OUT-']
                janela.window['-OUT-'].update(value='0')
            
            if eventos in ('='):
                janela.resultado = janela.igual()
                janela.window['-OUT-'].update(value=janela.resultado)
                janela.resultado = 0
                janela.operacao = ''
                
App().start()
