valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar?[Ss/Nn]'))
    if resposta in 'Nn':
        break

print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')