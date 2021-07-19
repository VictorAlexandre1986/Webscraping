from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

class Navegador():
    driver=''
    def __init__(self):
        options = Options()
        #options.add_argument(--headless) Esse comando executa mas não exibe as janelas
        options.add_argument('window-size=400,800')
        self.driver = webdriver.Chrome(options=options)
    
    def acessar(self,site):
        self.driver.get(site)
        
    def codigo_fonte(self):
        self.site = BeautifulSoup(self.driver.page_source,'html.parser').prettify()
        print(self.site)
        
    def buscar(self,conteudo):
        self.input_place = self.driver.find_element_by_class_name('nav-search-input')
        #Inserindo conteudo no textbox
        self.input_place.send_keys(conteudo)
        self.input_place.submit()
        
    def acessar_produto(self):
        #Encontrando por tipo do elemento 
        self.link =self.driver.find_element_by_class_name('ui-search-result__content ui-search-link')
        self.link.click()[1]
        #print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>{self.link}')
        
        
    def sair(self):
        self.driver.quit()
            
if __name__=='__main__':
    nav = Navegador()
    nav.acessar('https://www.mercadolivre.com.br/')
    sleep(1)#Precisa aumentar o sleep para poder pegar todo o html
    nav.codigo_fonte()
    nav.buscar('ps4')
    sleep(1)
    nav.acessar_produto()
    #nav.sair()
            

    