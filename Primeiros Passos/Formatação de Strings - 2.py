palavraComEspaco = "         Curso de Python          "

print(palavraComEspaco)
print(palavraComEspaco.strip()) #Remove os espaços


#-------------------------------------------------------------------------------------------

gostoPorFrutas = "Eu gosto de Laranja"
print("Laranja" in gostoPorFrutas) #Verifica se existe a palavra na string e retorna boolean (True or False)
print("Maçã" in gostoPorFrutas)

resultadoProcura = gostoPorFrutas.find("o") #Procura o caractere especificado na string e retorna a posição do primeiro encontrado
print(resultadoProcura)

#-------------------------------------------------------------------------------------------

copa = "Brasil ganhou a copa do mundo"
#campeao = "Alemanha" not in copa #Verifica se não existe a palavra na string e retorna boolean (True or False)
campeao = "Brasil" not in copa #Verifica se não existe a palavra na string e retorna boolean (True or False)

print(campeao)


#-------------------------------------------------------------------------------------------

aluno = "Rebeca Martins"
nota1 = 9.523
nota2 = 6.2
media = (nota1 + nota2) / 2

print("Aluna: " + aluno + " - Média: " + str(media)) # Concatenar string

print(f"Aluna: {aluno} - Média: {media:.2f}") #Outra forma de concatenação (o "f" permite adicionar as variáveis dentro da string dentro de chaves)
                                              #":.2f" limita a quantidade de decimais após o número inteiro, nesse caso em 2
ajusteTexto = "Aluna: {} - Média: {:.2f}"   #Outra forma de fazer (":.2f" limita a quantidade de decimais após o número inteiro, nesse caso em 2)
print(ajusteTexto.format(aluno, media)) #O format entende as chaves (placeholder) como campos a serem substituidos pelos argumentos que você insere na função


