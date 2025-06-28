import requests
from bs4 import BeautifulSoup

def scrape_documents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(('.pdf', '.docx'))]
    return links
