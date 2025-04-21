
numero = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), 
          int(input('Digite um número: ')))

print('O número 9 apareceu',numero.count(9), 'vezes')
if 3 in numero:
    print(f'O número 3 apareceu pela primeira vez na posição {numero.index(3)+1}')
else:
    print('O número 3 não foi digitado nenhuma vez')
for par in numero:
    if par % 2 == 0:
        print(f'Os números pares são {par}')