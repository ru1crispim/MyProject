try:
    idade = int(input("Informe a idade do aluno: "))
    idade_amigo = input("Informe a idade do amigo do aluno: ")
    #idade_total = idade + idade_amigo
    idade_total = 5/0

except ValueError:
    print("Favor informar um valor inteiro para idade")
except TypeError:
    print("Estamos com problemas técnicos, tentando somar inteiro com string. Aguarde a correção do codigo")
except Exception as error:
    print("Aconteceu um erro! ", error)

else:
    print("A idade do aluno é {}".format(idade))
    print("A idade do amigo é {}".format(idade_amigo))
    print("A idade total é {}".format(idade_total))
finally:
    print("Obrigado por utilizar o nosso sistema!")