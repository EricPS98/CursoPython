from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import time

navegador = opcoesSelenium.Chrome()

navegador.get('https://www.google.com.br')


time.sleep(10)  # espera 10 segundos antes de fechar
