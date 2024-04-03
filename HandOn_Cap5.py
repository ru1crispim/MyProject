#Funcao calculo Pizza

def calcula_pizza (tamanho,quantidade_sabores):
    if tamanho.lower() == "pequeno":
        preco = 20
    elif tamanho.lower() == "medio":
        preco = 30
    else:
        preco + 40
    preco = (quantidade_sabores * 5)+ preco

    return preco
print(calcula_pizza("pequeno",1))

#Viagem intergalatica

verificar_atmosfera = lambda planeta: "Ufa, pode respirar a vontade" if planeta != "Hoth" else "Cuidado, este planeta é perigoso"

print(list(map(verificar_atmosfera,["Tatooine", "Hoth", "Endor", "Alderaan", "Naboo"])))
