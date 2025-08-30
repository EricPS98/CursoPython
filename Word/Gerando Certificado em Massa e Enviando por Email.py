from docx import Document
from docx.shared import Pt #Manipulação de fontes, aumenta o tamanho da letra da fonte

from docx.shared import RGBColor #Manipula cores, muda cor do texto

from openpyxl import load_workbook #Manipulação de Excel

import win32com.client as win32 #Manipulação do Outlook para enviar email

import os # ADIÇÃO EXTRA MINHA: Módulo do Python que serve para interagir com o sistema operacional

outlook = win32.Dispatch("outlook.application")

#Pegando o arquivo Excel
arquivoAlunos = "D:\\\\Users\\eric.psouza\\Documents\\Cursos\\Curso Lógica de Programação (Python)\\Word\\DadosAlunosEmail.xlsx" 
planilhaDadosAlunos = load_workbook(arquivoAlunos)

#Seleciona a planilha
sheet_selecionada = planilhaDadosAlunos['Nomes'] 

for linha in range(2, len(sheet_selecionada["A"]) + 1): #Percorre as linhas da planilha (começa na linha 2, pois a 1 é o cabeçalho)


    #Abre o arquivo do Word
    arquivoWord = Document("D:\\\\Users\\eric.psouza\\Documents\\Cursos\\Curso Lógica de Programação (Python)\\Word\\Certificado3.docx") 

    #Seleciona o estilo
    estilo = arquivoWord.styles['Normal']

    #Pega o valor do nome do aluno na coluna 'A', 'B', 'C'... passando pelas linhas
    #O %s funciona como um placeholder (um espaço reservado) para inserir um valor de texto ou número
    #O operador % pega a string (linha) e substitui o %s pelo valor que vem depois.
    nomeAluno = sheet_selecionada['A%s' % linha].value 
    dia = sheet_selecionada['B%s' % linha].value 
    mes = sheet_selecionada['C%s' % linha].value 
    ano = sheet_selecionada['D%s' % linha].value 
    nomeCurso = sheet_selecionada['E%s' % linha].value 
    nomeInstrutor = sheet_selecionada['F%s' % linha].value 
    emailAluno = sheet_selecionada['G%s' % linha].value 

    for i in arquivoWord.paragraphs: #i = paragrafo

        if "@nome" in i.text:
            i.text = nomeAluno #Substitui o @nome pelo nome do aluno
            #Formatando o texto adicionado
            fonte = estilo.font
            fonte.name = "Calibri"
            fonte.size = Pt(24) #Tamanho da fonte

        paragrafoP1 = 'Concluiu com sucesso o curso de '
        paragrafoP2 = ', como carga horária de 20 horas, promovido pela escola de Cursos Online em '
        terceiraParteParagrafo = f"{paragrafoP2}{dia} de {mes} de {ano}"

        if "escola" in i.text: #Pega qualquer palavra do parágrafo
            i.text = paragrafoP1 #Substitui a escola pelo parágrafo 1
            #Formatando o texto adicionado
            fonte = estilo.font
            fonte.name = "Calibri (Corpo)"
            fonte.size = Pt(24) #Tamanho da fonte
            adicionaNovaPalavra = i.add_run(nomeCurso) #Adiciona o novo texto, no caso o nomeCurso formatado
            adicionaNovaPalavra.font.color.rgb = RGBColor(255, 0, 0) #Cor Vermelha
            adicionaNovaPalavra.underline = True #Sublinhado
            adicionaNovaPalavra.bold = True #Negrito
            adicionaNovaPalavra = i.add_run(terceiraParteParagrafo) #Adiciona mais um texto, no caso o restante do parágrafo com a cor original (preto)
            adicionaNovaPalavra.font.color.rgb = RGBColor(0, 0, 0) #Cor Preto
        
        if "Instrutor" in i.text: #Pega qualquer palavra do parágrafo
            i.text = nomeInstrutor + ' - Instrutor'#Substitui a palavra "Instrutor" pela variável nomeInstrutor
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

    #Pega o primeiro nome do aluno
    primeiroNome = nomeAluno.split(None, 1)[0]

    emailOutlook = outlook.CreateItem(0)
    emailOutlook.To = emailAluno #Quem vai receber o email
    emailOutlook.Subject = "Certificado - " + nomeAluno #Titulo do email
    #Corpo do e-mail
    emailOutlook.HTMLBody = f"""
        <p>Olá, {primeiroNome}. </p>
        <p>Segue seu <b>certificado</b> de conclusão do curso <b>{nomeCurso}</b>. </p>
        <p>Atenciosamente, </p>
        <p><img src="D:\\Users\\eric.psouza\\Documents\\Cursos\\Curso Lógica de Programação (Python)\\Word\\Assinatura Email.png"></p>
    """
    #Anexo do email (certificado)
    emailOutlook.Attachments.Add(caminho_completo)
    #save() = Salvar como Draft no outlook
    #.send ou send() (em algumas empresas é bloqueado o .send ou o .send(), se não funcionar um, tente o outro)
    if emailAluno == 'potiti8509@cavoyar.com': #Criei um e-mail temporário para enviar e testar o envio
        emailOutlook.send
    else:
        emailOutlook.save()


print("Certificados gerados com sucesso!")