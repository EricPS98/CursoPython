from dadosPessoais import Dados

pessoa1 = Dados("Celso", 34, "Solteiro", 5000)
pessoa2 = Dados("Aline", 41, "Solteira", 8000)

Dados.imprimirDados(pessoa1)
Dados.imprimirDados(pessoa2)

print("\n --------------------------------------------------- \n")

#Alterar os dados da pessoa1

pessoa1.nome = "Sebastian"
pessoa1.idade = 45
pessoa1.estadoCivil = "Casado"
pessoa1.salario = 10000

Dados.imprimirDados(pessoa1)

print("\n --------------------------------------------------- \n")

#Alterando os dados em tempo real
pessoa2.nome = input("Digite seu nome: ")
pessoa2.idade = int(input("Digite sua idade: "))
pessoa2.estadoCivil = input("Digite seu Estado Civil: ")
pessoa2.salario = float(input("Digite seu salario: "))


Dados.imprimirDados(pessoa2)