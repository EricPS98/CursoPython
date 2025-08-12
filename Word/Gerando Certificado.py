from docx import Document
from docx.shared import Pt #Manipulação de fontes

import os # ADIÇÃO EXTRA MINHA: Módulo do Python que serve para interagir com o sistema operacional

#Abre o arquivo do Word
arquivoWord = Document("D:\\\\Users\\eric.psouza\\Documents\\Cursos\\Curso Lógica de Programação (Python)\\Word\\Certificado1.docx")

#Seleciona o estilo
estilo = arquivoWord.styles['Normal']

for i in arquivoWord.paragraphs: #i = paragrafo

    if "@nome" in i.text:
        i.text = "Eric Palmeira"
        #Formatando o texto adicionado
        fonte = estilo.font
        fonte.name = "Calibri"
        fonte.size = Pt(24) #Tamanho da fonte

# ADIÇÃO EXTRA MINHA: Cria variáveis de caminho para salvar o arquivo aonde eu quiser e não na pasta raíz do projeto
caminho_base = r'D:\Users\eric.psouza\Documents\Cursos\Curso Lógica de Programação (Python)\Word\Arquivos gerados'
nome_arquivo = 'Eric Palmeira - Certificado.docx'
caminho_completo = os.path.join(caminho_base, nome_arquivo) # 'os.path.join' junta partes de caminhos (independente do sistema operacional)

#Salva o arquivo com o nome desejado no local desejado
arquivoWord.save(caminho_completo) 