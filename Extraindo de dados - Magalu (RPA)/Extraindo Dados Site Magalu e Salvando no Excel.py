from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By  #Importando a Classe By, que é usada para localizar elementos HTML dentro da página

#Importando o Pyautogui que controla mouse e teclado para automatizar interações com outras aplicações
import pyautogui as tempoEspera # Vai ser usado para o computador espera antes da próxima interação
import pyautogui as funcoesTeclado # Vai se usado para controlar o teclado

import pandas as pd #Biblioteca para trabalhar com tabelas

import os # ADIÇÃO EXTRA MINHA: Módulo do Python que serve para interagir com o sistema operacional

#----- ADIÇÂO EXTRA MINHA: Imports e configuração para desabiliar os logs e deixar o terminal mais limpo ---------#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Silencia logs
#-------------------------------------------------------------------------------------------

# Abrir o Chrome - COM ADIÇÃO EXTRA MINHA PARA DESABILITAR OS LOGS E DEIXAR O TERMINAL MAIS LIMPO
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome com opções de desabilitar os logs

#Preparando o site
navegador.get('https://www.magazineluiza.com.br/')

# Procura o campo de pesquisa pelo ID e digita o nome do produto (geladeira) 
# No site, clique com o botão direito do mouse e vá em "Inspecionar" (ou aperta F12),
# encontre no codigo html o elemento da barra de pesquisa e copie o ID do elemento, no caso é o 'input-search'
navegador.find_element(By.ID, 'input-search').send_keys('geladeira') 

# Aguarda um tempo para o computador processar as informações
tempoEspera.sleep(2)

#Apertando a tecla do teclado 'Enter' para pesquisar o produto
funcoesTeclado.press('enter')

# Aguarda um tempo para o navegador carregar a lista
tempoEspera.sleep(5)

# Criando uma lista (dataframe) que vai receber os dados
listaDataFrame= []

# Procura a lista de itens pelo nome da classe (CLASS_NAME) 
# No site, clique com o botão direito do mouse e vá em "Inspecionar" (ou aperta F12),
# encontre no codigo html o item de geladeira (no modo de encontrar pelo o mouse, passe o mouse e clique na imagem da primeira geladeira) 
# para pegar o nome da classe de cada item da lista gerada, desça um pouco o codigo e  onde tiver a lista <li>,
# copie o nome da classe, no caso é uma classe com 2 nomes (class="sc-kaaGRQ jVLgjd"), aqui vamos usar só o nome 'jVLgjd'
# Como cada item da lista tem o mesmo nome e vamos pegar todos, é usado "find_elements" com "s"
listaProdutos = navegador.find_elements(By.CLASS_NAME, 'jVLgjd') 

for i in listaProdutos: #i = item
    nomeProduto = ""
    precoProduto = "" 
    urlProduto = ""

    if nomeProduto == "":

        try:
            #Será usado a classe porque é o identificador que o item possui no site para podermos usar aqui
            #Ainda com o site aberto e a aba de desenvolvedor aberta, e ainda no modo de encontrar elementos pelo mouse,
            #clique no titulo do primeiro item para ser direcionado para o item no codigo e copie o nome da classe
            #no caso é uma classe com 2 nomes (class="sc-hsUFQk PdLos"), aqui vamos usar só o nome 'PdLos'
            nomeProduto = i.find_element(By.CLASS_NAME, "PdLos").text
        except Exception:
            pass
    elif nomeProduto == "":

        try:
            #Será usado a classe porque é o identificador que o item possui no site para podermos usar aqui
            #Ainda com o site aberto e a aba de desenvolvedor aberta, e ainda no modo de encontrar elementos pelo mouse,
            #clique no titulo do primeiro item para ser direcionado para o item no codigo e copie o nome da classe
            #no caso é uma classe com 2 nomes (class="sc-hsUFQk PdLos"), aqui vamos usar só o nome 'sc-hsUFQk'
            nomeProduto = i.find_element(By.CLASS_NAME, "sc-hsUFQk").text #Se os dados não estiverem no primeiro nome da classe, vão estar no segundo (usado nessa linha)
        except Exception:
            pass

   #----------------------------------------------------------------------------------------------------------------------------

    if precoProduto == "":

            try:
                #Será usado a classe porque é o identificador que o item possui no site para podermos usar aqui
                #Ainda com o site aberto e a aba de desenvolvedor aberta, e ainda no modo de encontrar elementos pelo mouse,
                #clique no preço do primeiro item para ser direcionado para o item no codigo e copie o nome da classe
                #no caso é uma classe com 4 nomes (class="sc-dcJsrY lmAmKF sc-cezyBN fATncB"), aqui vamos usar só o nome 'PdLos'

                precoProduto = i.find_element(By.CLASS_NAME, "fATncB").text
            except Exception:
                pass

    elif precoProduto == "":

            try:
                #Se os dados não estiverem no primeiro nome da classe, podem estar no segundo (usado aqui)
                precoProduto = i.find_element(By.CLASS_NAME, "sc-cezyBN").text
            except Exception:
                pass
    elif precoProduto == "":

            try:
                #Se os dados não estiverem no primeiro e segundo nome da classe, podem estar no terceiro (usado aqui)
                precoProduto = i.find_element(By.CLASS_NAME, "lmAmKF").text
            except Exception:
                pass
    elif precoProduto == "":

            try:
                #Se os dados não estiverem no primeiro, segundo ou terceiro nome da classe, podem estar no ultimo (usado aqui)
                precoProduto = i.find_element(By.CLASS_NAME, "sc-dcJsrY").text
            except Exception:
                pass
    else: 
         precoProduto = "0"

   #---------------------------------------------------------------------------------------------------------------------------- 

    if urlProduto == "":

            try:
                #Será usado o TAG_NAME porque é o identificador que o item possui no site para podermos usar aqui 
                # (até tem classe depois do link, mas o professor tentou pela classe e não veio nada),
                #PORTANTO, QUANDO FOR PRA PEGAR DE UM OUTRO SITE, É NA TENTATIVA E ERRO ATÉ CONSEGUIR PEGAR O ELEMENTO QUE PRECISA
                #No caso foi um pouco acima do código, encontrado um "<a href=..." que esta abrangendo todo o primeiro elemento
                #Portanto o tag name do "<a href=..." é "a" e o atributo dessa tag é "href", a url no código está dentro dessa tag
                urlProduto = i.find_element(By.TAG_NAME, "a").get_attribute("href")
            except Exception:
                pass
    else:
        urlProduto = "-"

    print(nomeProduto, "-", precoProduto)
    print(urlProduto)

    #o ";" será o delimitador para poder tratar a linha para colunas no excel
    #Versão usada na aula (vinha tudo em uma linha) -> dadosLinha = nomeProduto + ";" + precoProduto + ";"+ urlProduto
    #Minha versão melhorada para já trazer cada dado em sua devida coluna ↓
    dadosLinha = [nomeProduto, precoProduto, urlProduto]

    #Populando o dataFrame com os dados do site
    listaDataFrame.append(dadosLinha)

# ADIÇÃO EXTRA MINHA: Cria variáveis de caminho para salvar o arquivo aonde eu quiser e não na pasta raíz do projeto
caminho_base = r'D:\Users\eric.psouza\Documents\Cursos\Curso Lógica de Programação (Python)\Extraindo de dados - Magalu (RPA)\Dados Extraidos'
nome_arquivo = 'Dados - SiteMagalu.xlsx'
caminho_completo = os.path.join(caminho_base, nome_arquivo) # 'os.path.join' junta partes de caminhos (independente do sistema operacional)

#Prepara o arquivo do excel que terá o nome 'Dados - SiteMagalu.xlsx' usando o 'xlsxwriter' como mecanismo
#ADIÇÂO EXTRA MINHA: ao inves de passar só o nome do arquivo, que faria ele salvar na pasta raíz do projeto, 
# passei o caminnho inteiro com o nome do arquivo para salvar onde eu quiser
arquivoExcel = pd.ExcelWriter(caminho_completo, engine='xlsxwriter')

#Cria um dataframe que recebe a lista que foi incrementada com as linhas obtidas do site, com o cabeçalho das colunas = 'Descrição;Preço;Url' (";" para tratar a linha para colunas no Excel)
#Versão usada na aula (vinha tudo em uma linha) -> dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preço;Url'])
#Minha versão melhorada para já trazer cada dado em sua devida coluna ↓
dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição', 'Preço', 'URL'])

#Escreve no excel o dataframe carregado com a lista, no formato da variavel 'arquivoExcel' e com o nome da planilha 'Dados Extraidos do Site'
dataFrame.to_excel(arquivoExcel, sheet_name='Dados Extraidos do Site', index=False) #index = True autorizaria adicionar uma coluna de índice a esquerda (0,1,2,3...)

# Fecha o arquivo
arquivoExcel.close()


#input("Pressione Enter para fechar...")
