listaNomes = ["Bia", "Raquel", "Allan", "Mafalda"]

for i in listaNomes:
    if i == "Allan":
        #print("Nome encontrado com sucesso!")
        #break  # pause/ pare / interrompa
        continue # continue pula para a próxima iteração do loop
    print(i)

    #-----------------------------------------

print("\n")
#Contando de 0 até 10
for i in range(11):
        print(i)

print("\n")

#range(start, stop, step )
#range (start, 1, stop = 10, step == 1)

#Contar de 1 até 10 pulando de 2 em 2
for i in range(1, 11, 2):
    print("Número: ", i)

print("\n")

#Contar do 20 até o 10
for i in range(20, 9, -2): #Para chegar até o 10, o stop deve ser 9 porque a contagem começa no 0, portanto a posição 9 é = 10
    print("Posição: ", i)    
