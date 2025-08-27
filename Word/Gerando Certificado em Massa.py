from docx import Document
from docx.shared import Pt #Manipulação de fontes

from openpyxl import load_workbook #Manipulação de Excel

import os # ADIÇÃO EXTRA MINHA: Módulo do Python que serve para interagir com o sistema operacional

#Pegando o arquivo Excel
arquivoAlunos = "D:\\\\Users\\eric.psouza\\Documents\\Cursos\\Curso Lógica de Programação (Python)\\Word\\Alunos.xlsx"
planilhaDadosAlunos = load_workbook(arquivoAlunos)

#Seleciona a planilha
sheet_selecionada = planilhaDadosAlunos['Nomes'] 

for linha in range(2, len(sheet_selecionada["A"]) + 1): #Percorre as linhas da planilha (começa na linha 2, pois a 1 é o cabeçalho)


    #Abre o arquivo do Word
    arquivoWord = Document("D:\\\\Users\\eric.psouza\\Documents\\Cursos\\Curso Lógica de Programação (Python)\\Word\\Certificado2.docx")

    #Seleciona o estilo
    estilo = arquivoWord.styles['Normal']

    #Pega o valor do nome do aluno na coluna 'A' passando pelas linhas
    #O %s funciona como um placeholder (um espaço reservado) para inserir um valor de texto ou número
    #O operador % pega a string (linha) e substitui o %s pelo valor que vem depois.
    nomeAluno = sheet_selecionada['A%s' % linha].value 

    for i in arquivoWord.paragraphs: #i = paragrafo

        if "@nome" in i.text:
            i.text = nomeAluno #Substitui o @nome pelo nome do aluno
            #Formatando o texto adicionado
            fonte = estilo.font
            fonte.name = "Calibri"
            fonte.size = Pt(24) #Tamanho da fonte

    # ADIÇÃO EXTRA MINHA: Cria variáveis de caminho para salvar o arquivo aonde eu quiser e não na pasta raíz do projeto
    caminho_base = r'D:\Users\eric.psouza\Documents\Cursos\Curso Lógica de Programação (Python)\Word\Arquivos gerados'
    nome_arquivo = nomeAluno + ' - Certificado.docx' # Gera o nome do arquivo com o nome do aluno
    caminho_completo = os.path.join(caminho_base, nome_arquivo) # 'os.path.join' junta partes de caminhos (independente do sistema operacional)

    #Salva o arquivo com o nome desejado no local desejado
    arquivoWord.save(caminho_completo)

print("Certificados gerados com sucesso!")