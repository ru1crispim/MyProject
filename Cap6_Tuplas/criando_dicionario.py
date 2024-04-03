#Criando um dicionario vazio

dicionario = {}

#Incluindo dados no dicionario

dicionario["Andre David"] = "Professor"
dicionario["Maria Becker"] = "Advogada"
print(dicionario)

for nome, profissao in dicionario.items():
    print("{} é {}".format(nome,profissao))

#For com metodo values() para mostrar apenas os valores do dicionario
for valor in dicionario.values():
    print(valor)

#For com metodo keys() para mostrar apenas as chaves do dicionario

for chave in dicionario.keys():
    print(chave)


#Inserindo dados no dicionario

cadastro_clientes = {}

cadastro_clientes["Andre"] = "Buyer"

#Excluindo um dado do dicionario informando a chave
cadastro_clientes.pop("Andre")

novo_nome = input("Insira um novo nome: ")
novo_profissao = input("Insira a profissão: ")

cadastro_clientes[novo_nome]=novo_profissao


for nome, profissao in cadastro_clientes.items():
    print("{} works as a {}".format(nome,profissao))


#nova_chave = input("Informe o nome do novo colaborador: ")
#novo_valor = input("Informe o cargo deste novo colaborador: ")

#dicionario[nova_chave] = novo_valor
#dicionario.update({"Andre Marques":"Motorista"})
#dicionario.pop("Andre Marques")

#for chave, valor in dicionario.items():
 #   print("O colaborador {} desempenha a funcao de {}".format(chave,valor))

#dicionario.clear()
    

