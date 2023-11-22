from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Começo do Código
print("\n---------- WEB SCRAPING WITH GOOGLE DORKS ----------\n")
textSearch = input("Caso o que queira digitar esteja em um Texto, Digite 1. Caso o que voce queira esteja em um título digite 2: ")
search = input("Digite o que quer pesquisar: ")
typeArchive = input("Caso deseja um Tipo de Arquivo Digite 1. Caso seja um site especifico digite 2: ")
archive = input("Digite o tipo do Arquivo: ")

# Função para escolher pesquisa
def codeSearch():
    global textSearch
    if textSearch == "1":
        textSearch = "intext:" + search
    elif textSearch == "2":
        textSearch = "intitle:" + search
    else:
        print("Digite uma opção válida.")

# Função para escolher o tipo de arquivo
def codeArchive():
    global typeArchive
    if typeArchive == "1":
        typeArchive = "filetype:" + archive
    elif typeArchive == "2":
        typeArchive = "site:" + archive
    else:
        print("Digite uma opção válida.")

# Funçao Principal de Web Scraping
def webScraping():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # Corrija o método find_element para aceitar dois argumentos
    elementSearch = driver.find_element(By.ID, "APjFqb")
    elementSearch.send_keys(textSearch, " ", typeArchive, Keys.ENTER)

    # Aguarde indefinidamente até que o usuário decida fechar a página
    input("Pressione Enter para fechar o navegador.")

    driver.quit()

codeSearch()
codeArchive()
webScraping()
