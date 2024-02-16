# Definindo um procedimento
def saudacao(nome):
    print(f"Olá {nome}.")
    
#Chamando um procedimento
saudacao("Jonathan")

# Definindo uma função
def calcIdade(anoNasc):
    idadeAtual = 2024 - anoNasc
    return idadeAtual

# Chamando a função
anoNasc = input("Insira o ano do seu nascimento: ")

print("A sua idade atual é de: ", calcIdade(int(anoNasc)))