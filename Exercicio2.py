respostas_positivas = 0

perguntas = [
    "Você telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").lower()
    if resposta == "sim":
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é suspeito.")
elif 3 <= respostas_positivas <= 4:
    print("Você é cúmplice.")
elif respostas_positivas == 5:
    print("Você é o assassino.")
else:
    print("Você é inocente.")