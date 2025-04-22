valores = [[], []]

for c in range(0,7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)

valores[0].sort()
valores[1].sort()
print(valores[0])
print(valores[1])
