import pandas as pd
import sqlite3

print("Lendo os dados tratados...")

dados = pd.read_csv("dados/precos_tratados.csv")

print("Abrindo o banco SQLite...")

conexao = sqlite3.connect("dados/combustiveis.db")

dados.to_sql(
    "precos",
    conexao,
    if_exists="replace",
    index=False
)

conexao.close()

print("Dados salvos no banco!")
print("Banco criado em dados/combustiveis.db")
