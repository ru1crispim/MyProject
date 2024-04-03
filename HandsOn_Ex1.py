
#Calculo calorias

#qtd_alimentos = int(input("Infome quantas refeições você realizou durante o dia: "))
#total_calorias = 0
#for i in range(0,qtd_alimentos,1):
#    calorias=int(input("Infome o total de calorias consumido: "))
#    total_calorias = calorias + total_calorias    
#print("Para as {} refeições realizadas, você consumiu um total de {} calorias".format(qtd_alimentos,total_calorias))


# Media notas turmas impares de pares

media_impar = 0
media_par = 0
total_notas_impar = 0
total_notas_par= 0

for i in range(1,50,2):
    nota=float(input("Digite a nota do aluno da turma impar: "))
    total_notas_impar = total_notas_impar + nota

for i in range(2,50,2):
    nota=float(input("Digite a nota do aluno da turma par: "))
    total_notas_par = total_notas_par + nota

media_impar= total_notas_impar/25
media_par= total_notas_par/25

if (media_impar > media_par):
    print("A turma impar teve a maior média. Sendo: {}".format(media_impar))
else:
    print("A turma par teve a maior média. Sendo: {}".format(media_par))