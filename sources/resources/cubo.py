from unicodedata import name
from flask import Blueprint
from sources.utils.response import Response
from sources.business.cubo import CuboBusiness
import requests
from bs4 import BeautifulSoup as bs
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options  
# from selenium.webdriver.support.ui import Select
import os
from playwright.sync_api import sync_playwright as sp

cubo_api = Blueprint('cubo', __name__)
cubo_business = CuboBusiness()
header = { "Authorization" : "Basic aXRicm9rZXI6cmVrb3JidGkz" }

# chrome_options = Options()
# chrome_options.add_argument("--headless") # faz com que o browser não abra durante o processo
# simp_path = 'chromedriver'
# abs_path = os.path.abspath(simp_path)
# os.chmod(abs_path,755)
# driver = webdriver.Chrome(executable_path=abs_path,options=chrome_options)

@cubo_api.route('/getfullcnpj/<int:cnpj>', methods=['GET'], strict_slashes=False)
def find_all(cnpj):

    with sp() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.crunchbase.com/v4/data/autocompletes?query=cortex-intelligence&collection_ids=organizations&limit=25")
        print('--=--=-=-=-=-=-=-=-=-=')
        print(page.title())
        print('--=--=-=-=-=-=-=-=-=-=')
        browser.close()


    # driver.get('https://www.crunchbase.com/v4/data/autocompletes?query=cortex-intelligence&collection_ids=organizations&limit=25')

    # page = driver.page_source

    # result = requests.get(f'https://www.crunchbase.com/v4/data/autocompletes?query=cortex-intelligence&collection_ids=organizations&limit=25');
    
    # page = bs(result.text,"html.parser")
    # if page.title:
    #     if page.title.string == ''


    # html = open('page.html', 'w')
    # html.write(page)
    # html.close()
    
    # speedio = requests.get(f'http://api-es.speedio.com.br:5003/getfullcnpjdata?cnpj={cnpj}',headers=header).json()
    
    # if 'WEBSITE' in speedio:
    #     if speedio['WEBSITE'] != "":
    #         speedio = speedio['WEBSITE'].split('.')[1]
    #         print(speedio)
    #         company = requests.get(f'http://67.205.133.96/dev/company/{speedio}').json()
            
    #         name_company = company,name

    #         # return inf_company

    return ""


def getCrunchCompany(company):

    result = requests.get(f'https://www.crunchbase.com/v4/data/autocompletes?query={company}&collection_ids=organizations&limit=25');

