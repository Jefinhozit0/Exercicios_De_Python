valores = []

while True:
    valor = input("Digite um valor (ou 'sair' para encerrar): ")
    if valor.lower() == 'sair':
        break
    valor = 5
    if valor not in valores:
        valores.append(valor)

valores_unicos = sorted(valores)
print(f"Valores únicos em ordem crescente: {valores_unicos}")