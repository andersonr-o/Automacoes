from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import Select
from IPython.display import display

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

# Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager(driver_version='114.0.5735.90').install())
driver = webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.imdb.com/chart/top")
driver.maximize_window()
sleep(1)

linksFilmes = driver.find_element(by=By.CLASS_NAME, value="ipc-page-grid.ipc-page-grid--bias-left").find_element(by=By.TAG_NAME, value="ul").find_elements(by=By.TAG_NAME, value="a")
links = []
planilha = []
linha = []

i = 0

while i < 500:
    links.append(linksFilmes[i].get_attribute("href"))
    i = i + 2

for linkAtual in links:
    driver.get(linkAtual)
    sleep(1)
    nomeFilme = driver.find_element(by=By.CSS_SELECTOR, value="#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-304f99f6-0.eaRXHu > section > div:nth-child(4) > section > section > div.sc-e226b0e3-3.jJsEuz > div.sc-acac9414-0.jFcAtv > h1 > span").text
    linha.append(nomeFilme)

    anoLancamento = driver.find_element(by=By.CSS_SELECTOR, value="#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-304f99f6-0.eaRXHu > section > div:nth-child(4) > section > section > div.sc-e226b0e3-3.jJsEuz > div.sc-acac9414-0.jFcAtv > ul > li:nth-child(1) > a").text
    linha.append(anoLancamento)

    duracao = driver.find_element(by=By.CSS_SELECTOR, value="#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-304f99f6-0.eaRXHu > section > div:nth-child(4) > section > section > div.sc-e226b0e3-3.jJsEuz > div.sc-acac9414-0.jFcAtv > ul > li:nth-child(3)").text
    linha.append(duracao)

    avaliacao = driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span").find_element(by=By.TAG_NAME, value="span")
    avaliacao = avaliacao.get_attribute('innerText') # Para tags <span>, é melhor usar innerText.
    linha.append(avaliacao)

    try:
        descricao = driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/p/span[3]").text
    except:
        descricao = "Não há descrição"
    
    linha.append(descricao)

    planilha.append(linha)
    linha = []

    df = pd.DataFrame(planilha)
    df.columns = ["Nome", "Lançamento", "Duração", "Nota IMDB", "Descricao"]
    df.to_excel(r"C:\Users\ander\OneDrive\Documentos\Python\IMDbMovies\filmesPlanilhados.xlsx")

print("Arquivos salvos")
driver.quit()