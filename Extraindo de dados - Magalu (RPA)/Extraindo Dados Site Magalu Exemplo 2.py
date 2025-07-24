from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By  #Importando a Classe By, que é usada para localizar elementos HTML dentro da página

#Importando o Pyautogui que controla mouse e teclado para automatizar interações com outras aplicações
import pyautogui as tempoEspera # Vai ser usado para o computador espera antes da próxima interação
import pyautogui as funcoesTeclado # Vai se usado para controlar o teclado

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

# Procura a lista de itens pelo nome da classe (CLASS_NAME) 
# No site, clique com o botão direito do mouse e vá em "Inspecionar" (ou aperta F12),
# encontre no codigo html o item de geladeira (no modo de encontrar pelo o mouse, passe o mouse e clique na imagem da primeira geladeira) 
# para pegar o nome da classe de cada item da lista gerada, desça um pouco o codigo e  onde tiver a lista <li>,
# copie o nome da classe, no caso é uma classe com 2 nomes (class="sc-kaaGRQ jVLgjd"), aqui vamos usar só o nome 'jVLgjd'
# Como cada item da lista tem o mesmo nome e vamos pegar todos, é usado "find_elements" com "s"
listaProdutos = navegador.find_elements(By.CLASS_NAME, 'jVLgjd') 

for i in listaProdutos: #i = item
    nomeProduto = ""
    precoOriginal = "" 
    precoParcelado = ""
    precoPix = ""
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

    if precoOriginal == "":

            try:
                #Será usado a classe porque é o identificador que o item possui no site para podermos usar aqui
                #Ainda com o site aberto e a aba de desenvolvedor aberta, e ainda no modo de encontrar elementos pelo mouse,
                #clique no preço do primeiro item para ser direcionado para o item no codigo e copie o nome da classe
                #no caso é uma classe com 4 nomes (class="sc-dcJsrY lmAmKF sc-cezyBN fATncB"), aqui vamos usar só o nome 'PdLos'

                precoOriginal = i.find_element(By.CLASS_NAME, "fATncB").text
            except Exception:
                pass

    elif precoOriginal == "":

            try:
                #Se os dados não estiverem no primeiro nome da classe, podem estar no segundo (usado aqui)
                precoOriginal = i.find_element(By.CLASS_NAME, "sc-cezyBN").text
            except Exception:
                pass
    elif precoOriginal == "":

            try:
                #Se os dados não estiverem no primeiro e segundo nome da classe, podem estar no terceiro (usado aqui)
                precoOriginal = i.find_element(By.CLASS_NAME, "lmAmKF").text
            except Exception:
                pass
    elif precoOriginal == "":

            try:
                #Se os dados não estiverem no primeiro, segundo ou terceiro nome da classe, podem estar no ultimo (usado aqui)
                precoOriginal = i.find_element(By.CLASS_NAME, "sc-dcJsrY").text
            except Exception:
                pass
    else: 
         precoOriginal = "0"

   #---------------------------------------------------------------------------------------------------------------------------- 

    if precoParcelado == "":

            try:
                #Será usado a classe porque é o identificador que o item possui no site para podermos usar aqui
                #Ainda com o site aberto e a aba de desenvolvedor aberta, e ainda no modo de encontrar elementos pelo mouse,
                #clique no preço do primeiro item para ser direcionado para o item no codigo e copie o nome da classe
                #no caso é uma classe com 4 nomes (class="sc-dcJsrY dpUJi sc-bkEOxz cVhpkc"), aqui vamos usar só o nome 'PdLos'

                precoParcelado = i.find_element(By.CLASS_NAME, "cVhpkc").text
            except Exception:
                pass

    elif precoParcelado == "":

            try:
                #Se os dados não estiverem no primeiro nome da classe, podem estar no segundo (usado aqui)
                precoParcelado = i.find_element(By.CLASS_NAME, "sc-bkEOxz").text
            except Exception:
                pass
    elif precoParcelado == "":

            try:
                #Se os dados não estiverem no primeiro e segundo nome da classe, podem estar no terceiro (usado aqui)
                precoParcelado = i.find_element(By.CLASS_NAME, "dpUJi").text
            except Exception:
                pass
    elif precoParcelado == "":

            try:
                #Se os dados não estiverem no primeiro, segundo ou terceiro nome da classe, podem estar no ultimo (usado aqui)
                precoParcelado = i.find_element(By.CLASS_NAME, "sc-dcJsrY").text
            except Exception:
                pass
    else: 
         precoParcelado = "0"

   #---------------------------------------------------------------------------------------------------------------------------- 

    if precoPix == "":

            try:
                #Será usado a classe porque é o identificador que o item possui no site para podermos usar aqui
                #Ainda com o site aberto e a aba de desenvolvedor aberta, e ainda no modo de encontrar elementos pelo mouse,
                #clique no preço do primeiro item para ser direcionado para o item no codigo e copie o nome da classe
                #no caso é uma classe com 4 nomes (class="sc-dcJsrY eLxcFM sc-cXPBUD hAtJoE"), aqui vamos usar só o nome 'PdLos'

                precoPix = i.find_element(By.CLASS_NAME, "hAtJoE").text
            except Exception:
                pass

    elif precoPix == "":

            try:
                #Se os dados não estiverem no primeiro nome da classe, podem estar no segundo (usado aqui)
                precoPix = i.find_element(By.CLASS_NAME, "sc-cXPBUD").text
            except Exception:
                pass
    elif precoPix == "":

            try:
                #Se os dados não estiverem no primeiro e segundo nome da classe, podem estar no terceiro (usado aqui)
                precoPix = i.find_element(By.CLASS_NAME, "eLxcFM").text
            except Exception:
                pass
    elif precoPix == "":

            try:
                #Se os dados não estiverem no primeiro, segundo ou terceiro nome da classe, podem estar no ultimo (usado aqui)
                precoPix = i.find_element(By.CLASS_NAME, "sc-dcJsrY").text
            except Exception:
                pass
    else: 
         precoPix = "0"

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

    print('\n ------------------------------------------------------------------------ \n')
    print('Produto:', nomeProduto)
    print('Preço Original:', precoOriginal)
    print('Preço Parcelado com desconto:', precoParcelado)
    print('Preço no Pix com desconto:', precoPix)
    print('Link:', urlProduto)

input("Pressione Enter para fechar...")
