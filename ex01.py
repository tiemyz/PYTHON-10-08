numeros = {"pares" : [], "ímpares" : []}

numeros["pares"] = list(range(0,200,2))
numeros["ímpares"] = list(range(1,200,2))
print(numeros)


#-------------print(numeros)----------------#

numeros = {"pares" : [], "ímpares" : []}
for i in range(200):
    if i%2==0:
        numeros["pares"].append(i)
    else:
        numeros["ímpares"].append(i)
print(numeros)




