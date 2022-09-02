from PySimpleGUI import PySimpleGUI as sg
import datetime

sg.theme('Topanga')

while True:
    try:
        inicio = [
            [sg.Text('Informe seu nome'), sg.Input(key='nome', size=(20, 1))],
            [sg.Button('Próximo')]
        ]
        janela = sg.Window('Cor de roupa', inicio)
        eventos, valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos == 'Próximo':
            janela.close()
            nome = valores['nome']
            instrucoes = [
                [sg.Text(f'Olá {nome} é um prazer conhecer você!')],
                [sg.Text('Vamos realizar um procedimento para saber se você está vestindo roupas de uma única cor, nenhuma roupa de uma certa cor, cores que não se repetem ou se está vestindo cores igualmente distribuídas.', size=(60, 3))],
                [sg.Text('Escolha uma das opções:')],
                [sg.Button('Estou vestindo somente roupas de uma única cor', size=(14, 5), key='1'),
                sg.Button('Não estou usando nenhuma roupa de uma certa cor', size=(14, 5), key='2'),
                sg.Button('Estou vestindo roupas de cores que não se repetem', size=(14, 5), key='3'), 
                sg.Button('Estou vestindo roupas de cores igualmente distribuídas', size=(14, 5), key='4')],
            ]
            janela = sg.Window('Instruções', instrucoes)
            eventos, valores = janela.read()
            info = eventos
            janela.close()

            if eventos == sg.WINDOW_CLOSED:
                break

            condicao = True
            com_info = True

            cor = [
                [sg.Text('Selecione a cor da roupa:')],
                [sg.Button('Preto'), sg.Button('Branco'), sg.Button('Amarelo'), sg.Button('Azul'), sg.Button('Verde'), sg.Button('Vermelho')]                
            ]
            peca = [
                [sg.Text('Selecione a cor de cada peça:')],
                [sg.Text('Camisa'), sg.Combo(['Preto', 'Branco', 'Amarelo', 'Azul', 'Verde', 'Vermelho'])],
                [sg.Text('Calça'), sg.Combo(['Preto', 'Branco', 'Amarelo', 'Azul', 'Verde', 'Vermelho'])],
                [sg.Text('Meia'), sg.Combo(['Preto', 'Branco', 'Amarelo', 'Azul', 'Verde', 'Vermelho'])],
                [sg.Text('Sapato'), sg.Combo(['Preto', 'Branco', 'Amarelo', 'Azul', 'Verde', 'Vermelho'])],
                [sg.Button('Confirmar')],
            ]
            falso = [
                [sg.Text('A afirmação é falsa!')]
            ]
            verdadeiro = [
                [sg.Text('A afirmação é verdadeira!')]
            ]
            vazio = [
                [sg.Text('Falta informação!')]
            ]

            if (info == '1') or (info == '2'):
                janela = sg.Window('Cor', cor)
                eventos, valores = janela.read()
                cor = eventos
                janela.close()

            if eventos == sg.WINDOW_CLOSED:
                break

            janela = sg.Window('Peça', peca)
            eventos, valores = janela.read()
            peca = valores
            janela.close()

            if eventos == sg.WINDOW_CLOSED:
                break                

            if (eventos == 'Confirmar'):
                if (valores[0] == '') or (valores[1] == '') or (valores[2] == '') or (valores[3] == ''):
                    print(valores)
                    com_info = False
                elif (info == '1'):
                    for linha in range(4):
                        if peca[linha] != cor:
                            print(peca[linha])
                            condicao = False                            
                elif (info == '2'):
                    for linha in range(4):
                        if peca[linha] == cor:
                            condicao = False
                elif (info == '3'):
                    cont = 1
                    for linha1 in range(3):
                        for linha2 in range(cont, 3):
                            if peca[linha1] == peca[linha2]:
                                condicao = False
                        cont = cont + 1
                if (info == '4'):
                    if peca[0] == peca[1] == peca[2] == peca[3]:
                        condicao = False
                    else:
                        cont = 1
                        ver = 0
                        a = 0
                        b = 0
                        combinacao = 0
                        for linha1 in range(4):
                            for linha2 in range(cont, 4):
                                if peca[linha1] == peca[linha2]:                    
                                    if a != 1:
                                        a = a + 1
                                    elif b == 1:
                                        condicao = False
                                    elif a == 1:
                                        b = b + 1
                            cont = cont + 1
                        if (a != b):
                            condicao = False
            if com_info == False:
                janela = sg.Window('Fim', vazio)
                janela.read()
                break
            if condicao == False:
                janela = sg.Window('Fim', falso)
                janela.read()
                break
            if condicao == True:
                janela = sg.Window('Fim', verdadeiro)
                janela.read()
                break

    except Exception as erro:
        date = str(datetime.date.today())
        register_error = [erro.__class__]
        with open('register_error.txt', 'a') as error:
            for linha in register_error:
                error.write(str(date) + ' - ' + str(register_error) + '\n')
                error.seek(0)
                error.close()
                
