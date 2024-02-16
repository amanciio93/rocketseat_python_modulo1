# pip install requests => run in terminal

print("\nImportação e uso de um módulo de terceiro: ")
import requests
url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou {response.status_code}")