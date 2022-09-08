poluicao = float(input('Informe o indice de poluição medido: '))

if poluicao >= 0.55:
    print('Saudações, por motivos de seguração ao meio ambiente,',
    'solicitamos que todas as atividades de todas as empresas',
    'sejam suspensas imediatamente!')

elif poluicao >= 0.45:
    print('Saudações, por motivos de seguração ao meio ambiente,',
    'solicitamos que todas as atividades das empresas dos grupos',
    '1 e 2 sejam suspensas imediatamente!')

elif poluicao >= 0.3:
    print('Saudações, por motivos de seguração ao meio ambiente,',
    'solicitamos que todas as atividades das empresas do grupo',
    '1 sejam suspensas imediatamente!')

elif poluicao >= 0.27:
    print('Índice de poluição elevado, caso necessário as empresas',
    'serão notificadas para suspender as atividades!')
    
else:
    print('O índice de poluição se encontra dentro dos padroes!')
