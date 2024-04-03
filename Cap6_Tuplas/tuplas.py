#Convertendo uma lista em tupla com a função tuple()

nomes=["João","Maria","Pedro","Sara"]
print(nomes)

#Cria-se uma nova variavel para armazenar a tupla

tupla_nomes= tuple(nomes)
print(tupla_nomes)

for nome in tupla_nomes:
    print(nome)

posicao_maria = nomes.index("Maria")
print(posicao_maria) #Para localizar a posição da Maria

contagem_elementos_nomes = len(nomes)
print(contagem_elementos_nomes)
