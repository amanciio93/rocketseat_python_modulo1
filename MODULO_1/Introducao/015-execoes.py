print("Exemplo de captura de exeções")

#Tentativa
try:
    number = int(input("Integer number: "))
    result = 10 / number
    
#Captura do ValueError;
except ValueError as e:
    print(f"ValueError: {e}")
    #Descrição sobre o erro;
    raise ValueError("Tipo de variáveis incompátiveis")
#Captura do erro em 'e'
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Resultado: {result}")
finally:
    print("FIM DO PROGRAMA!!!")