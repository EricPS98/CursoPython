listanomes = ["Amanda", "Clarice", "Roger", "Allan"]

print(listanomes)
print(len(listanomes)) #len apresenta o tamanho da lista

print("\n -------------------------------------------------------------")
print("\n")


lista1 = ["A", "B", "C"]
lista2 = [1,2,3,4]
lista3 = [True, False, False]
lista4 = ["Roberta", 34, False]

print(lista1)
print(lista2)
print(lista3)
print(lista4)

print("\n -------------------------------------------------------------")
print("\n")
#              0      1       2    3       4        5
listaTeste = ["A", "Banana", "C", "D", "Elefante", "P"]

print(listaTeste[0])  # Imprimindo a posição 0 da lista
print(listaTeste[1])  # Imprimindo a posição 1 da lista
print(listaTeste[2])  # Imprimindo a posição 2 da lista     
print(listaTeste[3])  # Imprimindo a posição 3 da lista
print(listaTeste[4])  # Imprimindo a posição 4 da lista

print("\n")
print(listaTeste[-1])  # Imprimindo a última posição da lista
print(listaTeste[1:3])  # Imprimindo da posição 1 até a 3 (inclui a primeira posição, mas não inclui a ultima posição)
print(listaTeste[:3])  # Imprimindo os 3 primeiros elementos da lista (inicio não declarado (= mínimo), apenas o fim)
print(listaTeste[2:])  # Imprimindo a partir da posição 2 até o final da lista (fim não declarado (= máximo))
print(listaTeste[::2])  # Imprimindo a lista pulando de 2 em 2 elementos (não declarado inicio (=minimo) nem fim (=maximo), apenas o intervalo)
print(listaTeste[::-1])  # Imprimindo a lista de trás para frente (início não declarado (= mínimo), fim não declarado (= máximo), apenas o intervalo negativo)
