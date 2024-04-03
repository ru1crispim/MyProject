#Importando as funcoes do script Calculadora
import calculadora

#Testando

#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = calculadora.somar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(soma))

substração = calculadora.subtrair(valor1,valor2)

print("A subtração é {}".format(substração))
