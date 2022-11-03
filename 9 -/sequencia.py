x = 1
while True:
    try:
        num1 = int(input(f'Digite o número {x}: '))
        break
    except:
        print('O que foi digitado não parece ser um número')

seq, seqm = 0, 0
tot, totm = 0, 0
ign, ig, igm = 0, 0, 0

while True:
    x += 1
    while True:
        try:
            num2 = int(input(f'Digite o número {x}: '))
            break
        except:
            print('O que foi digitado não parece ser um número')

    if num1 == num2-1:

        if seq == 0:
            seq += 2
            tot += num1 + num2

        else:
            seq += 1
            tot += num2

        if seq == seqm and tot > totm:
            seqm = seq
            totm = tot

        if seq > seqm:
            seqm = seq
            totm = tot

    else:
        tot = 0
        seq = 0

    if num2 == num1:

        if ig == 0:
            ig += 2

        else:
            ig += 1

        if ig == igm and num2 > ign:
            igm = ig
            ign = num2

        if ig > igm:
            igm = ig
            ign = num2

    else:
        ig = 0

    if x == 150:
        break

    num1 = num2

if (seqm > 0):
    print(f'A maior sequência consecutiva de números em ordem crescente é: {seqm}')
else:
    print('Não teve sequência consecutiva de números em ordem crescente')

if (igm > 0):
    print(f'A maior sequência consecutiva de números constantes é: {igm}')
else:
    print('Não teve sequência consecutiva de números constantes')
