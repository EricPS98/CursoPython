#Robô de automação para abrir uma calculadora 

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

#Escrevendo a palavra "calc" de Calculadora
posicaoMouse.typewrite('calc')

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(1)

#Descobrir a posição do mouse 
# (nesse caso eu arrastei até o ícone de calculadora após rodar os comandos até essa parte, e o "print" me deu a posição (x=1170, y=355) para seguir com o código)
#print(posicaoMouse.position())

#Movendo o mouse até o aplicativo da calculadora (poderia dar um click direto, mas para fins acadêmicos, será movido antes)
posicaoMouse.moveTo(1170, 355)

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na calculadora
posicaoMouse.click(x=1170, y=355)

# Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#print(posicaoMouse.position())
