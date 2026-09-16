<div align="center">

# Análise de Preços de Combustíveis via ANP

Trabalho de análise de dados que coleta preços de gasolina e etanol disponibilizados pela ANP, trata os dados com Python, armazena as informações em um banco SQLite e gera consultas e um gráfico para facilitar a análise dos preços em uma cidade.

</div>

---

## Descrição

O projeto utiliza dados públicos da **Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)** para acompanhar preços de combustíveis.

A ideia é transformar o arquivo original da ANP em dados mais fáceis de consultar.

No final, o programa mostra:

* preço médio dos combustíveis na cidade escolhida;
* postos com os menores preços de gasolina;
* gráfico com a evolução do preço médio da gasolina.

Por padrão, a análise está configurada para **Curitiba - PR**, mas a cidade e o estado podem ser alterados no arquivo:

```text
04_analisar_dados.py
```

---

## Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/pmpimentel/Analise-Combustivel-ANP.git
cd Analise-Combustivel-ANP
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute os arquivos na ordem

```bash
python 01_baixar_dados.py
python 02_tratar_dados.py
python 03_salvar_no_banco.py
python 04_analisar_dados.py
```

Ao final, o gráfico será salvo em:

```text
resultados/preco_gasolina.png
```

---

## Como o projeto funciona?

```text
ANP
 │
 ▼
01_baixar_dados.py
Baixa o arquivo CSV
 │
 ▼
02_tratar_dados.py
Limpa e organiza os dados com Pandas
 │
 ▼
03_salvar_no_banco.py
Salva os dados em um banco SQLite
 │
 ▼
04_analisar_dados.py
Executa consultas SQL e gera o gráfico
```
