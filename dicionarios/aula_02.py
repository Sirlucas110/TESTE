estado = {}
brasil = []
for contador in range(0 ,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['uf'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for keys, values in estado.items():
        print(f'O campo {keys} tem valor {values}')
    