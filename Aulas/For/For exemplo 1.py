listaLetras = ["A", "B", "C", "D", "E"]

#for = para
for posicao in listaLetras:
    print("Letra: ", posicao)

print("\n")

for posicaoLetra, Letra in enumerate(listaLetras):
    print("Posição:", posicaoLetra, " - Letra:", Letra)

print("\n")

for i in "Curso de Lógica de Programação Python:":
    print("Letra: ", i)  

print("\n")

listaCores = ["Amarelo", "Vermelho", "Laranja", "Rosa"]

for posicao, i in enumerate(listaCores):
    if i == "Laranja":
        print("Cor Laranja encontrada com sucesso na posição:", posicao+1)  # +1 para mostrar a posição correta, já que o índice começa em 0
        break # pause/ pare / interrompa 