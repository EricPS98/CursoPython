def funcaoDivisao(numero1, numero2):
    return numero1 / numero2

resultado = funcaoDivisao(10, 2)
print("Resultado da divisão: ", resultado)

print("\n --------------------------------------------------- \n")

def funcaoMedia(nota1, nota2, nota3, nota4):
    return(nota1 + nota2 + nota3 + nota4) / 4

media = funcaoMedia(10, 6, 8, 10)

print("Média das notas: ", media)

print("\n --------------------------------------------------- \n")

#Função com argumentos arbitrários, *args

def frutaPreferida(*args):
    print("Eu gosto de", args[0])
    print("Eu gosto de", args[1])
    print("Eu gosto de", args[2])
    print("Eu gosto de", args[3])

frutaPreferida("Banana", "Goiaba", "Laranja", "Kiwi")

print("\n --------------------------------------------------- \n")

def unirListas(*args):
    print(args)

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

unirListas(*lista1, *lista2)

print("\n --------------------------------------------------- \n")

#Se o número de argumentos da palavra-chave for desconhecido, adicionamos ** antes do parâmetro
def funcaoKwargs(**parametro):
    print("Eu moro em", parametro["cidade1"])
    print("Eu moro em", parametro["cidade2"])

funcaoKwargs(cidade1 = "São Paulo", cidade2 = "Rio de Janeiro")
