from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By #Importando a Classe By, que é usada para localizar elementos HTML dentro da página

#import pyautogui as tempoEspera  # Vai ser usado para o computador esperar antes da próxima interação -> (Usado na aula, mas aqui será usado uma opção melhor abaixo ↓)
#----- ADIÇÃO EXTRA MINHA: importação de uma opção melhor para aguardar condições específicas para esperar, ao invés de um tempo pré definido de espera como "pyautogui.sleep(5)"
from selenium.webdriver.support.ui import WebDriverWait as esperaEvento
#Documentação para usar o "expected_conditions" corretamente: https://medium.com/@lflucasferreira/entendendo-os-tipos-de-espera-no-selenium-webdriver-2b7adda4db59
from selenium.webdriver.support import expected_conditions as condicaoEspera

#----- ADIÇÂO EXTRA MINHA: Imports e configuração para desabiliar os logs e deixar o terminal mais limpo ---------#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Silencia logs
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Abrir o Chrome - COM ADIÇÃO EXTRA MINHA PARA DESABILITAR OS LOGS E DEIXAR O TERMINAL MAIS LIMPO
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome com opções de desabilitar os logs

#Preparando o site para acesso
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

# Define o tempo para o computador processar as informações 
espera = esperaEvento(navegador, 10) # 10 é o tempo máximo de espera (segundos) até que um elemento esteja presente ou atenda a uma condição (como estar visível ou clicável).
                                     # Se não aparecer até os 10 segundos, ele lança uma exceção (TimeoutException).

# Espera até que o elemento " barra de pesquisa" encontrado pelo "name" da tag da pesquisa (<input...) no codigo fonte do site (no caso é "endereco") ser carregado, e atribui a variavel
elemento_Pesquisacep = espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "endereco")))

#Digita o cep na barra de pesquisa encontrada
elemento_Pesquisacep.send_keys("05894360")

# Espera até que o elemento "botão" encontrado pelo "name" da tag da pesquisa (<button...) no codigo fonte do site (no caso é "btn_pesquisar") ser carregado, e atribui a variavel
botaoPesquisa = espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "btn_pesquisar")))

#Esperar o CAPTCHA do site ser resolvido manualmente e ter digitado "ENTER" no terminal antes de seguir com a automação
input("Por favor, digite o CAPTCHA no navegador e pressione Enter aqui para continuar.")

#Clica no botão
botaoPesquisa.click() 

# Espera até que o elemento "tabela" encontrado pelo "XPath" (clique com o botão direito e em Copy, clique em Copy XPath) da tag da tabela (<table...)
#  no codigo fonte do site (no caso é "//*[@id="resultado-DNEC"]") ser carregado, e atribui a variavel
#OBS. Para descobrir o elemento necessário é na tentativa e erro, poderia ser no (<tbody... ou <tr...) que recebem as linhas e colunas tambem,
#  no caso funcionou pegando direto da tabela inteira (<table...)
elementoTabela = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]')))

# Percorrendo as linhas dentro da tabela (encontradas pelo nome da tag "tr") no codigo fonte dentro da tag da tabela (<table...)
for i in elementoTabela.find_elements(By.TAG_NAME, "tr"):  # i = linhaTabela
    endereco = ""

    # Percorrendo as colunas dentro da linha (encontradas pelo nome da tag "td") no codigo fonte dentro da tag da linha (<tr...)
    for j in i.find_elements(By.TAG_NAME, "td"): # j = colunaTabela

        endereco = endereco + ";" + j.text


#Imprimindo informações obtidas
print('\n --------------------------------------------- \n')
print('Endereço:', endereco)
print('\n --------------------------------------------- \n')

#Impedir o programa finalize e feche o navegador
input("Pressione Enter para finalizar.")