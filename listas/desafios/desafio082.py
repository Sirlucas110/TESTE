valores = []
lista_pares = []
lista_impares = []
while True:
    numero = (int(input('Digite um numero: ')))
    valores.append(numero)
   
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    resposta = str(input('Quer sair?[S/N]: '))
    if resposta in 'Ss':
        break
    

print(valores)
print(lista_pares)
print(lista_impares)