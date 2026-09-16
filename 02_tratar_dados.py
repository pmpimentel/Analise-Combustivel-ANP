import pandas as pd

arquivo_entrada = "dados/precos_anp.csv"
arquivo_saida = "dados/precos_tratados.csv"

print("Lendo o arquivo da ANP...")

# a ANP usa ; para separar as colunas.
# o try serve apenas porque alguns arquivos podem usar outra cod de texto.
try:
    dados = pd.read_csv(arquivo_entrada, sep=";", encoding="utf-8-sig")
except UnicodeDecodeError:
    dados = pd.read_csv(arquivo_entrada, sep=";", encoding="latin1")

print("Quantidade de linhas antes do tratamento:", len(dados))

colunas = [
    "Estado - Sigla",
    "Municipio",
    "Revenda",
    "Produto",
    "Data da Coleta",
    "Valor de Venda",
    "Bandeira"
]

dados = dados[colunas]

dados = dados.rename(columns={
    "Estado - Sigla": "uf",
    "Municipio": "municipio",
    "Revenda": "posto",
    "Produto": "produto",
    "Data da Coleta": "data",
    "Valor de Venda": "preco",
    "Bandeira": "bandeira"
})


dados["preco"] = dados["preco"].astype(str).str.replace(",", ".", regex=False)
dados["preco"] = pd.to_numeric(dados["preco"], errors="coerce")

dados["data"] = pd.to_datetime(dados["data"], dayfirst=True, errors="coerce")

dados = dados.dropna(subset=["uf", "municipio", "produto", "data", "preco"])

dados = dados.drop_duplicates()

dados["uf"] = dados["uf"].str.strip().str.upper()
dados["municipio"] = dados["municipio"].str.strip().str.upper()
dados["produto"] = dados["produto"].str.strip().str.upper()

dados.to_csv(arquivo_saida, index=False)

print("Quantidade de linhas depois do tratamento:", len(dados))
print("Arquivo tratado salvo em", arquivo_saida)
print("\nPrimeiras linhas:")
print(dados.head())
