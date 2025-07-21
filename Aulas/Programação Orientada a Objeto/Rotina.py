class Rotina:
    def __init__(self, nome, dormindo = False, dirigindo = False):
        self.nome = nome
        self.dormindo = dormindo
        self.dirigindo = dirigindo

    def dormir(self):

        if self.dirigindo: #Não é necessário colocar "= True" pois só de deixar a estrutura "if self.dirigindo:", a linguagem ja entende que é True
            print(self.nome + " não pode dormir enquanto dirige")
            print("---------------------------------")
            return
        
        if self.dormindo:
            print(self.nome + " já está dormindo")
            print("---------------------------------")
            return

        print("O " + self.nome + " está dormindo")
        print("---------------------------------")
        self.dormindo = True

    def acordar(self):

        if not self.dormindo:
            print(self.nome + " já está acordado")
            print("---------------------------------")
            return

        print("O " + self.nome + " acordou")
        print("---------------------------------")
        self.dormindo = False

    def dirigir(self):

        if self.dormindo:
            print(self.nome + " não pode dirigir enquanto está dormindo")
            print("---------------------------------")
            return

        if self.dirigindo:
            print("O " + self.nome + "Já está dirigindo")
            print("---------------------------------")
            return

        print("O " + self.nome + " está dirigindo")
        print("---------------------------------")
        self.dirigindo = True
        
    def pararDeDirigir(self):

        if not self.dirigindo:
            print(self.nome + " Já parou de dirigir")
            print("---------------------------------")
            return

        print("O " + self.nome + " parou de dirigir")
        print("---------------------------------")
        self.dirigindo = False