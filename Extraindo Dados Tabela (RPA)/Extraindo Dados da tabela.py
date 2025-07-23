from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By #Importando a Classe By, que é usada para localizar elementos HTML dentro da página

# Abrir o Chrome
navegador = opcoesSelenium.Chrome()

# Abrindo o site do rpachallengerocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

# No site, clique com o botão direito do mouse e vá em "Inspecionar" (ou aperta F12),
# encontre no codigo html a tag de abertura da tabela "<table id =...", clique com o botão direito e em Copy,
# clique em Copy XPATH para obter o valor (no caso o obtido foi: //*[@id="tableSandbox"] )
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#Ainda em inspecionar, abra a tag "table" a dentro dela, pegue a tag identificador das linhas da tabela, no caso é todo 'tr'
linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')

#Ainda em inspecionar, abra qualquer tag "tr" (linha) e pegue agora o identificador das colunas, no caso é o 'td'
colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

#↑ Da forma feita acima, será verificado em todas as linhas e todas as colunas da tabela ↑

linha = 1

for i in linhas: #i = linha atual
    print(i.text)

    linha +=  1 #Incrementa a variável "linha" em 1