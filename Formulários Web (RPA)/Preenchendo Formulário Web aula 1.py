from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

#import pyautogui as tempoEspera  # Vai ser usado para o computador esperar antes da próxima interação -> (Usado na aula, mas aqui será usado uma opção melhor abaixo ↓)
#----- ADIÇÃO EXTRA MINHA: importação de uma opção melhor para aguardar condições específicas para esperar, ao invés de um tempo pré definido de espera como "pyautogui.sleep(5)"
from selenium.webdriver.support.ui import WebDriverWait as esperaEvento
#Documentação para usar o "expected_conditions" corretamente: https://medium.com/@lflucasferreira/entendendo-os-tipos-de-espera-no-selenium-webdriver-2b7adda4db59
from selenium.webdriver.support import expected_conditions as condicaoEspera

from selenium.webdriver.support.select import Select  # Importa a função Select para selecionar opções em dropdowns (caixas de seleção)

#----- ADIÇÂO EXTRA MINHA: Imports e configuração para desabiliar os logs e deixar o terminal mais limpo ---------#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Silencia logs
#-------------------------------------------------------------------------------------------------------------------------------#

# Abrir o Chrome - COM ADIÇÃO EXTRA MINHA PARA DESABILITAR OS LOGS E DEIXAR O TERMINAL MAIS LIMPO
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome com opções de desabilitar os logs

#Abrindo o site do formulário
navegador.get("https://form.jotform.com/221436066464051")

# Define o tempo para o computador processar as informações 
espera = esperaEvento(navegador, 10) # 10 é o tempo máximo de espera (segundos) até que um elemento esteja presente ou atenda a uma condição (como estar visível ou clicável).
                                     # Se não aparecer até os 10 segundos, ele lança uma exceção (TimeoutException).

# Espera até que o elemento "input(Nome)" encontrado pelo "name" da tag da pesquisa no codigo fonte do site (no caso é "q3_nome[first]") ser carregado e escreve o nome "Eric"
espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "q3_nome[first]"))).send_keys("Eric")  

# Espera até que o elemento "input(Sobrenome)" encontrado pelo "name" da tag da pesquisa no codigo fonte do site (no caso é "q3_nome[last]") ser carregado e escreve o nome "Palmeira"
espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "q3_nome[last]"))).send_keys("Palmeira")  

# Espera até que o elemento "input(E-mail)" encontrado pelo "name" da tag da pesquisa no codigo fonte do site (no caso é "q4_email") ser carregado e escreve o nome "emailficticio@email.com.br"
espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "q4_email"))).send_keys("emailficticio@email.com.br") 

# Espera até que o elemento "form(Estado Civil)" encontrado pelo "ID" da tag da pesquisa no codigo fonte do site (no caso é "input_5") ser carregado 
pegaDropDown = espera.until(condicaoEspera.visibility_of_element_located((By.ID, "input_5")))
itemSelecionado = Select(pegaDropDown)  # Cria um objeto Select para interagir com o dropdown
itemSelecionado.select_by_visible_text("Solteiro(a)")  # Seleciona a opção "Solteiro" no dropdown pelo texto visível

filho = "Não"

if filho == "Sim":
    # Espera o elemento ser carregado e clica na opção "Sim"
    elementoFilhos = espera.until(condicaoEspera.element_to_be_clickable ((By.ID, "label_input_6_0")))
    #Rola a página para baixo até encontrar o elemento, garantindo que o click não vá para outro elemento e gere erros
    navegador.execute_script("arguments[0].scrollIntoView();", elementoFilhos) 
    elementoFilhos.click()
else:
    # Espera o elemento ser carregado e clica na opção "Sim"
    elementoFilhos = espera.until(condicaoEspera.element_to_be_clickable ((By.ID, "label_input_6_1")))
    #Rola a página para baixo até encontrar o elemento, garantindo que o click não vá para outro elemento e gere erros de bloqueio visual
    navegador.execute_script("arguments[0].scrollIntoView();", elementoFilhos) 
    elementoFilhos.click()

    #Espera o elemento ser carregado e clica na cor "Preto"
espera.until(condicaoEspera.element_to_be_clickable ((By.ID, "label_input_7_4"))).click()
    #Espera o elemento ser carregado e clica na cor "Azul"
espera.until(condicaoEspera.element_to_be_clickable ((By.ID, "label_input_7_0"))).click()

# Avaliando o site com 4 estrelas
    #Espera o elemento  das estrelas ser carregado e clica na avaliação de 4 estrelas pelo XPATH porque ele não possui um "name" nem um "ID", 
    # e a classe possui muitos nomes, teria que criar um código mais complexo só para tratar a classe e encontrar a estrela correta 
espera.until(condicaoEspera.element_to_be_clickable ((By.XPATH, '//*[@id="input_8"]/div[4]'))).click()




input('Digite Enter para encerrar o programa e fechar o navegador...')  # Espera o usuário digitar Enter para encerrar o programa e fechar o navegador