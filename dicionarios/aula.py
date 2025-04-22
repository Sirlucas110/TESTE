pessoas = {
    'nome': 'Lucas',
    'sexo': 'M',
    'Idade': 22
}
for keys in pessoas.keys():
    print(keys)

for keys, values in pessoas.items():
    print(f'{keys} = {values}')
print(f'O {pessoas["nome"]} tem {pessoas.get("Idade")}')
#Duas formas de acessar
print(pessoas['Idade'])
print(pessoas.get('nome'))
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())