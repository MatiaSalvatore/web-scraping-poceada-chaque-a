import requests
from bs4 import BeautifulSoup as Bs
import pandas as pd

#FUNCION PARA EXTRAER SORTEOS
#FUNCTION TO EXTRACT DRAWS

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


        #Extracción de números
        #Number extraction
        #Primero hago una búsqueda de la ul que contiene los números y chequeo que exista.
        numeros_ul = parser.find('ul', class_='results-list')
        if not numeros_ul:
            return None
        #Busco cada elemento li dentro de numeros_ul.
        items = numeros_ul.find_all('li', class_='results-list__item')
        numeros = []
        for i in items:
            if 'headers' in i.get('class', []):
                continue
            #Buscos los elementos p dentro de cada li
            #Como son dos p por li, hago una condición para que me devuelva solamente la columna que corresponde a los resultados.
            parrafos = i.find_all('p',class_='results-number')
            if len(parrafos)>=2:
                numero = parrafos[1].get_text(strip=True)
                if numero.isdigit():
                    numeros.append(int(numero))
        
        return {"fecha": fecha_sorteo, "numeros": numeros}
    except Exception:
        return None
#TEST
print(extraer_sorteos(934))

#