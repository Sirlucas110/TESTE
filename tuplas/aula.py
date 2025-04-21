#Tuplas são imutáveis

#Variáveis compostas
#         tupla  listas  dict
#lanche = ()     []      {}

a = (2, 3, 6, 8)
b = (5, 9, 0)
c = a + b
print(c)


lanche = ('Hambúrguer', 'Suco', 'Sobremesa', 'Pizza')


#Organiza em ordem
print(sorted(lanche))

print('O lanche na posição 1 é ',lanche[1])

print('O lanche na posição -1 é ',lanche[-1])
#Mostra do elemento 1 até o 3
print('O lanche da posição 1 até 3 é ',lanche[1:3])
#Mostra do elemento 2 até o final
print('O lanche da posição 2 até o último é ',lanche[2:])
#Mostra do primerio elemento até o 2
print('O lanche da posição inicial até o 2 é ',lanche[:2])


for cont in range(0 , len(lanche)):
    print(f'Vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')