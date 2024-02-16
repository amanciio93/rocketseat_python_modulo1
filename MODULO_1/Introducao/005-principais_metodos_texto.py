# MÉTODOS UPPER & LOWER

nome = "Jonathan"
sobrenome = "Amancio"

print("Imprimindo o nome na tela: ", nome)
print("Imprimindo o nome na tela com o método UPPER(): ", nome.upper())
print("Imprimindo o nome na tela com o método LOWER(): ", nome.lower())

# Uma STRING é uma cadeia de caracteres, e sendo assim podemos acessar seu indice;
print("Acessando posição 0 da String nome: ", nome[0])
print("Acessando posição 1 da String nome: ", nome[1])
print("Acessando posição 2 da String nome: ", nome[2])
print("Acessando posição 3 da String nome: ", nome[3])
print("Acessando posição 4 da String nome: ", nome[4])
print("Acessando posição 5 da String nome: ", nome[5])
print("Acessando posição 6 da String nome: ", nome[6])
print("Acessando posição 7 da String nome: ", nome[7])

# MÉTODO COUNT()
# Sensitive Case
nomeCompleto = "Jonathan Amancio Vieira Coelho da Silva"
print("Usando o para contar o nº de ocorrencias do caracter 'a': ", nomeCompleto.count("a"))

#MÉTODO FIND()
print("Posição da primeira ocorrência: ", nomeCompleto.find("a"))

#MÉTODO ENCODE e DECODE
print("Método ENCODE()", nomeCompleto.encode())
print("Método DECODE()", nomeCompleto.encode().decode())

#MÉTODO REPLACE
print("Replace de a por A: ", nomeCompleto.replace("a", "A"))
print("Replace de Amancio por Silva: ", nomeCompleto.replace("Amancio", "Silva"))

#MÉTODO JOIN
print("Usando join: ", "_".join(nome))

#MÉTODO SPLIT
print("Usando SPLIT: ", nomeCompleto.split(" "))

#MÉTODO STRIP
"""
    O método Strip() em Python remove ou trunca os caracteres fornecidos do início e do final da string original . O comportamento padrão do método strip() é remover os espaços em branco do início e do final da string.
"""
nomeCompletoEspacos = " Jonathan A. V. C da Silva "
print("Nome completo com espaços: ", nomeCompletoEspacos)
print("Usando STRIP: ", nomeCompletoEspacos.strip(" "))

#MÉTODO STARTWITH 
print("Inicia com Jonathan? ", nomeCompleto.startswith("Jonathan"))

#MÉTODO IN
print("Existe Vieira em nomeCompleto? ", "Vieira" in nomeCompleto)

#MÉTODO NOT
print("Existe Martins em nomeCompleto? ", "Martins" in nomeCompleto)