from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By  # Importa o By para localizar elementos na página
from selenium.webdriver.support.select import Select  # Importa a função Select para selecionar opções em dropdowns (caixas de seleção)

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
#-------------------------------------------------------------------------------------------------------------------------------#

# Abrir o Chrome - COM ADIÇÃO EXTRA MINHA PARA DESABILITAR OS LOGS E DEIXAR O TERMINAL MAIS LIMPO
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome com opções de desabilitar os logs

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")  # Abrindo o site do formulário

# Define o tempo para o computador processar as informações 
espera = esperaEvento(navegador, 10) # 10 é o tempo máximo de espera (segundos) até que um elemento esteja presente ou atenda a uma condição (como estar visível ou clicável).
                                     # Se não aparecer até os 10 segundos, ele lança uma exceção (TimeoutException).

# Espera até que o elemento "input(Nome)" encontrado pelo "name" da tag da pesquisa no codigo fonte do site ser carregado e escreve o nome
espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "72542598"))).send_keys("Eric Palmeira")  # Espera até que o elemento com ID "q1" esteja visível

# Espera até que o elemento "input(Email)" encontrado pelo "name" da tag da pesquisa no codigo fonte do site ser carregado e escreve o email
espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "72542821"))).send_keys("emailficticio@email.com.br")  # Espera até que o elemento com ID "q1" esteja visível

sexo = "Masculino"

if sexo == "Masculino":
    # Espera o elemento ser carregado e clica na opção "Masculino"
    elementoSexo = espera.until(condicaoEspera.element_to_be_clickable ((By.ID, "583517054")))
    #Rola a página para baixo até encontrar o elemento, garantindo que o click não vá para outro elemento e gere erros
    navegador.execute_script("arguments[0].scrollIntoView();", elementoSexo) 
    elementoSexo.click()
else:
    # Espera o elemento ser carregado e clica na opção "Feminino"
    elementoSexo = espera.until(condicaoEspera.element_to_be_clickable ((By.ID, "583517055")))
    #Rola a página para baixo até encontrar o elemento, garantindo que o click não vá para outro elemento e gere erros de bloqueio visual
    navegador.execute_script("arguments[0].scrollIntoView();", elementoSexo) 
    elementoSexo.click()


# Espera o elemento "<select(Qual sua cor favorita?)" ser carregado e clica na opção "Cinza"
# Como o elemento de dropdown possui várias classes, é mais seguro usar o XPATH para localizá-lo
pegaDropDown = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="question-field-72543178"]/div/fieldset/div/select'))) 
itemSelecionado = Select(pegaDropDown)  # Cria um objeto Select para interagir com o dropdown
itemSelecionado.select_by_index(4)  # Seleciona a opção "Cinza" no dropdown pelo índice (0 é a primeira opção, 1 é a segunda, etc.)

#Clica no botão "Concluído"
# Como o elemento de botão possui várias classes, é mais seguro usar o XPATH para localizá-lo
# Esta comentado para não enviar porque é um formulário de teste, e possui um limite de envios, como a aula possui varios alunos, vai dar erro de limite de envios se todos enviarem
# espera.until(condicaoEspera.element_to_be_clickable ((By.XPATH, '//*[@id="view-pageNavigation"]/div/button'))).click()  

input('Digite Enter para encerrar o programa e fechar o navegador...')  # Espera o usuário digitar Enter para encerrar o programa e fechar o navegador