# <--------- By Clevs ------------>


# Importar bibliotecas 
from PySimpleGUI.PySimpleGUI import Window
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import PySimpleGUI as sg
import time
import sys
import os

# Inicia e baixa o webdriver para o chrome
       
       

def search():
    font = ("Arial", 8)
    layout = [
           [sg.Text('Material :'),sg.Input()],
           [sg.Button('Buscar',bind_return_key=True),sg.Button('Sair'),] ,
           [sg.Text('By Clevs', justification='right',size=(80, 1),font=font)]          
       ]
    
    janela = sg.Window("Material Hub",disable_close=True).layout(layout)
    
       
    button, values = janela.Read()
       
    janela.close()
    # Pegar termo a ser buscado
    
    term = values
    
    if button == 'Sair':
        layout2 = [
                   [sg.Text('Deseja encerrar o programa?')],
                   [sg.Button('Sim',bind_return_key=True),sg.Button('Não')]  
                   ]
        janela2 = sg.Window("Material Hub",disable_close=True,element_justification="center").layout(layout2)
        button, values = janela2.Read()
        if button == 'Sim':
            janela2.close()
            sys.exit(0)
        else:
            janela2.close()
            search()
        
    else:
        
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        # <--- Busca na primeira pagina Polyheaven --->
        browser.get("https://polyhaven.com/textures")
        search_box=browser.find_element_by_xpath('//*[@id="page"]/div[1]/div[1]/div/div[1]/div[2]/form/input')
        search_box.send_keys(term)
        search_box.submit()
        # <--- Fim da primeira Busca Polyheaven --->

        # <--- Abrir proxima busca em nova aba "cgbookcase" --->
        browser.execute_script("window.open('https://www.cgbookcase.com/textures/', '_blank')")
        browser.switch_to_window(browser.window_handles[1])
        time.sleep(3)

        search_box2=browser.find_element_by_xpath('//*[@id="search-container"]/input')
        search_box2.send_keys(term)
        browser.find_element_by_xpath('//*[@id="search-container"]/button').click()

        # <--- FIm da busca na segunda pagina cgbookcase --->


        # <--- Abrir proxima busca em nova aba "textures" --->
        browser.execute_script("window.open('https://www.textures.com/search', '_blank')")
        browser.switch_to_window(browser.window_handles[2])
        time.sleep(3)

        search_box3=browser.find_element_by_xpath('//*[@id="search-box"]/div/form/div[1]/input')
        search_box3.send_keys(term)
        browser.find_element_by_xpath('//*[@id="search-box"]/div/form/button').click()

        # <--- Fim da busca na terceira pagina texture --->
        
        
        # <--- Abrir proxima busca em nova aba "ambientcg" --->
        browser.execute_script("window.open('https://ambientcg.com/list', '_blank')")
        browser.switch_to_window(browser.window_handles[3])
        time.sleep(3)

        search_box3=browser.find_element_by_xpath('//*[@id="searchInput"]')
        search_box3.send_keys(term)
        browser.find_element_by_xpath('/html/body/div[2]/form/div[1]/button').click()
        # <--- Fim da busca na terceira pagina ambientcg --->
        
        # <--- Abrir proxima busca em nova aba "Sketchup Textures" --->
        browser.execute_script("window.open('https://www.sketchuptextureclub.com/textures', '_blank')")
        browser.switch_to_window(browser.window_handles[4])
        time.sleep(3)

        search_box3=browser.find_element_by_xpath('//*[@id="cerca"]')
        search_box3.send_keys(term)
        browser.find_element_by_xpath('//*[@id="search"]').submit()
        # <--- Fim da busca na terceira pagina ambientcg --->
        
        os.system("taskkill /im chromedriver.exe")
        return search()   
        
      
    

search()