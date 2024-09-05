estoque = {
    'produto1': {'quantidade': 10, 'valor_unitario': 2.5},
    'produto2': {'quantidade': 2, 'valor_unitario': 13.0},
    'produto3': {'quantidade': 100, 'valor_unitario': 23.0},
    'produto4': {'quantidade': 22, 'valor_unitario': 73.0},
    'produto5': {'quantidade': 12, 'valor_unitario': 366.0},
   
}

total_compra = 0

while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if produto.lower() == 'sair':
        break
    if produto in estoque:
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        if quantidade <= estoque[produto]['quantidade']:
            valor_total = quantidade * estoque[produto]['valor_unitario']
            print(f"Item adicionado: {quantidade}x {produto} - Valor total: {valor_total}")
            estoque[produto]['quantidade'] -= quantidade
            total_compra += valor_total
        else:
            print("Quantidade indisponível em estoque.")
    else:
        print("Produto não encontrado.")

print(f"\nTotal de itens comprados: {total_compra}")