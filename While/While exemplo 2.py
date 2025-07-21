linha = 0
#while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira
#nesse exemplo, o bloco de código será executado enquanto a variável linha for menor que 3
#o bloco de código imprime o número da linha e da coluna, e incrementa a variável linha em 1
#dentro do bloco de código, há outro loop while que executa enquanto a variável coluna for menor que 3
#o bloco de código interno imprime o número da linha e da coluna, e incrementa a variável coluna em 1
#ao final, o loop externo incrementa a variável linha em 1, e o loop interno reinicia a variável coluna em 0
#isso resulta em uma tabela de 3 linhas e 3 colunas, onde cada célula é impressa com seu respectivo número de linha e coluna
#o resultado final será:

while linha < 3:
    coluna = 0
    while coluna < 3:
        print("Linha:", linha,  " - Coluna:", coluna)
        coluna += 1
    linha += 1

#----------------------------------

print("\n")

numeroInicial = 1
numeroFInal = int(input("Digite um número maior que 1: "))

while numeroInicial <= numeroFInal:
    print("Escolhi o numero: ", numeroInicial)
    numeroInicial += 1

#----------------------------------

print("\n")

numero = 1
numeroPar = int(input("Digite um número maior que 1: "))  

while numero <= numeroPar:
    #verifica se o número é par
    if numero % 2 == 0:
        print("O número", numero, "é par")
    numero += 1