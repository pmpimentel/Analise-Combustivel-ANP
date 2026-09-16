import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("resultados", exist_ok=True)

# voce pode trocar estes valores para analisar outra cidade
uf = "PR"
municipio = "CURITIBA"

conexao = sqlite3.connect("dados/combustiveis.db")

print("\nPRECO MEDIO POR COMBUSTIVEL EM", municipio)

consulta_media = """
SELECT produto, ROUND(AVG(preco), 2) AS preco_medio
FROM precos
WHERE uf = ? AND municipio = ?
GROUP BY produto
ORDER BY preco_medio DESC
"""

media = pd.read_sql_query(
    consulta_media,
    conexao,
    params=(uf, municipio)
)

print(media.to_string(index=False))

print("\nPOSTOS COM GASOLINA MAIS BARATA")

consulta_postos = """
SELECT posto, bandeira, preco
FROM precos
WHERE uf = ?
  AND municipio = ?
  AND produto = 'GASOLINA'
ORDER BY preco ASC
LIMIT 10
"""

postos = pd.read_sql_query(
    consulta_postos,
    conexao,
    params=(uf, municipio)
)

print(postos.to_string(index=False))

#cria um grafico simples
consulta_grafico = """
SELECT data, AVG(preco) AS preco_medio
FROM precos
WHERE uf = ?
  AND municipio = ?
  AND produto = 'GASOLINA'
GROUP BY data
ORDER BY data
"""

grafico = pd.read_sql_query(
    consulta_grafico,
    conexao,
    params=(uf, municipio)
)

conexao.close()

if len(grafico) > 0:
    grafico["data"] = pd.to_datetime(grafico["data"])

    plt.figure(figsize=(9, 5))
    plt.plot(grafico["data"], grafico["preco_medio"], marker="o")
    plt.title("Preco medio da gasolina em " + municipio)
    plt.xlabel("Data")
    plt.ylabel("Preco medio (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("resultados/preco_gasolina.png")
    plt.close()

    print("\nGrafico salvo em resultados/preco_gasolina.png")
else:
    print("\nNao foram encontrados dados de gasolina para essa cidade.")
