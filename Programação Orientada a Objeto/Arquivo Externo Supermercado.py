#Importando o arquivo externo "Supermercado" e interagindo com as propriedades dele
from os import sep
import Supermercado as sp

sp.SupermercadoDoPovo()

print("\n")

print("O arroz do supermercado custa:", sp.produtos["Macarrão"])

print("\n --------------------------------------------------- \n")

#Se quiser importar somente a variável "produtos" do arquivo "Supermercado" ao invés de importar tudo que tem nele
from Supermercado import produtos

print("O feijão do supermercado custa:", produtos["Feijão"])

print("\n --------------------------------------------------- \n")

#Imprimindo o nome de todos os produtos
for i in produtos:
    print(i)

#Imprimindo o preço de todos os produtos
for i in produtos:
    print(produtos[i])

print("\n --------------------------------------------------- \n")

#Imprimindo o nome e o preço dos produtos
for i, j in produtos.items():
    print(i, "-", j)

print("\n --------------------------------------------------- \n")

from Supermercado import departamento

#O primeiro "for" vai percorrer pela primeira camada (chaves {}) do dicionário
for i, j in departamento.items():
    print(i)
    #O segundo "for" vai percorrer pela segunda camasa (chaves {}) do dicionario, dentro da primeira camada
    for i, j in j.items():
        print("Produto:", i, "R$", j)