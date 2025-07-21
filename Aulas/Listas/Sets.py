"""
add - Adiciona um elemento ao final da lista.
union - unifica sets, ou seja, combina dois conjuntos em um único conjunto sem duplicatas.
intersection - encontra os elementos comuns entre dois conjuntos.

summetric_difference_update - remove os elementos que estão em ambos os conjuntos, mantendo apenas os elementos exclusivos de cada conjunto.

summetric_difference - retorna um novo conjunto com os elementos que estão em um conjunto ou no outro, mas não em ambos.
"""

setExemploNumeros =  set() # Cria um conjunto vazio
setExemploNumeros.add(1)
setExemploNumeros.add(2)
setExemploNumeros.add(3)
setExemploNumeros.add(4)
setExemploNumeros.add(5)
setExemploNumeros.add("Amanda")

print(setExemploNumeros)  # Resultado: {1, 2, 3, 4, 5, 'Amanda'}

print("\n ----------------------------------- \n")

setLetras = {"A", "B", "C"}
print(setLetras)  # Não imprime na ordem correta, pois os sets não mantêm a ordem dos elementos.

print("\n ----------------------------------- \n")

set1 = {"Allan", "Berenice", "Roger"}
set2 = {39, 21, 45}

uniaoSets = set1.union(set2) # Combina os dois conjuntos em um único conjunto, sem duplicatas.
print(uniaoSets)  # Imprime a união dos dois conjuntos, sem manter a ordem.

print("\n ----------------------------------- \n")

listaSet1 = {"Python", "C++", "Java"}
listaSet2 = {"VisualG", "Lógica", "Python"}

print("\n")
imprimindoOsDoisParaConferir = listaSet1.union(listaSet2)  # Combina os dois conjuntos em um único conjunto, sem duplicatas.
print(imprimindoOsDoisParaConferir)  # Imprime a união dos dois conjuntos, sem mantér a ordem.

valorQueEstaEmAmbosOsSets = listaSet1.intersection(listaSet2)  # Encontra os elementos comuns entre os dois conjuntos.
print(valorQueEstaEmAmbosOsSets)  # Imprime os elementos que estão em ambos os conjuntos.

listaSet1.symmetric_difference_update(listaSet2) # Remove os elementos que estão em ambos os conjuntos, mantendo apenas os elementos exclusivos de cada conjunto.
print(listaSet1)  # Imprime os elementos exclusivos de cada conjunto após a atualização.

print("\n ----------------------------------- \n")

listaS1 = {"Python", "C++", "Java"}
listaS2 = {"VisualG", "Lógica", "Python"}

naoEstaoEmAmbosOsSets = listaS1.symmetric_difference(listaS2)  # Retorna um novo conjunto com os elementos que estão em um conjunto ou no outro, mas não em ambos.
print(naoEstaoEmAmbosOsSets)  # Imprime os elementos que estão em um conjunto ou no outro, mas não em ambos.

print("\n ----------------------------------- \n")

setNumero = {1, 2, 3, 4, 5, 6, 6, 7, 8}
print(setNumero)  # Imprime o conjunto, que não mantém duplicatas, então o número 6 só aparece uma vez.
print(len(setNumero))  # Imprime o tamanho do conjunto, que é 8, pois não há duplicatas.

setExemplo1 = {"A", "B", "C"}
setExemplo2 = {1, 2, 3}
setExemplo3 = {True, False, True}
setExemplo4 = {"Maça", 12, True}
setExemplo2.update(setExemplo1)  # Atualiza setExemplo2 com os elementos de setExemplo1.

print("\n")
print(setExemplo1)  # Imprime o conjunto original, que contém os elementos "A", "B" e "C".
print(setExemplo2)  # Imprime o conjunto atualizado, que agora contém os elementos atualizados de setExemplo1.
print(setExemplo3)  # Imprime o conjunto que contém valores booleanos.
print(setExemplo4)  # Imprime o conjunto que contém uma string, um número e um valor booleano.

print("\n ----------------------------------- \n")

listaObjetos = {"Casa", "Moto", "Bicicleta", "Lancha"}

for i in listaObjetos:
    print(i)  # Imprime cada elemento do conjunto listaObjetos.

listaObjetos.add("Carro")  # Adiciona o elemento "Carro" ao conjunto listaObjetos.
print(listaObjetos)  # Imprime o conjunto atualizado, que agora contém "Carro".

listaObjetos.remove("Moto")  # Remove o elemento "Bicicleta" do conjunto listaObjetos.
print(listaObjetos)  # Imprime o conjunto atualizado, que agora não contém mais "Moto".

listaObjetos.pop()  # Remove e retorna um elemento aleatório do conjunto listaObjetos.
print(listaObjetos)  # Imprime o conjunto atualizado após a remoção de um elemento

print ("Bicicleta" in listaObjetos)
