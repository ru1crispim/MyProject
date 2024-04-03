#personagens = []
#categorias = []

#for x in range(3):
    #personagens.append(input("Informe o nome do personagem: "))
    #categorias.append(input("Informe a categoria do personagem: "))

#for indice in range (3):
#    print("O personagem {} é um(a) {}".format(personagens[indice],categorias[indice]))

#print(personagens)

#Criando um dicionario

dicionario={"Luva":"EPI","Oculos":"EPI","Lampada":"Material Eletrico","Cano PVC":"Material Hidraulico"}
print("O objeto dicionario é to tipo{}".format(type(dicionario)))

print(dicionario["Luva"])
print(dicionario.get("Luva"))

for valor in dicionario.values():
    print(valor)

for chave in dicionario.keys():
    print(chave)

for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))