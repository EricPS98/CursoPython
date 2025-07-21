"""
Neste exercício, você vai criar uma função que calcula a média de uma lista de números.

1° Primeiro, defina uma função chamada calcula_media que recebe uma lista de números como argumento.

2° Dentro da função, use a função incorporada sum para somar todos os números da lista e a função len 
para obter a quantidade de números. Divida a soma pela quantidade para obter a média.

3° Retorne a média calculada.
"""

def calcula_media(numeros):
    return sum(numeros) / len(numeros)
    
listaNumeros = [10, 4, 7, 6]

print("Média dos numeros:", calcula_media(listaNumeros))

