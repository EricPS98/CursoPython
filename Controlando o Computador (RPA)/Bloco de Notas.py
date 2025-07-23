
import pyautogui as posicaoAbreArquivos
import pygetwindow as obterJanela

# Hotkey deixa pressionar 2 teclas ao mesmo tempo (Tecla "Windows" + "R")
posicaoAbreArquivos.hotkey('win', 'r')

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)

#Digitando na caixa 'Executar' a palavra 'notepad' para abrir o bloco de notas
posicaoAbreArquivos.typewrite('notepad')

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(1)

#Pressionando a tecla "Enter"
posicaoAbreArquivos.press('enter')

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)

#Digitando dentro do bloco de notas
posicaoAbreArquivos.write('Bloco de notas aberto com o Python! :)', interval=0.05)

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)

#Nova variável que permite pegar a janela que está ativa
fecharBlocoDeNotas = obterJanela.getActiveWindow()

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(1)

#Aciona a opção para fechar a janela ativa
fecharBlocoDeNotas.close()

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(1)

#Pressiona "TAB" para selecionar a próxima opção (Não salvar) que aparece após fechar o bloco de notas
posicaoAbreArquivos.press('tab')

#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(1)

#Pressionando a tecla "Enter" para fechar sem salvar
posicaoAbreArquivos.press('enter')

print("Automação executada com sucesso!")