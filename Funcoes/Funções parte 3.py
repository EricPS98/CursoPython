#Argumentos com chaves

def provaAluno(nota1, nota2, nota3):
    print("O aluno tirou:", nota2)

provaAluno(nota1 = 9, nota2 = 7, nota3 = 10)

print("\n --------------------------------------------------- \n")

#Função com um parâmetro padrão

def funcaoNome(nome = "Python"):
    print("Meu nome é", nome)

funcaoNome("Alice")
funcaoNome("Pedro")
funcaoNome()
funcaoNome("Carolina")

print("\n --------------------------------------------------- \n")

#Passando uma lista como um argumento

def funcaoListaNumeros(numero):
    #print(numero) #Imprimir a lista inteira
    for i in numero: #Imprimindo cada posição da lista por iteração do "for"
        print(i)


listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

funcaoListaNumeros(listaNumeros)

print("\n --------------------------------------------------- \n")

def multiplicacaoDoisNumeros(numerorecebido):
    return 10 * numerorecebido

print(multiplicacaoDoisNumeros(5))
print(10, "x", 10, "=", multiplicacaoDoisNumeros(10))
print(10, "x", 8, "=", multiplicacaoDoisNumeros(8))
