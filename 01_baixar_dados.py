import requests
import os

# link oficial da anp
url = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv"

os.makedirs("dados", exist_ok=True)

print("Baixando os dados da ANP...")

resposta = requests.get(url, timeout=30)
resposta.raise_for_status()

with open("dados/precos_anp.csv", "wb") as arquivo:
    arquivo.write(resposta.content)

print("Download concluido!")
print("Arquivo salvo em dados/precos_anp.csv")
