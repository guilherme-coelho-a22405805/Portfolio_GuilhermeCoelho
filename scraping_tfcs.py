import os
import django 
import requests
from bs4 import BeautifulSoup
import json

# Configuração Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC, Licenciatura

def scrape_lusofona_tfcs():
    url = "https://informatica.ulusofona.pt/investigacao/tfcs-dissertacoes-teses/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    

    # O site da Lusófona usa WordPress. 
    # Precisamos de encontrar os elementos que contêm os TFCs.
    # Nota: A estrutura exata depende dos seletores do site.
    
    tfcs_data = []
    
    # Exemplo de lógica de extração (ajustar conforme os seletores reais do site)
    # Procuramos as linhas da tabela ou blocos de projeto
    projetos = soup.find_all('tr') # Normalmente os TFCs estão em tabelas <tr>

    for p in projetos:
        colunas = p.find_all('td')
        if len(colunas) >= 3:
            titulo = colunas[0].get_text(strip=True)
            autor = colunas[1].get_text(strip=True)
            orientador = colunas[2].get_text(strip=True)
            
            # Filtro: O enunciado pede apenas 2025
            # Verificamos se "2025" aparece no texto
            if "2025" in p.get_text():
                tfcs_data.append({
                    "titulo": titulo,
                    "autor": autor,
                    "orientador": orientador,
                    "ano": "2025",
                    "resumo": "Extraído via Web Scraping",
                    "link": "https://informatica.ulusofona.pt/..." # Link para o PDF se existir
                })

    # Guardar num ficheiro JSON para o portfólio (como pede o ponto 3 da imagem)
    os.makedirs('data', exist_ok=True)
    with open('data/tfcs_2025.json', 'w', encoding='utf-8') as f:
        json.dump(tfcs_data, f, ensure_ascii=False, indent=4)
        
    print(f"Web Scraping concluído. {len(tfcs_data)} projetos de 2025 guardados em data/tfcs_2025.json")

    # Importar para o Django
    licenciatura = Licenciatura.objects.first()
    for item in tfcs_data:
        TFC.objects.get_or_create(
            nome=item['titulo'],
            licenciatura=licenciatura,
            defaults={
                'autor': item['autor'],
                'orientador': item['orientador'],
                'descricao': item['resumo'],
                'rating': 0 # Ponto 4 da imagem: o teu interesse
            }
        )

if __name__ == "__main__":
    scrape_lusofona_tfcs()