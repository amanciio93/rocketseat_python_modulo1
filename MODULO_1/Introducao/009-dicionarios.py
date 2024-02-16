#Coleção não ordenadas de chaves, pares, valor;
pessoa = {"nome": "Jonathan", "idade": 30, "cidade": "S. J. do Rio Preto"}

#Exibindo o dicionario
print("Meu dicionario pessoa:", pessoa)

#Acessando valores pro chave
print("Onde ", pessoa["nome"], " mora? ")
print("Em ", pessoa["cidade"])

#Atribuindo chaves e valores
pessoa["sobrenome"] = "Amancio"
print("Pessoa com sobrenome atribuido:", pessoa)

#Alterando valores
pessoa["idade"] = 31
print("Idade atualizada: ", pessoa["idade"])

#Método DEL
del pessoa["sobrenome"]
print("Pessoa sem sobrenome: ", pessoa)

#Método Keys
chaves = pessoa.keys()
print("Chavez de pessoa: ", chaves)
#Para acessar posições especificas, converta para list() e use o indice desejado.

#Método Values
valores = pessoa.values()
print("Valores de pessoa: ", valores)

#Método items
itens = pessoa.items()
print("Pares chave-valor dicionário pessoa: ", itens)