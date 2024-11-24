print("\nImportação e uso de um módulo de terceiros")

import requests

url = "https://www.example.com"

response = requests.get(url)

print(f"Status code: {response.status_code}")
