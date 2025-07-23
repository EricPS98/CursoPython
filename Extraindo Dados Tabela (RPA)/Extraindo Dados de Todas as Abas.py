from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By #Importando a Classe By, que é usada para localizar elementos HTML dentro da página
import time as tempoEspera

#----- Imports e configuração para desabiliar os logs e deixar o terminal mais limpo ---------#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Silencia logs
#---------------------------------------------------------

# Abrir o Chrome
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome comopções de desabilitar os logs

# Abrindo o site do rpachallengerocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

linha = 1

i = 1

while i < 4:

    # No site, clique com o botão direito do mouse e vá em "Inspecionar" (ou aperta F12),
    # encontre no codigo html a tag de abertura da tabela "<table id =...", clique com o botão direito e em Copy,
    # clique em Copy XPATH para obter o valor (no caso o obtido foi: //*[@id="tableSandbox"] )
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    #Ainda em inspecionar, abra a tag "table" a dentro dela, pegue a tag identificador das linhas da tabela, no caso é todo 'tr'
    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')

    #Ainda em inspecionar, abra qualquer tag "tr" (linha) e pegue agora o identificador das colunas, no caso é o 'td'
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

    #Passando por todas as linhas
    for linhaHTML in linhas: #linhaHTML = Linha Atual
        print(linhaHTML.text)

        linha += 1

    i += 1

    # Aguarde 1 segundo para o computador processar as informações
    tempoEspera.sleep(1)

    # No site, clique com o botão direito do mouse em cima do botão 'Next' do navegador de páginas, vá em "Inspecionar" (ou aperta F12),
    # Na opção de encontrar elemento pelo mouse, clique novamente no botão 'Next' para encontra no codigo html a tag do botão, clique com o botão direito e em Copy,
    # clique em Copy XPATH para obter o valor (no caso o obtido foi: //*[@id="tableSandbox_next"]' )
    # Poderia ter sido obtido tambem pelo ID (By.ID), no caso, fomos pelo XPATH
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click() # Vai clicar no 'Next' e ir pra próxima página

    # Aguarde 1 segundo para o computador processar as informações
    tempoEspera.sleep(1)

else:

    print("Dados extraidos com sucesso!")

