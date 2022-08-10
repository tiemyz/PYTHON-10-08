dicionario = {"chave" : "valor"}
print(dicionario["chave"])
dicionario["nova_chave"] = ['novo_valor']
print(dicionario)
dicionario["chave"] = "teste"
print(dicionario["nova_chave"].append("mais_um_valor"))
print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

del dicionario["chave"]
print(dicionario)
mercadinho = {"fruta" : ["abacaxi", "banana"], "preço R$" : ["2.00", "1.00"], "peso" : ["200g", "100g"]}
print(mercadinho)

lista = ["maça", "3.00", "50g"]
i=0
for chave in mercadinho.keys():
    mercadinho[chave].append(lista[i])
    i+=1
print(mercadinho) 

#import pandas as pd
#mercadinho = pd.DataFrame(mercadinho)
#print(mercadinho)

