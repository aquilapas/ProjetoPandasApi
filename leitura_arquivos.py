# Etapa 1: Leitura de diferentes formatos
import pandas as pd
import fastavro

# CSV
df_csv = pd.read_csv('dados/exemplo.csv')

# Parquet
df_parquet = pd.read_parquet('dados/exemplo.parquet')

# TXT delimitado por tabulação
df_txt = pd.read_csv('dados/exemplo.txt', delimiter='\t')

# Avro
with open('dados/exemplo.avro', 'rb') as f:
    reader = fastavro.reader(f)
    df_avro = pd.DataFrame([r for r in reader])

# Impressão inicial para validação
print(df_csv.head())
print(df_parquet.head())
print(df_txt.head())
print(df_avro.head())
