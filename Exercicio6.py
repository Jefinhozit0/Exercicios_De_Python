clientes = {
    'cliente1': {'nome': 'Carlos', 'idade': 25},
    'cliente2': {'nome': 'Arthur', 'idade': 17},
    'cliente3': {'nome': 'Sidinei', 'idade': 12},
    'cliente4': {'nome': 'Maitê', 'idade': 21},
    'cliente5': {'nome': 'João', 'idade': 19},
    'cliente6': {'nome': 'Miguel', 'idade': 16},
    'cliente7': {'nome': 'Rayssa', 'idade': 18},
    
}

maiores_idade = 0
menores_idade = 0

for cliente, info in clientes.items():
    if info['idade'] >= 18:
        print(f"{info['nome']} é maior de idade.")
        maiores_idade += 1
    else:
        print(f"{info['nome']} é menor de idade.")
        menores_idade += 1

print(f"Clientes maiores de idade: {maiores_idade}")
print(f"Clientes menores de idade: {menores_idade}")