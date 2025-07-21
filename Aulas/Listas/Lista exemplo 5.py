listaLetras = ["A", "C", "E", "D", "F", "B"]
print(listaLetras)  # Lista original

listaLetras.sort()
print(listaLetras)  # Ordenando a lista em ordem alfabética

listaLetras.sort(reverse=True)
print(listaLetras)  # Ordenando a lista em ordem alfabética reversa

print("\n ------------------------------------------ \n")

listaNumeros = [4, 9, 5, 20, 16, 14, 12]
print(listaNumeros)  # Lista original

listaNumeros.sort()
print(listaNumeros)  # Ordenando a lista em ordem crescente

listaNumeros.sort(reverse=True)
print(listaNumeros)  # Ordenando a lista em ordem decrescente

print("\n ------------------------------------------ \n")

listaMaiMin = ["Sofá", "tv", "carro", "Casa", "Armario"]
listaMaiMin.sort()
print(listaMaiMin)  # Ordenando a lista, mas sem considerar maiúsculas e minúsculas

listaMaiMin.sort(key= str.lower) # Ordenando a lista, considerando minúsculas e maiúsculas
print(listaMaiMin)  # Ordenando a lista, considerando minúsculas e maiúsculas