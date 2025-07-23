from selenium import webdriver as opcoesSelenium # Importando o módulo que controla o navegador (webdriver) da biblioteca Selenium
from selenium.webdriver.common.by import By #Importando a Classe By, que é usada para localizar elementos HTML dentro da página
import time

import pandas as pd #Biblioteca para trabalhar com tabelas

import os # ADIÇÃO EXTRA MINHA: Módulo do Python que serve para interagir com o sistema operacional.

# Abrir o Chrome
navegador = opcoesSelenium.Chrome()

# Abrindo o site do rpachallengerocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

# Aguarde 1 segundo para a página carregar completamente
time.sleep(1)

# No site, clique com o botão direito do mouse e vá em "Inspecionar" (ou aperta F12),
# encontre no codigo html a tag de abertura da tabela "<table id =...", clique com o botão direito e em Copy,
# clique em Copy XPATH para obter o valor (no caso o obtido foi: //*[@id="tableSandbox"] )
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#Ainda em inspecionar, abra a tag "table" a dentro dela, pegue a tag identificador das linhas da tabela, no caso é todo 'tr'
linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')

#Ainda em inspecionar, abra qualquer tag "tr" (linha) e pegue agora o identificador das colunas, no caso é o 'td'
colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

#↑ Da forma feita acima, será verificado em todas as linhas e todas as colunas da tabela ↑

dataFrameLista = [] #Cria uma lista

linha = 1

for i in linhas: #i = linha atual
    print(i.text)
    # "i.text" Adiciona linha por linha na nova lista porém como uma string inteira
    # Porém i.text.split() transforma essa string em uma lista com colunas separadas
    dataFrameLista.append(i.text) 

    linha +=  1 #Incrementa a variável "linha" em 1

#Usando o Pandas para criar o arquivo excel chamado 'dadosSite', engine é o mecanismo, ou seja, o que ele vai utilizar, no caso, vai usar a biblioteca 'xlsxwriter'
#arquivoExcel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter') <- não funciona mais.
#arquivoExcel.save()    <- o método save() não existe mais na forma como o pandas.ExcelWriter funciona nas versões atuais do pandas

# ↓ VERSÃO ATUALIZADA ↓
#Usando o Pandas para criar o arquivo excel chamado 'dadosSite', engine é o mecanismo, ou seja, o que ele vai utilizar, no caso, vai usar a biblioteca 'xlsxwriter'

#Cria um dataframe que recebe a lista que foi incrementada com as linhas obtidas do site, com o cabeçalho da coluna = 'Coluna_Dados'
dataFrame = pd.DataFrame(dataFrameLista, columns=['Coluna_Dados']) 

# ADIÇÃO EXTRA MINHA: Cria variáveis de caminho para salvar o arquivo aonde eu quiser e não na pasta raíz do projeto
caminho_base = r'D:\Users\eric.psouza\Documents\Cursos\Curso Lógica de Programação (Python)\Extraindo Dados Tabela (RPA)\Dados Extraidos'
nome_arquivo = 'dadosSite.xlsx'
caminho_completo = os.path.join(caminho_base, nome_arquivo) # 'os.path.join' junta partes de caminhos (independente do sistema operacional)

#Prepara o arquivo do excel usando o 'xlsxwriter' como mecanismo
#ADIÇÂO EXTRA MINHA: ao inves de passar só o nome do arquivo, que faria ele salvar na pasta raíz do projeto, 
# passei o caminnho inteiro com o nome do arquivo para salvar onde eu quiser
arquivoExcel = pd.ExcelWriter(caminho_completo, engine='xlsxwriter') 

#Escreve no excel o dataframe carregado com a lista, no formato da variavel 'arquivoExcel' e com o nome da planilha 'Sheet1'
dataFrame.to_excel(arquivoExcel, sheet_name='Sheet1', index=False) #index = True autorizaria adicionar uma coluna de índice a esquerda (0,1,2,3...)

# Fecha o arquivo
arquivoExcel.close()