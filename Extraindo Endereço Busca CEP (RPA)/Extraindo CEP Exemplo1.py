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

# Espera até que o elemento "barra de pesquisa" encontrado pelo "name" da tag da pesquisa (<input...) no codigo fonte do site (no caso é "endereco") ser carregado, e atribui a variavel
elemento_Pesquisacep = espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "endereco")))

#Digita o cep na barra de pesquisa encontrada
elemento_Pesquisacep.send_keys("05894360")

# Espera até que o elemento "botão" encontrado pelo "name" da tag do botão (<button...) no codigo fonte do site (no caso é "btn_pesquisar") ser carregado, e atribui a variavel
botaoPesquisa = espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "btn_pesquisar")))

#Esperar o CAPTCHA do site ser resolvido manualmente e ter digitado "ENTER" no terminal antes de seguir com a automação
input("Por favor, digite o CAPTCHA no navegador e pressione Enter aqui para continuar.")

#Clica no botão
botaoPesquisa.click() 

# Espera até que o texto "Logradouro/Nome" encontrado pelo "XPath" (clique com o botão direito e em Copy, clique em Copy XPath) da tag do texto (<td...)
#  no codigo fonte do site (no caso é "//*[@id="resultado-DNEC"]/tbody/tr/td[1]") ser carregado, e atribui a variavel
rua = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]'))).text

# Espera até que o texto "Bairro/Distrito" encontrado pelo "XPath" (clique com o botão direito e em Copy, clique em Copy XPath) da tag do texto (<td...)
#  no codigo fonte do site (no caso é "//*[@id="resultado-DNEC"]/tbody/tr/td[2]") ser carregado, e atribui a variavel
bairro = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]'))).text

# Espera até que o texto "Localidade/UF" encontrado pelo "XPath" (clique com o botão direito e em Copy, clique em Copy XPath) da tag do texto (<td...)
#  no codigo fonte do site (no caso é "//*[@id="resultado-DNEC"]/tbody/tr/td[3]") ser carregado, e atribui a variavel
cidade = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]'))).text

# Espera até que o texto "CEP" encontrado pelo "XPath" (clique com o botão direito e em Copy, clique em Copy XPath) da tag do texto (<td...)
#  no codigo fonte do site (no caso é "//*[@id="resultado-DNEC"]/tbody/tr/td[4]") ser carregado, e atribui a variavel
cep = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]'))).text

#Imprimindo informações obtidas
print('\n --------------------------------------------- \n')
print('Rua:', rua)
print('Bairro:', bairro)
print('Cidade:', cidade)
print('CEP:', cep)
print('\n --------------------------------------------- \n')

#Impedir o programa finalize e feche o navegador
input("Pressione Enter para finalizar.")