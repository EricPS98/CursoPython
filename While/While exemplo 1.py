#while = enquanto

numero = 1
while numero <= 10:
    print(numero)
    numero += 1 #numero = numero + 1

#-------------------------------------------------
print("\n")
num = 1
while num <= 1000:
    print("Número: ", num)
    #Quando o número for 5, parar o loop
    if num == 5:
        break #Parar
    num += 1 #num = num + 1

#-------------------------------------------------
print("\n")

n = 0
while n < 10:
    n += 1 #n = n + 1
    #Pular o loop quando n for 6
    if n == 6:
        continue
    print("Número: ", n)
#-------------------------------------------------
print("\n")

contador = 0
while contador < 11:
    contador += 1 #contador = contador + 1
    print("Numero: ", contador)
else:
    print("Números impressos com sucesso!")