class IdadeMaximaExcedida (Exception):
    def __str__(self):
        return "A idade não pode ser superior a 125 anos"

try:
    idade = int(input("Insira sua idade: "))

    if idade < 0:
        raise ValueError("Valor da idade não pode ser menor que zero")
    elif idade > 125:
        raise IdadeMaximaExcedida
except ValueError as error:
    print("Erro: ", error)
except Exception as error:
    print("Aconteceu um erro: ", error)
else:
    print(f"Você tem {idade} anos")