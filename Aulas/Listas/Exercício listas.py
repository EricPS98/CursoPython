frutas = ["maçã", "banana", "manga", "abacate", "laranja"]

frutas.append("kiwi") #adiciona "kiwi" no final da lista

frutas.remove("banana") #remove o valor "banana" da lista

if "abacaxi" in frutas:
    print("Abacaxi está na lista")
else:
    print("Abacaxi não está na lista")

print (len(frutas)) #imprime o tamanho da lista

print(frutas[0]) #Imprime o valor da primeira posição da lista

print(frutas[-1]) #Imprime o valor da última posição da lista