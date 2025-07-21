dicionario = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42
}

print(dicionario) #imprime o dicionário
print(len(dicionario)) #imprime o tamanho do dicionário
print(type(dicionario)) #imprime o tipo do dicionário

print("\n ------------------------------------------------------ \n")

#Cópia do dicionário exemplo 1
dicionario2 = dicionario.copy() #copia o dicionário
print("Exemplo dicionario2: ", dicionario2) #imprime o dicionário copiado

print("\n ------------------------------------------------------ \n")

#Cópia do dicionário exemplo 2 
dicionario3 = dict(dicionario) #copia o dicionário
print("Exemplo dicionario3: ", dicionario3) #imprime o dicionário copiado

print("\n ------------------------------------------------------ \n")

dicionarioPessoas = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42,
    "Pedro": 53
}

print(dicionarioPessoas) #imprime o dicionário com chaves duplicadas (Considera apenas a última chave duplicada)

#Pegar a idade da Marcela
dados = dicionarioPessoas["Marcela"] #Exemplo 1
dados2 = dicionarioPessoas.get("Pedro") #Exemplo 2 (com get)

print("Idade da Marcela: ", dados) #imprime a idade da Marcela
print("Idade do Pedro: ", dados2) #imprime a idade do Pedro

#Pegar somente os nomes do dicionário (coluna 1)
nomes = dicionarioPessoas.keys() #pega as chaves do dicionário
print("Nomes: ", nomes) #imprime os nomes

#Pegar somente as idades (coluna 2)
idades = dicionarioPessoas.values() #pega os valores do dicionário  
print("Idades: ", idades) #imprime as idades

print("\n ------------------------------------------------------ \n")

alimentos = {
    "arroz": 35.90,
    "macarrao": 21.90,
    "feijao": 29
}

print(alimentos) #imprime o dicionário de alimentos

#Alterando o valor do macarrão
alimentos["macarrao"] = 39.90 #altera o valor do macarrão (Exemplo 1)
print("Alimentos após alteração do macarrão: ", alimentos) #imprime o dicionário após alteração

#Alterando o valor do feijão
alimentos.update({"feijao": 31}) #altera o valor do feijão (Exemplo 2)
print("Alimentos após atualização do feijão: ", alimentos) #imprime o dicionário após atualização  