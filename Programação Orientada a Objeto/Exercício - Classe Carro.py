class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometragem = 0
    
    def drive(self):
        print("**Digirindo**")
        self.kilometragem = self.kilometragem + 1000

    def descricao(self):
        print("------------------------------------")
        print("Descrição do veículo: ")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Kilometragem:", self.kilometragem, "Km's rodados")
        print("------------------------------------")

carro1 = Carro("Toyota", "Corolla", 2022)

Carro.descricao(carro1)
Carro.drive(carro1)
Carro.drive(carro1)
Carro.drive(carro1)
Carro.drive(carro1)
Carro.drive(carro1)
Carro.descricao(carro1)