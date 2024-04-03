#funcao lambda (Syntax: lambda arguments: expression)

soma=lambda a,b:a+b

print(soma(5,5))

#funcao lambda com desvios condicionais (Syntax: lambda arguments: expression (if true) if COMPARACAO else expression (if false))

verificar_positivo = lambda x:"Positivo"if x>=0 else "Negativo"
print("O numero informado é: ", verificar_positivo(-1))

#funcao com MAP:

def dobro(x):
    return x *2

print(list(map(dobro,[1,2,3])))

#funcao lambda com MAP:

dobro = list(map(lambda x: x*2,[8,6,5]))
print(dobro)
