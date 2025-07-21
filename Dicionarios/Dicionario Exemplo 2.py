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

alimentos["salsicha"] = 35
print(alimentos) #adiciona o valor da salsicha ao dicionário

alimentos.pop("salsicha") #remove o valor da salsicha do dicionário
print(alimentos)

alimentos.popitem() #remove o último item do dicionário
print(alimentos) #imprime o dicionário após remoção do último item

alimentos.clear() #limpa o dicionário
print(alimentos) #imprime o dicionário após limpeza

alimentos["arroz"] = 35.90 
alimentos["macarrao"] = 21.90
alimentos["feijao"] = 29

print("\n ------------------------------------------------------ \n")

print(alimentos) #imprime o dicionário de alimentos restaurado

del alimentos["arroz"] #remove o arroz do dicionário 
print(alimentos) #imprime o dicionário após remoção do arroz

if "feijao" in alimentos: #verifica se o macarrão está no dicionário
    print("Alimento encontrado com sucesso!") #imprime se o macarrão está no dicionário
else:
    print("O Alimento não foi encontrado na lista")

print("\n ------------------------------------------------------ \n")

letras = {
    "Letra 1": "A",
    "Letra 2": "B", 
    "Letra 3": "C",
    "Letra 4": "D",
    "Letra 5": "E",
    "Letra 6": "F",
}

print(letras) #imprime o dicionário de letras

for posicao in letras:
    print(posicao) #imprime cada posição (primeiro parâmetro) e seu respectivo valor no dicionário

for i in letras:
    print(letras[i]) #imprime cada valor do dicionário (exemplo 1)

print("\n ------------------------------------------------------ \n")

for contador in letras.values():
    print(contador) #imprime cada valor do dicionário (exemplo 2)

print("\n ------------------------------------------------------ \n")

for titulo, valor in letras.items():
    print(titulo, "-", valor) #imprime cada título e seu respectivo valor no dicionário

print("\n ------------------------------------------------------ \n")

exemplo1 = {
    "A" : 1,
    "B" : 2
}

exemplo2 = {
    "C" : 3,
    "D" : 4
}

exemplo3 = {
    "E" : 5,
    "F" : 6
}

unirVariosDicionarios = {
    "Dicionario 1": exemplo1,
    "Dicionario 2": exemplo2,  
    "Dicionario 3": exemplo3
}
print(unirVariosDicionarios) #imprime o dicionário com outros dicionários como valores

print("\n ------------------------------------------------------ \n")

escola = {
    "Turma 1" : {
        "Andre:" : 10,
        "Amanda:" : 8
    },
    "Turma 2" : {
        "Cesar:" : 6,
        "Alessandra:" : 7
    },
    "Turma 3" : {
        "Roger:" : 9,
        "Rosiane:" : 10
    }
}

for turma1, turma2 in escola.items(): #Define os elementos dentro do dicionario "Escola"
  print(turma1) #imprime o primeiro elemento (Dentro da primeira {} - no caso, "Turma 1, Turma 2, "Turma 3")
  for turma1, turma2 in turma2.items(): #Dentro da "Turma x", define os elementos dentro do subdicionário dessa "Turma x: "
    print("Aluno:", turma1, "- Nota: ", turma2) #Imprime os 2 elementos dentro do subdicionário e reseta o primeiro loop até acabar 
