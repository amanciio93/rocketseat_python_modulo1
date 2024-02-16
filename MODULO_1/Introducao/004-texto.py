# DECLARAÇÃO
nomeCompleto = "Jonathan Amancio Vieira Coelho da Silva"

# PERMITE A QUEBRA DE LINHAS NO TEXTO NO CÓDIGO
nomeCompletoComAspas = """
                          Jonathan
                          Amancio
                          Vieira
                          Coelho
                          da
                          Silva
                        """

nomeCompletoQuebraLinha = "Jonathan \
                           Amancio \
                           Vieira \
                           Coelho \
                           da \
                           Silva"

print(nomeCompleto)
print(nomeCompletoComAspas)
print(nomeCompletoQuebraLinha)

#FORMATAÇÃO
print("Nome Completo:", nomeCompleto) # ESPAÇO NA JUNÇÃO
print("Nome Completo:" + nomeCompleto) # SEM ESPAÇO NA JUNÇÃO
print("Nome Completo: %s" % nomeCompleto)
print(f"Nome Completo: {nomeCompleto}")