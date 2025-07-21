"""
A diferença das Listas para Tuplas é que não podemos editar os elementos de uma Tupla.
Não podemos adicionar ou remover elementos de uma Tupla, mas podemos acessar os elementos.
Tuplas são imutáveis, ou seja, uma vez criadas, não podem ser alteradas.
Tuplas são definidas com parênteses () e listas com colchetes [].
"""

# Exemplo de Tupla
tuplaLetras = ("A", "B", "C", "D")
print(tuplaLetras)  # Imprime a tupla

print(type(tuplaLetras))  # Imprime o tipo da variável
print(len(tuplaLetras))  # Imprime o tamanho da tupla

print(tuplaLetras[1])  # Acessa o primeiro elemento (segundo índice) da tupla
print(tuplaLetras[-1])  # Acessa o último elemento da tupla

print("\n ----------------------------------- \n")

novaTupla = ("E", ) # Cria uma nova tupla com o valor "E"
print(novaTupla)

print(type(novaTupla))  # Imprime o tipo da variável (str, não tupla)

tuplaLetras += novaTupla  # Adiciona novaTupla à tuplaLetras

print("\n ----------------------------------- \n")

print(tuplaLetras)  # Imprime a tupla atualizada

print("\n ----------------------------------- \n")

tuplaNumeros = (1, 2, 3, 4, 5, 6, 7)
listaNumeros = list(tuplaNumeros)  # Converte a tupla em uma lista
listaNumeros.remove (4)  # Remove o número 4 da lista
listaNumeros = tuple(listaNumeros)  # Converte a lista de volta para tupla

print("\n")
print(listaNumeros)  # Imprime a lista atualizada

print("\n ----------------------------------- \n")

tuplaFrutas = ("Banana", "Abacaxi", "Laranja", "Maça")

for i in tuplaFrutas:
    print(i)  # Imprime cada fruta da tupla