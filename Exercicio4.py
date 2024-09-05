numeros = []

while True:
    valor = input("Digite um número (ou 'sair' para encerrar): ")
    if valor.lower() == 'sair':
        break
    valor = int(valor)
    numeros.append(valor)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(f"Números digitados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")