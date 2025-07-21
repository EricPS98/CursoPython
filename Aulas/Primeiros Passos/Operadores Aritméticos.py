"""
+ Adição / Soma
- Subtração / Diminui
* Multiplicação / Realiza multiplicação
/ Divisão / Divide
// Divisão inteira, realiza a divisão entra operandos e a parte decimal de ambos os operandos
% Módulo / Retorna o resto da divisão
** Exponenciação / Eleva um número em uma potência
"""

numero1 = 10
numero2 = 2

adição = numero1 + numero2
print("Resultado da Adição:", adição)
print("César" + " " + "Fonseca")

subtracao = numero1 - numero2
print("Resultado da Subtração:", subtracao)

multiplicacao = numero1 * numero2
print("Resultado da Multiplicação:", multiplicacao)
print(numero1 * "C")

divisao = numero1 / numero2
print("Resultado da Divisão:", divisao)

divisaoInteira = numero1 // numero2
print("Resultado da Divisão Inteira:", divisaoInteira)

#Retorna o resto em inteiro, se você tem 10 pra dividir pra 6, não é uma divisão exata, então divide um pra cada 6 e sobra 4
modulo = numero1 % numero2
print("Resultado do Módulo:", modulo)

#Eleva o primeiro valor ao segundo valor
exponenciacao = numero1 ** numero2
print("Resultado da Exponenciação:", exponenciacao)
