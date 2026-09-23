import requests

URL_BASE = "http://localhost:8000"

print("--- Testando a API Calculadora ---")

# Testando a rota raiz
resposta_raiz = requests.get(f"{URL_BASE}/")
print(f"Raiz (Status {resposta_raiz.status_code}): {resposta_raiz.json()}")

# Testando a Soma (20 + 35 )
resposta_soma = requests.get(f"{URL_BASE}/somar/20/35")
print(f"Soma (Status {resposta_soma.status_code}): {resposta_soma.json()}")

# Testando a Divisão por zero
resposta_erro = requests.get(f"{URL_BASE}/dividir?a=10&b=0")
print(f"Divisão por zero (Status {resposta_erro.status_code}): {resposta_erro.json()}")