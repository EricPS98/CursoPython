"""
Classes - São as espeficicações de um ou mais objetos
É um conjunto de objetos / regras

Objeto - É uma instância, um item da classe 
Exemplo explicativo: Se uma classe é uma casa, os objetos são os móveis de dentro dela
"""

class minhaPrimeiraClasse:
    idade = 30 # Propriedade / Objeto
    nome = "João" # Propriedade / Objeto

pegaIdade = minhaPrimeiraClasse()

print("Nome:",pegaIdade.nome, "- Idade:", pegaIdade.idade)

print("\n ------------------------------------------------- \n")

class Aluno:
    #Propriedade / Objeto
    nome = ""
    idade = 0
    altura = 0

#Instanciando o objeto da classe
dados = Aluno()

dados.nome = "Cintia"
dados.idade = 21
dados.altura = 1.69

print("Estudante:", dados.nome)
print("Idade:", dados.idade)
print("Altura:", dados.altura)

print("\n ------------------------------------------------- \n")

class Turma:
    #def é um construtor - método construtor
    # O método __init__ é um construtor que inicializa os atributos da classe. Ele recebe três parâmetros que são usados para definir as propriedades do objeto.
    # self é uma palavra-parâmetro especial do python que referencia métodos e atributos dentro da própria classe, só é usado dentro da classe
    #Sempre que você usa o self dentro de uma classe você esta referenciando aquele atributo (variável) que a classe esta criando no momento com o método __init__

    #Método para construir
    def __init__(self, nomeAluno, idadeAluno, alturaAluno):
        self.nome  = nomeAluno # O "nome" da esquerda é da classe Turma, o "nomeAluno" da direita vem da classe construtora
        self.idade = idadeAluno
        self.altura = alturaAluno

    #Método para imprimir
    #Da pra acessar o "self" entro de outros métodos construtores porque fazem parta de classe "Turma"
    def imprimir(self):
        print("Estudante:", self.nome)
        print("Idade:", self.idade)
        print("Altura:", self.altura)
        print("---------------------")

#Criando instâncias do objeto da classe 
aluno1 = Turma("Pedro", 31, 1.72)
aluno2 = Turma("Roseli", 21, 1.65)
aluno3 = Turma("Alberto", 25, 1.89)

#Executando os métodos da classe (só é possível após ter instanciado primeiro)
aluno1.imprimir()
aluno2.imprimir()
aluno3.imprimir()
