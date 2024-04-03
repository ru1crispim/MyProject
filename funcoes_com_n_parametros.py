#Criando uma função com n paramentros
def fSaudacao(pPeriodo, *pNome):
    for i in pNome:
        if pPeriodo.lower() in ('manha',"m"):
            print(f"Bom dia, {i}! Como vai?")
        elif pPeriodo.lower() in ('tarde',"t"):
            print(f"Boa tarde, {i}! Como vai?")
        else:
            print(f"Boa noite, {i}! Como vai?")

fSaudacao("M","João","Maria","Paulo")