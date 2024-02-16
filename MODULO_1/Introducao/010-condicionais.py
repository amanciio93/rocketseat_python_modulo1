#CONDICIONAIS IF, ELIF, ELSE
""" 
    >
    <
    >=
    <=
    ==
    !=
"""

idade = 30

if idade < 18:
    print("Menor idade, não pode ter CNH.")
else:
    print("Maior idade, pode ter CNH")

if idade >= 18:
    print("ADULTO")
elif idade > 12 and idade < 18:
    print("ADOLESCENTE")
else:
    print("CRIANÇA")

mensagem = "Pode ter CNH" if idade >= 18 else "Não pode ter CNH"
print(mensagem)