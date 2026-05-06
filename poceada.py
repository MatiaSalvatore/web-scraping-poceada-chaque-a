import requests
from bs4 import BeautifulSoup as Bs
import pandas as pd

def extraer_sorteos(id_sorteo):
    #Definición de la url y headers para la extracción, la idea es extraer ingresando el id de la página, que almacena todos los sorteos.
    #Defining the URL and headers for extraction; the idea is to extract by entering the page ID, which stores all the draws.

    url = f"https://loteria.chaco.gov.ar/detalle_poceada/{id_sorteo}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        #Conexión a la página y parseo para la lectura.
        #Conection and parsing of the webpage.
        response = requests.get(url, headers=headers)
        if response.status_code  != 200:
            return None
        parser = Bs(response.text, 'html.parser')
        
        #Extracción de fecha de sorteo.
        #Extraction of draw date.
        fecha_div = parser.find('div',class_='title')
        fecha_sorteo = None
        if fecha_div:
           h5 = fecha_div.find('h5')
           if h5:
              fecha_sorteo = h5.get_text(strip=True)


    except Exception:
        return None