pessoas = []
total_idade = 0
mulheres_cadastradas = []

while True:
    pessoa = {}
    pessoa['nome'] = input("Digite o nome da pessoa: ")
    pessoa['sexo'] = input("Digite o sexo biológico da pessoa (M/F): ").upper()
    while pessoa['sexo'] not in ['M', 'F']:
        print("Sexo inválido. Digite M para masculino ou F para feminino.")
        pessoa['sexo'] = input("Digite o sexo biológico da pessoa (M/F): ").upper()
    pessoa['idade'] = int(input("Digite a idade da pessoa: "))
    total_idade += pessoa['idade']
    pessoas.append(pessoa)

    if pessoa['sexo'] == 'F':
        mulheres_cadastradas.append(pessoa['nome'])

    continuar = input("Deseja cadastrar mais uma pessoa? (sim/não): ").lower()
    if continuar != 'sim':
        break

media_idade = total_idade / len(pessoas)
idades_acima_media = [pessoa['idade'] for pessoa in pessoas if pessoa['idade'] > media_idade]

print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")
print(f"Média de idade das pessoas: {media_idade:.2f}")
print(f"Mulheres cadastradas: {mulheres_cadastradas}")
print(f"Idades acima da média: {idades_acima_media}")