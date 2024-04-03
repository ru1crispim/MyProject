#Criando listas

jedi=list(("Anakin","Obi-Wan","Yoda"))

#print(jedi)
#print(type(jedi))

#Incluir dado no final da lista
#jedi.append("Mace Mindu")

#Inserir dado na lista, substituindo por um ja existente
#jedi.insert(2,"Mace Mindu")

#Percorrer todos os elementos de uma lista
#for i in jedi:
#    print([i])

#Incluir dado na lista utilizando o INPUT e APPEND

#jedi.append(input("Informe um nome: "))
#jedi.insert(2,input("Informe um nome para subtituir: "))
#jedi.pop()
#jedi.remove("Anakin")


#print(jedi)

#Unir uma lista a outra
#nomes = ["A","B","C"]
#outros_nomes = ["D","E","F"]
#nomes.extend(outros_nomes)
#copia_nomes = nomes.copy()
#copia_nomes.append("G")
#print(nomes)
#print(copia_nomes)
#print(f"O tamanho da lista:{len(copia_nomes)}")
#print(f"O nome A aparece:{copia_nomes.count("A")} vez(es)")
#copia_nomes.reverse()
#print(copia_nomes)
#copia_nomes.sort()
#print(copia_nomes)

numeros=[1,2,3,5,4,5,7]
numeros.insert(2,"A")
print(numeros)
#print(sum(numeros))
#print(f"Os 3 primeiros numeros: {numeros[0:3]}")