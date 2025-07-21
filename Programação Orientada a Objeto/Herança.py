
class alunoEscolaPai:
    #Construtor
    def __init__(self, nome, sexo, media, situacao):
        self.nome = nome
        self.sexo = sexo
        self.media = media
        self.situacao = situacao

    def imprimirDados(self):
        print("Estudante:", self.nome)
        print("Sexo:", self.sexo)
        print("Média:", self.media)
        print("Situação:", self.situacao)
        print("---------------------------")

#Para herdar os dados, basta inserir o nome da classe que quer herdar os dados no parâmetro da classe que você quer que herde os objetos
class alunoEscolaFilho(alunoEscolaPai):
    #Quando crio um construtor na classe filho, esse construtor sobrescreve o da classe pai
    def __init__(self, nome, sexo, n1, n2, n3, n4):
        #É Possível usar a "media" que é um objeto da classe pai nessa classe, obtido através da herança
        self.media = (n1 + n2 + n3 + n4) / 4

        #Da mesma forma, é possível usar o objeto "situacao" da classe pai, através da herança
        if self.media >= 6:
            self.situacao = "Aprovado(a)"
        else:
            self.situacao = "Reprovado(a)"

        #Através da função "Super" chamamos o construtor da classe pai, podendo jogar pra lá os dados tratados da classe filho
        #O __init__ nesse caso é o construtor da classe pai
        super().__init__(nome, sexo, self.media, self.situacao)

class alunoEscolaFilho2(alunoEscolaPai):
    #Quando crio um construtor na classe filho, esse construtor sobrescreve o da classe pai
    def __init__(self, nome, sexo, n1, n2, n3, n4):
        #É Possível usar a "media" que é um objeto da classe pai nessa classe, obtido através da herança
        self.media = (n1 + n2 + n3 + n4) / 4

        #Da mesma forma, é possível usar o objeto "situacao" da classe pai, através da herança
        if self.media >= 6:
            self.situacao = "Aprovado(a)"
        else:
            self.situacao = "Reprovado(a)"

        #Através da função "Super" chamamos o construtor da classe pai, podendo jogar pra lá os dados tratados da classe filho
        #O __init__ nesse caso é o construtor da classe pai
        super().__init__(nome, sexo, self.media, self.situacao)
    
#Instanciando a classe filho
aluno1 = alunoEscolaFilho("Pedro", "M", 9, 8, 10, 10)
aluno2 = alunoEscolaFilho2("Mariza", "F", 6, 4, 5, 5)


#Usando método da classe pai com os dados tratados da classe filho
aluno1.imprimirDados()
aluno2.imprimirDados()