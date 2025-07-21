listaMinMax = [52, 10, 20, 100, 50, 300, 5]

print(min(listaMinMax))
print(max(listaMinMax))

print("\n ------------------------------------------------- \n")

# Lista de 0 até 10
listaNumeros1ate10 = [i for i in range(101) if i <= 10] # Cria uma lista de 0 a 100 e filtra para manter apenas os números de 0 a 10

print(listaNumeros1ate10)

print("\n ------------------------------------------------- \n")

listaDoisEmDois = list(range(1, 100, 2))  # Cria uma lista de 2 em 2 de 0 a 100
print(listaDoisEmDois)

print("\n ------------------------------------------------- \n")

listaOriginal = ["Carro", "Moto", "Bicicleta", "Lancha"]
listaCopiada = listaOriginal.copy()  # Cria uma cópia da lista original

print(listaCopiada)

print("\n ------------------------------------------------- \n")

lista1Letras = ["A", "B", "C"]
lista2Numeros = [1, 2, 3]

listaJoin = lista1Letras + lista2Numeros  # Junta duas listas
print(listaJoin)

print("\n ------------------------------------------------- \n")

l1 = ["a1", "b1", "c1"]
l2 = [11, 12, 13]

for item in l2:
    l1.append(item)  # Adiciona os itens de l2 na lista l1 

print(l1)

      
