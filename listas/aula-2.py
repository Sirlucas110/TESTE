teste = []
galera = [['Joao', 10], ['Aba', 15]]

teste.append('Gustavo')
teste.append(40)


galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])
print(galera)

galera = []
dado = []
total_maior = total_menor = 0
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} maiores e {total_menor} menores de idade')