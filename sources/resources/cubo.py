from time import sleep
from flask import Blueprint
from sources.utils.response import Response
from sources.business.cubo import CuboBusiness
import requests
from bs4 import BeautifulSoup   
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import Select
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument("--headless")
simp_path = 'chromedriver'
abs_path = os.path.abspath(simp_path)
os.chmod(abs_path,755)
driver = webdriver.Chrome(executable_path=abs_path,options=chrome_options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)
#Remove navigator.webdriver Flag using JavaScript
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
print('arguments done')
# driver.get('https://www.google.com')
driver.get('https://www.crunchbase.com/organization/cortex-intelligence')
sleep(5)
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

description = soup.find('span', attrs={'class':'description'}).next


cubo_api = Blueprint('cubo', __name__)
cubo_business = CuboBusiness()
header = { "Authorization" : "Basic aXRicm9rZXI6cmVrb3JidGkz" }


@cubo_api.route('/getfullcnpj/<int:cnpj>', methods=['GET'], strict_slashes=False)
def find_all(cnpj):

    # with sync_playwright() as p:
    #     browser = p.chromium.launch()
    #     page = browser.new_page()
    #     result = page.goto("https://www.crunchbase.com/v4/data/autocompletes?query=cortex-intelligence&collection_ids=organizations&limit=25")

    #     # result = page.evaluate()  # page.query_selector('.page-title').inner_text()        
   
    #     verificacao = page.query_selector('.page-title').inner_text()

    #     tentativas = 0;
        
        # while(verificacao == "Please verify you are a human"):
        #     print("Resolvendo captcha tentativas ", tentativas);
        #     sleep(5);
        #     page.screenshot(path='ss.png');
        #     page.mouse.move(0, 0);
        #     page.mouse.move(150, 240);
        #     page.mouse.down();
        #     sleep(7);
        #     page.screenshot(path='ss2.png');
        #     page.mouse.up();
        #     sleep(10);
        #     page.screenshot(path='ss3.png');
        #     verificacao = page.query_selector('.page-title').inner_text()     

        #     tentativas += 1

        #     if tentativas > 2: 
        #         page.close()
        #         break

    #     if tentativas <= 2:
    #         result = page.content()

    #     browser.close()

    # return result

    driver = webdriver.Chrome(executable_path=abs_path,options=chrome_options)
    # driver.get('https://www.crunchbase.com/v4/data/autocompletes?query=cortex-intelligence&collection_ids=organizations&limit=25')

    # json_company = driver.page_source

    driver.get('https://www.crunchbase.com/organization/cortex-intelligence')

    driver.close()


    # result = requests.get(f'https://www.crunchbase.com/v4/data/autocompletes?query=cortex-intelligence&collection_ids=organizations&limit=25');
    
    # page = bs(result.text,"html.parser")
    # if page.title:
    #     if page.title.string == '':

    # html = open('page.html', 'w')
    # html.write(page)
    # html.close()
    
    return page


    # speedio = requests.get(f'http://api-es.speedio.com.br:5003/getfullcnpjdata?cnpj={cnpj}',headers=header).json()
    
    # if 'WEBSITE' in speedio:
    #     if speedio['WEBSITE'] != "":
    #         speedio = speedio['WEBSITE'].split('.')[1]
    #         print(speedio)
    #         company = requests.get(f'http://67.205.133.96/dev/company/{speedio}').json()
            
    #         name_company = company,name

    #         # return inf_company


def getCrunchCompany(company):

    result = requests.get(f'https://www.crunchbase.com/v4/data/autocompletes?query={company}&collection_ids=organizations&limit=25');

