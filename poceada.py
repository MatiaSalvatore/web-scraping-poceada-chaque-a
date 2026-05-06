import requests
from bs4 import BeautifulSoup as Bs
import pandas as pd

def extraer_sorteos(id_sorteo):
    url = f"https://loteria.chaco.gov.ar/detalle_poceada/{id_sorteo}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code  != 200:
            return None
        parser = Bs(response.text, 'html.parser')
    
    except Exception:
        return None