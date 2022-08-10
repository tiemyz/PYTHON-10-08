numeros = {"zero" : 0, "um" : 1, "dois" : 2, "três" : 3, "quatro" : 4, "cinco" : 5, "seis" : 6, "sete" : 7, "oito" : 8, "nove" : 9}
num_tel = []
for i in range(10):
    num = input("Digite o número do seu celular: ")
    num_tel.append(numeros[num])
print(num_tel)


#------------------#------------------#

numeros = {"zero" : 0, "um" : 1, "dois" : 2, "três" : 3, "quatro" : 4, "cinco" : 5, "seis" : 6, "sete" : 7, "oito" : 8, "nove" : 9}
num_tel = []
for i in range(10):
    num = input("Digite o número do seu celular: ")
    if num in numeros.keys():
        num_tel.append(numeros[num])
    else:
        print("vc errou!")
print(num_tel)








