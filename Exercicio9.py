funcionario = {}

funcionario['nome'] = input("Digite o nome do funcionário: ")
funcionario['ano_nascimento'] = int(input("Digite o ano de nascimento do funcionário: "))
funcionario['ctps'] = int(input("Digite o número da CTPS (0 se não tiver): "))

if funcionario['ctps'] != 0:
    funcionario['ano_contratacao'] = int(input("Digite o ano de contratação: "))
    funcionario['salario'] = float(input("Digite o salário do funcionário: "))
    idade_atual = 2023 - funcionario['ano_nascimento']
    anos_contribuicao = 2023 - funcionario['ano_contratacao']
    anos_para_aposentar = 35 - anos_contribuicao
    idade_aposentadoria = idade_atual + anos_para_aposentar
    funcionario['idade_aposentadoria'] = idade_aposentadoria

print("\nInformações do funcionário:")
for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")