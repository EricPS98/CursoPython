"""

Operador
and Operador (E)
or Operador (OU)
not Operador (NÃO)
"""

numero1 = 25
numero2 = 21
numero3 = 40

if numero1 > numero2 and numero3 > numero1:
    print("Ambas as condições são verdadeiras")

nome = "Matheus"
idade = 30

if nome == "Matheus" and idade > 18:
    print("Matheus é maior de idade")

#---------------------------------------

usuario = "Jorge"
senha = 123

if usuario == "Jorge" and senha == 123:
    print("usuário logado com sucesso")
else:
    print("Usuário ou senha inválidos")

#---------------------------------------

#or Operador (OU)

n1 = 10
n2 = 15
n3 = 20

if n1 > n2 or n1 > 5:
    print("Pelo menos uma das condições é VERDADEIRO")

fruta = "Laranja"

if fruta == "Maçã" or fruta == "Laranja":
    print("A fruta é Maçã ou Laranja")

#----------------------------------------

#Operador not (NÃO)

letra = ""

if not letra:
    print("Não foi encontrado nenhuma letra")

numeroTestado = 0

if not numeroTestado:
    print("O numero não pode ser 0 pois 0 é considerado um boleano do tipo FALSE")