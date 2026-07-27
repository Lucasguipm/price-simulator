import re
import requests
from bs4 import BeautifulSoup

def extract_asin(url):
    """Extrai o identificador único (ASIN) da URL da Amazon."""
    match = re.search(r'/(?:dp|gp/product)/([A-Z0-9]{10})', url)
    return match.group(1) if match else None

def get_amazon_product_details(url):
    """
    Faz o scraping dos detalhes reais do produto na Amazon Brasil.
    """
    # Cabeçalhos completos para evitar o bloqueio da Amazon
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=10)
        
        print(f"[DEBUG] Status Code Amazon: {response.status_code}") # Log para acompanharmos no terminal

        if response.status_code != 200:
            print("[DEBUG] Amazon bloqueou a requisição ou o link é inválido.")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        # 1. Título do Produto
        title_element = soup.find(id="productTitle")
        title = title_element.get_text(strip=True) if title_element else "Produto Amazon"

        # 2. Imagem do Produto
        img_element = soup.find(id="landingImage")
        image_url = ""
        if img_element:
            image_url = img_element.get('src') or img_element.get('data-old-hires') or ""

        # 3. Preço Atual
        price = None
        price_element = soup.find("span", class_="a-offscreen")
        
        if price_element:
            raw_price = price_element.get_text(strip=True)
            cleaned_price = re.sub(r'[^\d,]', '', raw_price).replace(',', '.')
            if cleaned_price:
                try:
                    price = float(cleaned_price)
                except ValueError:
                    price = None

        # Fallback de segurança caso o preço estivesse oculto/indisponível
        if not price:
            price = 0.00

        return {
            "title": title,
            "image_url": image_url,
            "current_price": price
        }

    except Exception as e:
        print(f"[DEBUG] Erro no Scraping: {e}")
        return None