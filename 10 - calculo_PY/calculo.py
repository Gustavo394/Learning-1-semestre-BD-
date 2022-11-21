n, h, s, p = 0, 1, 1, 0

while True:
    try:
        n = int(input('Informe um número maior que 50 para calcular o H: '))
        if n < 50:
            print('Por favor insira um número que seja maior que 50')
        elif (n >= 50):
            break
    except:
        print('O que foi digitado não parece ser um número')

while n > 1:

    if n%2 == 0:
        h += (n*2-1)/n

    if n%2 == 1:
        h -= (n*2-1)/n
    
    n -= 1

while True:
    try:
        n = int(input('Informe um número maior que 50 para calcular o S: '))
        if n < 50:
            print('Por favor insira um número que seja maior que 50')
        elif (n >= 50):
            break
    except:
        print('O que foi digitado não parece ser um número')

while n > 1:

    if n%2 == 0:
        s -= n/(n*n)

    if n%2 == 1:
        s += n/(n*n)
    
    n -= 1

count, pot = 0, 1

while True:
    try:
        n = int(input('Informe um número maior que 50 para calcular o P: '))
        if n < 50:
            print('Por favor insira um número que seja maior que 50')
        elif (n >= 50):
            break
    except:
        print('O que foi digitado não parece ser um número')

while True:
    
    while pot <= n:
        count +=1
        mult = count
        total = 0

        while (mult != 1):
            if count % mult == 0:
                total += 1
            mult -= 1

        if total == 1:
            p += count/pot**3
            pot += 2

    if pot > n:
        break

print (f'O valor dos cálculos de H = {h}\nO valor dos cálculos de S = {s}\nO valor dos cálculos de P = {p}')
