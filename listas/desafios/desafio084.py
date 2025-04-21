dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer sair?[S/N]'))
    if resposta in 'Ss':
        break
print(pessoas)
print(len(pessoas))
