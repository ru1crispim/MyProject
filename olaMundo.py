

try:
    num_mes = int(input("Digite o numero de um mês (1-12): "))
    meses = ["J,F,M,A,M,J,J,A,S,O,N,D"]
    mes = meses[num_mes-1]
    print("O mês correspondente é: ", mes)
except:
    print("ERRO: Você precisa digitar um numero inteiro entre 1 e 12.")