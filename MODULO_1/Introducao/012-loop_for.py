#LOOPS = LAÇOS

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Elementos no LISTA com FOR:")
for elemento in lista:
    print(elemento)
    
print("Chaves do DIC PESSOA com FOR:")
pessoa = {"nome":"Jonathan", "idade":30, "curso":"Python"}
for chave in pessoa.keys():
    print(chave)

print("Valores das chaves do DIC PESSOA com FOR:")
for valor in pessoa.values():
    print(valor)

print("Chave & Elemento do DIC PESSOA com FOR:")
for items in pessoa.items():
    print(items)    
    
for chave, valor in pessoa.items():
    print(chave+": ", valor)
    
print("FOR COM RANGE():")
for numeros in range(5):
    print("Número: ", numeros)
    
print("FOR COM RANGE() E LEN():")
for indice in range(0, len(lista)):
    print("Indice:", indice, " => elemento:", lista[indice])
    
#USANDO ENUMERATE
listaEnumerate = ["a", "e", "i", "o", "u"]
for indice, valor in enumerate(listaEnumerate):
    #Format string
    print(f"{indice}: {valor}")