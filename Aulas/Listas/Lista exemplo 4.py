listaNome = ["Bryan", "Leticia", "Bruna", "Clarice","Carla"]

for i in listaNome: #Imprimindo os itens da lista
    print(i)

print("\n -------------------------------------------------------- \n")

#Exemplo impressão com for 2
[print(item) for item in listaNome] #Imprimindo os itens da lista com compreensão de lista

print("\n -------------------------------------------------------- \n")

i = 0 # É necessário inicializar a variável i para usar no while

while i < len(listaNome): #Imprimindo os itens da lista com while
    print(listaNome[i])
    i += 1

print("\n -------------------------------------------------------- \n")
listaNomeC = [] #Criando uma lista vazia para armazenar os nomes que possuem a letra "c"

for item in listaNome: #Imprimindo os itens da lista com for
    if "c" in item:
        listaNomeC.append(item) #Adicionando o item na lista se a letra "c" estiver no nome

print(listaNomeC) #Imprimindo a lista com os nomes que possuem a letra "c"

print("\n -------------------------------------------------------- \n")

print(listaNome) #Imprimindo a lista original

listaMinuscula = [item.lower() for item in listaNome] #Criando uma nova lista com os nomes em letras minúsculas
print(listaMinuscula) #Imprimindo a lista com os nomes em letras minúsculas

listaMaiuscula = [item.upper() for item in listaNome] #Criando uma nova lista com os nomes em letras maiúsculas
print(listaMaiuscula) #Imprimindo a lista com os nomes em letras maiúsculas