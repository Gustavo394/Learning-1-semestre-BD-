import PySimpleGUI as sg

sg.theme('Topanga')

class palavra():
    def __init__():
        layout_login = [
            [sg.Text('')],
            [sg.Input('')],
            [sg.Button('')],
            [sg.Combo('')],
            [sg.Checkbox('')]
        ]
        return sg.Window('Teste', layout=layout_login, margins=(0, 0))

while True:
    window, eventos, valores = sg.read_all_windows()

    

"""
vetor = ['Lorem ipsum dolor sit amet consumtetur adipisumg elit']
frase = str(vetor)
print(frase)
palavra = 'sum'
sum = frase.count(palavra)
print(sum)
"""