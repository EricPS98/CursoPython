from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By #Importando a Classe By, que é usada para localizar elementos HTML dentro da página
import time as tempoEspera
import pandas as pd #Biblioteca para trabalhar com tabelas

import os # ADIÇÃO EXTRA MINHA: Módulo do Python que serve para interagir com o sistema operacional

#----- ADIÇÂO EXTRA MINHA: Imports e configuração para desabiliar os logs e deixar o terminal mais limpo ---------#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Silencia logs
#---------------------------------------------------------

# Abrir o Chrome - COM ADIÇÃO EXTRA MINHA PARA DESABILITAR OS LOGS E DEIXAR O TERMINAL MAIS LIMPO
navegador = opcoesSelenium.Chrome(service=Service(), options=chrome_options) # Parâmetros dentro do chrome com opções de desabilitar os logs

# Abrindo o site do rpachallengerocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

listaDataFrame = []

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
        # "linhaHTML.text" Adiciona linha por linha na nova lista (dataFrame) porém como uma string inteira
        # Porém linhaHTML.text.split() transforma essa string em uma lista com colunas separadas
        listaDataFrame.append(linhaHTML.text)

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


# ADIÇÃO EXTRA MINHA: Cria variáveis de caminho para salvar o arquivo aonde eu quiser e não na pasta raíz do projeto
caminho_base = r'D:\Users\eric.psouza\Documents\Cursos\Curso Lógica de Programação (Python)\Extraindo Dados Tabela (RPA)\Dados Extraidos'
nome_arquivo = 'dadosAbasSite.xlsx'
caminho_completo = os.path.join(caminho_base, nome_arquivo) # 'os.path.join' junta partes de caminhos (independente do sistema operacional)

#Prepara o arquivo do excel que terá o nome 'dadosAbasSite.xlsx' usando o 'xlsxwriter' como mecanismo
#ADIÇÂO EXTRA MINHA: ao inves de passar só o nome do arquivo, que faria ele salvar na pasta raíz do projeto, 
# passei o caminnho inteiro com o nome do arquivo para salvar onde eu quiser
arquivoExcel = pd.ExcelWriter(caminho_completo, engine='xlsxwriter')

#arquivoExcel.save() <- Foi usado na aula, mas não funciona mais(nem é necessário mais pois só o Writter já salva o arquivo automaticamente)

#Cria um dataframe que recebe a lista que foi incrementada com as linhas obtidas do site, com os cabeçalhos das colunas = '#;ID;Due Date'
dataFrame = pd.DataFrame(listaDataFrame, columns=['#;ID;Due Date'])

#arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter') <- Foi feito a mesma coisa da linha 68 na aula, mas com as bibliotecas atuais, não é mais necessário

#Escreve no excel o dataframe carregado com a lista, no formato da variavel 'arquivoExcel' e com o nome da planilha 'Dados Extraidos do Site'
dataFrame.to_excel(arquivoExcel, sheet_name='Dados Extraidos do Site', index=False) #index = True autorizaria adicionar uma coluna de índice a esquerda (0,1,2,3...)

# Fecha o arquivo
arquivoExcel.close()