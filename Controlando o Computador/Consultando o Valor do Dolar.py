#Robô de automação para verificar a cotação do Dólar no navegador

import pyautogui as posicaoMouse
import pyautogui as tempoEspera # É possível usar a mesma para as 2 funções, mas para fins acadêmicos, será usado 2

 #Aguardar 5 segundos depois que executar para que o computador possa processar as informações
tempoEspera.sleep(2)

#Descobrir a posição do mouse (quando clicar)
#print(posicaoMouse.position())

#Movendo o mouse até a posição do botão do windows
posicaoMouse.moveTo(465, 1053)

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(465, 1053)

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Digitando o nome do navegador
posicaoMouse.typewrite('Brave')

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Pressionando a tecla "Enter" para abrir o navegador autoselecionado após digitar o nome dele
posicaoMouse.press('Enter')

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Digitando a palavra 'Dolar' para pesquisar no navegador
posicaoMouse.typewrite('Dolar hoje')

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Pressionando a tecla "Enter" para pesquisar
posicaoMouse.press('Enter')