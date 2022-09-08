nome = input('Olá, por gentileza informe seu nome: ')
salario_h = float(input('Informe quanto ganha por hora: '))
dependentes = int(input('Informe o número de dependentes: '))
aumento = 0

if dependentes > 3:
    aumento = (((salario_h/100) *3) *3)

if aumento > 0:
    print(f'Olá {nome}, seu salário atualmente é de',
    f'{salario_h} por hora, você tem direito a um aumento de {aumento}')
    
elif aumento == 0:    
    print(f'Olá {nome}, seu salário atualmente é de',
    f'{salario_h} por hora, você não tem direito a um aumento')
