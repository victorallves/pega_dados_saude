from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

lista_links = [
  
]

nomes_hospitais = []
enderecos_hospitais = []
lista_servicos_hospitais = []

driver = webdriver.Chrome()

for link in lista_links:
    driver.get(link)
    nome_hospital = driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']").text
    endereco_hospital = driver.find_element(By.CSS_SELECTOR, "p[itemprop='address']").text

    servicos = driver.find_elements(By.CSS_SELECTOR, "table.table.tabelaServEspec tbody tr")
    servicos_hospital = []
    for servico in servicos:
        nome_servico = servico.find_element(By.CSS_SELECTOR, "td:nth-of-type(1)").text
        caracteristica_servico = servico.find_element(By.CSS_SELECTOR, "td:nth-of-type(2)").text
        servicos_hospital.append({"Nome do Serviço": nome_servico, "Característica": caracteristica_servico})

    nomes_hospitais.append(nome_hospital)
    enderecos_hospitais.append(endereco_hospital)
    lista_servicos_hospitais.append(servicos_hospital)

driver.quit()

lista_hospitais = []

for nome_hospital, endereco_hospital, servicos_hospital in zip(nomes_hospitais, enderecos_hospitais, lista_servicos_hospitais):
    for servico in servicos_hospital:
        lista_hospitais.append({"Nome": nome_hospital, "Endereço": endereco_hospital, "Serviço": servico})

dados_hospitais = pd.DataFrame(lista_hospitais)

dados_hospitais.to_excel("postos_publicos.xlsx", index=False)