from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By #Importando a Classe By, que é usada para localizar elementos HTML dentro da página

#import pyautogui as tempoEspera  # Vai ser usado para o computador esperar antes da próxima interação -> (Usado na aula, mas aqui será usado uma opção melhor abaixo ↓)
#----- ADIÇÃO EXTRA MINHA: importação de uma opção melhor para aguardar condições específicas para esperar, ao invés de um tempo pré definido de espera como "pyautogui.sleep(5)"
from selenium.webdriver.support.ui import WebDriverWait as esperaEvento
#Documentação para usar o "expected_conditions" corretamente: https://medium.com/@lflucasferreira/entendendo-os-tipos-de-espera-no-selenium-webdriver-2b7adda4db59
from selenium.webdriver.support import expected_conditions as condicaoEspera

import time

#----- ADIÇÂO EXTRA MINHA: Imports e configuração para desabiliar os logs e deixar o terminal mais limpo ---------#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Silencia logs
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Abrir o Chrome - COM ADIÇÃO EXTRA MINHA PARA DESABILITAR OS LOGS E DEIXAR O TERMINAL MAIS LIMPO
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome com opções de desabilitar os logs

# Define o tempo para o computador processar as informações 
espera = esperaEvento(navegador, 10) # 10 é o tempo máximo de espera (segundos) até que um elemento esteja presente ou atenda a uma condição (como estar visível ou clicável).
                                     # Se não aparecer até os 10 segundos, ele lança uma exceção (TimeoutException).

#Preparando o site para acesso
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

#Dicionário
dicionarioCEPS = {
    "CEP 1": "05894360",
    "CEP 2": "05340000",
    "CEP 3": "01153000"
}

# Espera até que o elemento " barra de pesquisa" encontrado pelo "name" da tag da pesquisa (<input...) no codigo fonte do site (no caso é "endereco") ser carregado, limpa e digita o cep
elemento_Pesquisacep = espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "endereco")))
elemento_Pesquisacep.clear()
elemento_Pesquisacep.send_keys("05894360") # Digita ou cep qualquer na barra de pesquisa encontrada só para chegar até a tela onde será iniciado o loop

#-------ADAPTACÃO EXTRA MINHA: Loop de verificação feito exclusivamente para tratar o captcha---------------------
while True:
    #Esperar o CAPTCHA do site ser resolvido manualmente e ter digitado "ENTER" no terminal antes de seguir com a automação
    input("Por favor, digite o CAPTCHA no navegador e pressione Enter aqui para continuar.")

    # Espera até que o elemento "botão" encontrado pelo "name" da tag da pesquisa (<button...) no codigo fonte do site (no caso é "btn_pesquisar") ser carregado, e clica
    espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "btn_pesquisar"))).click()

    # Dá um tempinho pro site atualizar a classe do alerta
    time.sleep(3)

    #Verifica se o alerta aparece - isso indica CAPTCHA errado
    alerta = espera.until(condicaoEspera.visibility_of_element_located((By.ID, 'alerta'))) #Espera o elemento 'alerta' que está oculto aparecer na tela
     #Espera o elemento 'alerta' que está oculto aparecer na tela
    classe_alerta = alerta.get_attribute("class")  # Pega o valor (nome) da classe da '<div' do elemento

    if classe_alerta and "aberto" in classe_alerta: #Se tiver vindo algo em "classe" e o nome a classe ="aberto"...
        print("⚠️ CAPTCHA inválido. Tente novamente.")
        continue
    else:
        print("✅ Primeiro CAPTCHA resolvido.")
        break
#-----------------------------------------------------------------------------------------------------------

# Garante que a página de resultados realmente carregou (ao carregar de volta a barra de pesquisa) antes de ir para o for
espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]')))
#-----------------------------------------------------------------------------------------------------------

#Até aqui o código só serviu pra chegar na tela do cep impresso em tela, não esta extraindo ainda os endereços
#A partir da tela que o codigo parou até aqui, será feito o loop de voltar pra pagina inicial, inserindo os ceps do dicionarioCEPS e extraindo-os

# Percorrendo as linhas dentro do dicionário de CEP's
for cep in dicionarioCEPS.values():  # cep = linha que esta sendo percorrida (no caso ela ja vem recebendo o valor daquela linha por conta do ".values()")

    #Clicando no botão "Nova Busca" para voltar para a pagina inicial e recomeçar a pesquisa
    #No video foi usado "find_elemento(By.NAME)" mas no codigo atual não há mais "NAME" da tag do botão, portanto usei ID
    espera.until(condicaoEspera.visibility_of_element_located((By.ID, 'btn_nbusca'))).click()

    # Espera até que o elemento " barra de pesquisa" encontrado pelo "name" da tag da pesquisa (<input...) no codigo fonte do site (no caso é "endereco") ser carregado, e digita o cep
    barraPesquisa = espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "endereco"))) #Envia o "dicionarioCEPS.values()" da linha atual
    barraPesquisa.clear()
    barraPesquisa.send_keys(cep) # Digita o cep atual do dicionarioCEPS


    #-------ADAPTACÃO EXTRA MINHA: Loop de verificação feito exclusivamente para tratar o captcha---------------------
    #   Verifica se o CAPTCHA foi resolvido corretamente
    while True:

        #Esperar o CAPTCHA do site ser resolvido manualmente e ter digitado "ENTER" no terminal antes de seguir com a automação
        input("Por favor, digite o CAPTCHA no navegador e pressione Enter aqui para continuar.")

        # Espera até que o elemento "botão" encontrado pelo "name" da tag da pesquisa (<button...) no codigo fonte do site (no caso é "btn_pesquisar") ser carregado, e atribui a variavel
        espera.until(condicaoEspera.visibility_of_element_located((By.NAME, "btn_pesquisar"))).click()

        # Pequena espera para o site processar o CAPTCHA (evita checar muito rápido e pegar o estado anterior)
        time.sleep(3)

        #Verifica se o alerta aparece - isso indica CAPTCHA errado
        alerta = espera.until(condicaoEspera.visibility_of_element_located((By.ID, 'alerta'))) #Espera o elemento 'alerta' que está oculto aparecer na tela
        classe_alerta = alerta.get_attribute("class")  # Pega o valor (nome) da classe da '<div' do elemento

        if classe_alerta and "aberto" in classe_alerta: #Se tiver vindo algo em "classe" e o nome a classe ="aberto"...
            print("CAPTCHA inválido. Por favor, resolva novamente.")
            continue #Volta para o início do loop

        else:
            print("CAPTCHA resolvido corretamente.")
            # Se não cair no except, o CAPTCHA foi aceito e podemos prosseguir
            break

    #-----------------------------------------------------------------------------------------------------------

    try:
        # Espera até que o elemento "tabela" encontrado pelo "XPath" (clique com o botão direito e em Copy, clique em Copy XPath) da tag da tabela (<table...)
        #  no codigo fonte do site (no caso é "//*[@id="resultado-DNEC"]") ser carregado, e atribui a variavel
        #OBS. Para descobrir o elemento necessário é na tentativa e erro, poderia ser no (<tbody... ou <tr...) que recebem as linhas e colunas tambem,
        #  no caso funcionou pegando direto da tabela inteira (<table...)
        elementoTabela = espera.until(condicaoEspera.visibility_of_element_located((By.XPATH, '//*[@id="resultado-DNEC"]')))
        endereco = ""

        #Percorre as linhas da tabela do site pegando as linhas "tr"
        for linha in elementoTabela.find_elements(By.TAG_NAME, "tr"): 
            # Percorrendo as colunas dentro da linha (encontradas pelo nome da tag "td") no codigo fonte dentro da tag da linha (<tr...)
            for coluna in linha.find_elements(By.TAG_NAME, "td"): # j = colunaTabela
                endereco += ";" + coluna.text #Variável "endereco" recebe os valores das colunas separados por ";"

        #Imprimindo informações obtidas
        print('\n --------------------------------------------- \n')
        print('Endereço:', endereco)
        print('\n --------------------------------------------- \n')

    except:
        print("Erro: a tabela não foi carregada. Verifique se o CAPTCHA foi realmente resolvido.")



#Impedir o programa finalize e feche o navegador
input("Pressione Enter para finalizar.")

