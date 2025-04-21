valores = []

posicao_maior = []
posicao_menor = []
for contador in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {contador}: ')))

for posicao, valor in enumerate(valores):
    if valor == max(valores):
        posicao_maior.append(posicao)
    if valor == min(valores):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {valores}')
print(f'O maior valor da lista é {max(valores)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(valores)}, nas posições {posicao_menor}')


