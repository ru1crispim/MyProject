#Criação de variavel de resposta

#resposta = 0

#while (resposta!= "42"):
 #   resposta = input("Qual é a resposta para a vida, universo e tudo mais?")
#print("Parabéns! Você acertou!")

#Variavel contadora

#i = 0

#while(i<10):
    #print("O numero é: ", i)
    #i = i+1

for i in range(1,10,2):
    print("O numero é: ",i)

op = 0
while (op!=4):
    print("Bem vindo ao atendimento da Claro!")
    
    print("1 - Financeiro")
    print("2 - Assistencia Técnica")
    print("3 - Falar com atendente")
    print("4 - Sair")
    op = int(input("Digite uma das opções abaixo: \n"))

    if op == 1:
        print("Estamos te transferindo para a nossa area de cobrança.")

    elif op == 2:
        print("Estamos te transferindo para a nossa area de agendamento de visitas técnica.")

    elif op == 3:
        print("Estamos te transferindo para um atendente Claro.")

print("Obrigado pelo contato! Até logo!")








