numeros = [5, 3, 6, 8, 7, 9, 1, 2] 

#Isso cria uma cópia da lista numeros
b = numeros[:]


#trocar o numero na posição 1
numeros[1] = 6

#Adiciona um número na lista
numeros.append(2)

#Coloca em ordem
numeros.sort(reverse=True)

#Insere um numero na lista
numeros.insert(5, 8)

#Remove o numero da ultima posicao ou da posicao que quiser
numeros.pop()

if 1 in numeros:
    numeros.remove(9)
else:
    print('Não achei o número 1')

print(len(numeros))
print(numeros)
