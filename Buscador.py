import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('Qual produto você está procurando : ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text,'html.parser')

produtos = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated'})

for produto in produtos:
    link = produto.find('a',attrs={'class':'ui-search-link'})
    
    real = produto.find('span', attrs={'class':'price-tag-fraction'})

    centavos = produto.find('span', attrs={'class':'price-tag-cents'})

    frete = produto.find('p', attrs={'class':'ui-search-item__shipping ui-search-item__shipping--free'})

    titulo = produto.find('h2',attrs={'class':'ui-search-item__title ui-search-item__group__element'})

    print(f'Produto : {titulo.text}')

    if(centavos!=None):
        print(f'Preço :R$ {real.text},{centavos.text}')
    else:
        print(f'Preço :R$ {real.text}')
        
    print(f'Frete : {frete.text}')
    
    print('Link : ',link['href'])
    
    print('\n')





