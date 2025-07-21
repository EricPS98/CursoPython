import pyautogui as escolha_opcao
import pymsgbox as caixa_de_dialogo


opcao = caixa_de_dialogo.confirm('Clique no botão desejado', 
                            buttons = ['Excel', 'Word', 'Notepad'])

if opcao == "Excel":
    #Apertando as teclas (Windows + R)
    escolha_opcao.hotkey('win', 'r')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(2)
    
    #Digitando a palavra "Excel"
    escolha_opcao.write('Excel')

    #Apertando tecla "enter" do teclado para abrir o programa
    escolha_opcao.press('enter')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(3)

    #Pegando posição do mouse
    #print(escolha_opcao.position())

    #Clicando na opção "Pasta de trabalho em branco"
    escolha_opcao.click(x=-1471, y=325)

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    #Digitando no excel
    escolha_opcao.write('Escolhi abrir o Excel', interval=0.05)

    print("Você escolheu abrir o Excel")

elif opcao == "Word":

    #Apertando as teclas (Windows + R)
    escolha_opcao.hotkey('win', 'r')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(2)
    
    #Digitando a palavra "Word"
    escolha_opcao.write('winword')

    #Apertando tecla "enter" do teclado para abrir o programa
    escolha_opcao.press('enter')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(3)

    #Apertando tecla "enter" do teclado para abrir a opção "Pasta de trabalho em branco" (autoselecionada)
    escolha_opcao.press('enter')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    #Digitando no Word
    escolha_opcao.write('Escolhi abrir o Word', interval=0.05)

    print("Você escolheu abrir o Word")

else:

    #Apertando as teclas (Windows + R)
    escolha_opcao.hotkey('win', 'r')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(2)
    
    #Digitando a palavra "notepad"
    escolha_opcao.write('notepad')

    #Apertando tecla "enter" do teclado para abrir o programa
    escolha_opcao.press('enter')

    #Aguardando 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    #Digitando no Word
    escolha_opcao.write('Escolhi abrir o Bloco de Notas', interval=0.05)

    print("Você escolheu abrir o Bloco de notas")

