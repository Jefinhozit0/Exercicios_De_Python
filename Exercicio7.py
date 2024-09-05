alunos = {}

for _ in range(5):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    situacao = "Aprovado" if media >= 7 else "Recuperação" if 5 <= media < 7 else "Reprovado"
    alunos[nome] = {'media': media, 'situacao': situacao}

print("\nInformações dos alunos:")
for aluno, info in alunos.items():
    print(f"{aluno} - Média: {info['media']} - Situação: {info['situacao']}")