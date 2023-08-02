from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()

link = "https://www.investing.com/"

navegador.get(url=link)
navegador.maximize_window()
navegador.implicitly_wait(5)

try:
    navegador.find_element(by=By.CLASS_NAME, value="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon")
except:
    pass

tabela = navegador.find_element(by=By.CLASS_NAME, value="genTbl.openTbl.smallTbl")
dados = []

for linhas in tabela.find_elements(by=By.TAG_NAME, value="tr"):
    linhaDados = []
    for coluna in linhas.find_elements(by=By.TAG_NAME, value="td"):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)

# Instanciando um DataFrame() para pegar diferentes tipos de dados (int, string, boolean, etc.) das colunas da tabela
df = pd.DataFrame(dados)

# Removendo a primeira linha de dados da tabela, pois ela é vazia
df.iloc[1:, :]

# Definindo o cabeçalho do DataFrame(). Precisa ter o mesmo número que as colunas.
df.columns = ["Positivo/Negativo", "Name", "Month", "Last", "Chg.%"]

print(df)

#Salvando os dados em csv

df.to_csv("dadosIndicesDaBolsa.csv")