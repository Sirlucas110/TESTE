valores = []
while True:
    numero = int(input('Digite um numero: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado!!!')
    else:
        print('Valor duplicado!! Não vou adicionar')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

print(valores.sort())