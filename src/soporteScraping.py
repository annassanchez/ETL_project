import requests
import pandas as pd
from time import sleep
import numpy as np
from tqdm import tqdm
import os
import pickle
import re
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options

import numpy as np
from IPython.display import clear_output

import warnings
warnings.filterwarnings('ignore')

def scrapingGeniusChrome(test, filename):
    ## iniciamos el web driver
    opciones= Options()
    opciones.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=opciones)
    driver.get('https://genius.com/')
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    ## te metes dentro de la página y con inspeccionar, seleccionas el elemento de las cookies --> copy / selector
    ##por si tu ordenador es un poco lento, le puedes poner un tiempo para que intente hacerlo
    driver.implicitly_wait(30)
    almacen_paginas = {
        'pagina' : [], 
        'lyrics':[],
        'featuring' : [],
        'produced_by': [],
        'label': [],
        'written by': [],
        'drums': [],
        'guitar': [],
        'recorded_at' : [],
        'release_date':[],
        'url':[]
    }
    for index, row in test.iterrows():
        print(index, row['artist'].split(',')[0],'---', row['track'].split('-')[0])
        almacen_paginas['url'].append(row['url'])
        if index == 0: 
            driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()
            #sleep(1)
            ## busco el nombre de canción que quiero buscar
            driver.find_element(By.CSS_SELECTOR, '#application > div > div.PageHeaderdesktop__Container-bhx5ui-0.dmNhEr > div.PageHeaderdesktop__Left-bhx5ui-2.ctcvqz > form > input').send_keys(row['artist'].split(',')[0] + ' ' + row['track'].split('-')[0], Keys.ENTER)
            #sleep(1)
        else:
            ## busco el nombre de canción que quiero buscar
            try:
                driver.find_element(By.CSS_SELECTOR, '#sticky-nav > div.StickyNavdesktop__Right-sc-60o25r-2.kMDkxm > form > input').send_keys(row['artist'].split(',')[0] + ' ' + row['track'].split('-')[0], Keys.ENTER)
            except:
                driver.find_element(By.CSS_SELECTOR, '.StickyNavSearchdesktop__Input-sc-1wddxfx-2').send_keys(row['artist'].split(',')[0] + ' ' + row['track'].split('-')[0], Keys.ENTER)
        # sleep(1)
        ## selecciono el resultado de la búsqueda que quiero
        try:
            driver.find_element('xpath', '/html/body/routable-page/ng-outlet/search-results-page/div/div[2]/div[1]/div[2]/search-result-section/div/div[2]/search-result-items/div[1]/search-result-item/div/mini-song-card/a').click()
            driver.implicitly_wait(30)
            ## clico el all credits
            try:
                driver.find_element('xpath', '//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[4]/div/a').click()
            except:
                try:
                    driver.find_element('xpath', '//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[3]/div/a').click()
                except:
                    try:
                        driver.find_element('xpath', '//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[2]/div/a').click()
                    except:
                        try:
                            driver.find_element('xpath', '//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div[1]/div/a').click()
                        except:
                            print('oye que no va')
                            break
            #'//*[@id="application"]/main/div[1]/div[4]/div/div[1]/div/div/a'
            #sleep(1)
            page_source = driver.page_source
            url = driver.current_url
            res = requests.get(url + '#song-info')
            soup = BeautifulSoup(res.content, 'html.parser')
            pagina = soup.text
            almacen_paginas['pagina'].append(pagina)
            try:
                almacen_paginas['lyrics'].append(re.findall(r'Lyrics(.*)EmbedCancel?', pagina)[0])
            except:
                almacen_paginas['lyrics'].append(np.nan)
            with open(f'../data/pickle/{filename}.pickle', 'wb') as data_scrapeado:
                pickle.dump(almacen_paginas, data_scrapeado)
            clear_output(wait=True)
            return almacen_paginas
        except:
            almacen_paginas['pagina'].append(np.nan)
            almacen_paginas['lyrics'].append(np.nan)
            clear_output(wait=True)
        return almacen_paginas