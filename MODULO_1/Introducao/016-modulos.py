#Importando um módulo inteiro;
import math
print("Exemplo de importação de um módulo padrão (math): ")
raizQuad = math.sqrt(25)
print(f"Raiz quadrada de 25 é: {raizQuad}")

#Importando a funcionalidade sqrt do módulo Math como rq;
from math import sqrt as rq
print("Exemplo de importação de um módulo padrão (math): ")
raizQuad = rq(25)
print(f"Raiz quadrada de 25 é: {raizQuad}")

print("\nExemplo de criação e utilização de módulos personalizados: ")

#Importando meu módulo;
import meuModulo
mensagem = meuModulo.saudacao("Usuário")
print(mensagem)
dobro = print("O dobro de 100 é", meuModulo.dobro(100))