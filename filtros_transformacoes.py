# Etapa 2: Filtros e seleção
import pandas as pd

# Carregando CSV para exemplo
df = pd.read_csv('dados/exemplo.csv')

# Filtro e seleção
filtro = df[df['coluna_exemplo'] > 100][['coluna_exemplo', 'outra_coluna']]

# Salvando como parquet
filtro.to_parquet('dados/filtrado.parquet')

# Etapa 3: Transformações estilo "CASE WHEN"
df['classificacao'] = df['coluna_exemplo'].apply(lambda x: 'Alto' if x > 100 else 'Baixo')

print(df[['coluna_exemplo', 'classificacao']].head())
