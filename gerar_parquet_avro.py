
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
import os

# Criação de diretório
os.makedirs('dados', exist_ok=True)

# DataFrame de exemplo
df = pd.DataFrame({
    'coluna_exemplo': [50, 120, 80, 200],
    'outra_coluna': ['A', 'B', 'C', 'D']
})

# Caminhos dos arquivos
parquet_path = 'dados/exemplo.parquet'
avro_path = 'dados/exemplo.avro'

# Exportar Parquet
df.to_parquet(parquet_path, index=False)
print(f'Arquivo Parquet criado em: {parquet_path}')

# Exportar Avro
schema = {
    'doc': 'Exemplo de esquema Avro',
    'name': 'Exemplo',
    'namespace': 'example.avro',
    'type': 'record',
    'fields': [
        {'name': 'coluna_exemplo', 'type': 'int'},
        {'name': 'outra_coluna', 'type': 'string'}
    ]
}

records = df.to_dict(orient='records')

with open(avro_path, 'wb') as out:
    fastavro.writer(out, schema, records)

print(f'Arquivo Avro criado em: {avro_path}')
