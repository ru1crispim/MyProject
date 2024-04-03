# Capitulo sobre funções (Criação de função com dois parametros)
def CalculoVelocidadeMedia (dist,temp):
    velocidade_media = dist/temp
    return "A velocidade média é {} km/h".format(velocidade_media)


distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite a tempo da viagem: "))

mensagem = CalculoVelocidadeMedia(distancia,tempo)
print(mensagem)
