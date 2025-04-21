tabela = ('Flamengo', 'Palmeiras', 'Fluminense', 'Juventude', 'Ceará', 'Cruzeiro', 'Bragantino', 'Corinthians', 'Vasco da Gama', 'Internacional', 'Mirassol', 'Botafogo', 'Fortaleza', 'Santos', 'Vitória', 'São Paulo', 'Bahia', 'Atlético-MG', 'Sport')

#5 primeiros colocados
print('Os 5 primeiros colocados são ',tabela[:5])

#4 últimos colocados
print('Os 4 últimos colocados são ', tabela[15:])

#Tabela em ordem alfabética
print(sorted(tabela))

#Posição do São Paulo
print(f'O São Paulo está em {tabela.index("São Paulo")+1}ª')