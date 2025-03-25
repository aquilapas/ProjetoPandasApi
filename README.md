# Projeto de Estudo com Pandas, Matplotlib, Requests e PLN

Este repositório reúne estudos práticos para aprofundar o conhecimento nas bibliotecas **Pandas**, **Matplotlib**, **Requests** e no uso de **Processamento de Linguagem Natural (PLN)** com Python.

## 📌 Descrição

O projeto foi dividido em etapas práticas que simulam situações reais de manipulação e análise de dados. A cada módulo, novos recursos e bibliotecas são explorados com foco no aprendizado e aplicabilidade no mundo real.

---

## 🎯 Objetivo

- Estudar a biblioteca Pandas com leitura de arquivos variados.
- Aplicar filtros e transformações como `CASE WHEN`.
- Criar gráficos com Matplotlib diretamente de DataFrames.
- Fazer requisições REST usando a biblioteca Requests.
- Desenvolver uma análise básica de sentimento com técnicas de PLN.

---

## 🧩 Etapas do Projeto

### 1️⃣ Leitura de Arquivos
**Arquivo:** `leitura_arquivos.py`
- Carregamento de arquivos nos formatos:
  - `.csv`
  - `.parquet`
  - `.avro`
  - `.txt` com delimitador
- Conversão em DataFrames com Pandas

### 2️⃣ Filtros e Transformações
**Arquivo:** `filtros_transformacoes.py`
- Aplicação de filtros com expressões condicionais
- Seleção de colunas
- Salvamento em arquivo `.parquet`
- Simulação de `CASE WHEN` com `.apply()`

### 3️⃣ Gráficos com Matplotlib
**Arquivo:** `graficos_pandas_matplotlib.py`
- Geração de:
  - Gráfico de barras
  - Gráfico de linha (série temporal)
  - Histograma
- Exportação dos gráficos como imagens PNG

### 4️⃣ Integração com APIs
**Arquivo:** `chamadas_api_requests.py`
- Requisições `GET` e `POST` com `requests`
- Tratamento de respostas
- Conversão em DataFrame

### 5️⃣ Processamento de Linguagem Natural
**Arquivo:** `pln_analise_sentimento.py`
- Tokenização de texto com `nltk`
- Remoção de `stopwords`
- Análise de sentimento com `TextBlob`
- Resultado: polaridade de textos positivos ou negativos

---

## 🧠 Bibliotecas Utilizadas

- `pandas`
- `matplotlib`
- `requests`
- `fastavro`
- `pyarrow`
- `nltk`
- `textblob`

---

## ▶️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/projeto_pandas_api_pln.git
cd projeto_pandas_api_pln
