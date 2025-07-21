#Variável no escopo global
nome = "Silvana"

def funcao1():
    print(nome)

def funcao2():
    print(nome)

funcao1()
funcao2()

print("\n --------------------------------------------------- \n")

nomeSobrenome = "Steve Jobs"

def funcaoNomeSobrenome():
    print(nomeSobrenome)

def funcaoNomeSobrenome2():
    #Escopo local - Variável local
    #Quando mudamos o valor da variável dentro da função, não estamos mudando o valor, estamos criando uma nova variável
    # por isso que a variável global não é afetada
    nomeSobrenome = "Bill Gates"
    print(nomeSobrenome)

funcaoNomeSobrenome() #Usando Variável Global
funcaoNomeSobrenome2() #Usando a variável local de dentro da função (é como se tivesse criado uma nova variável)
print(nomeSobrenome) #Usando Variável Global

print("\n --------------------------------------------------- \n")

idade = 32

def funcaoIdade1():
    print(idade)

def funcaoIdade2():
    global idade #Acessando a variável global ao inves de criar uma nova
    idade = 34 # Alterando a variável global (não recomendado, nesse caso é para fim acadêmico mesmo)
    print(idade)

funcaoIdade1() #Imprimindo a vairável global (sem alteração)
funcaoIdade2() #Imprimindo a vairável global (alterada)
print(idade)   #Imprimindo a vairável global (após alteração)

