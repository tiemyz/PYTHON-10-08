emocoes = {"amo" : "🥰"}
frase = input("Diga eu te amo: ")
frase_alterada = frase.split(" ")[:]
print(list(enumerate(frase.split(""))))
for indice,palavra in enumerate(frase.split("")):
    if palavra in emocoes.keys():
        frase_alterada[indice] = emocoes[palavra]
for palavra in frase_alterada:
    print(palavra, end="")



