listagem_de_precos = ('Pão', 1.00, 'Leite', 5.00, 'Bolacha', 3.50, 'Refrigerante', 10.00, 'Detergente', 4.00, 'Sabonote', 2.50)

print("-"*40)
print("         LISTAGEM DE PREÇOS       ")
print("-"*40)
for pos in range(0, len(listagem_de_precos)):
    if pos % 2 ==0:
        print(listagem_de_precos[pos], "."*30, end='')
    else:
        print(f'R${listagem_de_precos[pos]}')

