Lista1 = ["A", "B", "C"]
Lista2 = ["D", "E", "F"]

Lista1.extend(Lista2) #Extende une as duas listas

print(Lista1)  # Exibe a lista resultante

Lista1.remove("E")  # Remove o elemento "E" da lista1
print(Lista1)  # Exibe a lista1 após a remoção

Lista1.pop(2)  # Remove o elemento na posição 2 da lista1
print(Lista1)  # Exibe a lista1 após a remoção do elemento na posição 2

Lista1.pop()  # Remove o último elemento da lista1
print(Lista1)  # Exibe a lista1 após a remoção do último elemento

#Removendo o primeiro elemento da lista1

del Lista1[0]  # Remove o primeiro elemento da lista1
print(Lista1)  # Exibe a lista1 após a remoção do primeiro elemento

Lista1.clear()  # Limpa todos os elementos da lista1
print(Lista1)  # Exibe a lista1 após a limpeza

Lista1.append("Maça")  # Adiciona o item "Maça" à lista1
print(Lista1)  # Exibe a lista1 após a adição de "Maça"

Lista1.insert(1, "Goiaba")  # Insere o item "Goiaba" na posição 1 (segunda posição) da lista1
print(Lista1)  # Exibe a lista1 após a inserção de "Goiaba"

Lista1.insert(1, "Laranja")  # Insere o item "Laranja" na posição 1 (segunda posição) da lista1
print(Lista1)  # Exibe a lista1 após a inserção de "Laranja"

if "Laranja" in Lista1:  # Verifica se "Laranja" está na lista1
    print("Sim, a Laranja está na Lista")  # Exibe mensagem se "Laranja" estiver na lista1
else:
    print("Não encontramos a fruta")  # Exibe mensagem se "Laranja" não estiver na lista1

Lista1[2] = "Banana"  # Substitui o item na posição 2 (terceira posição) da lista1 por "Banana"
print(Lista1)  # Exibe a lista1 após a substituição

Lista1[1:3] = ["A", "B"]
print(Lista1)  # Exibe a lista1 após a substituição de um intervalo de elementos