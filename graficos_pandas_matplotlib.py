# Etapa 4: Gráficos com Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Dataset exemplo
df = pd.DataFrame({
    'categoria': ['A', 'B', 'C'],
    'valores': [10, 20, 15],
    'datas': pd.date_range(start='2025-01-01', periods=3)
})

# Gráfico de barras
plt.figure()
df.plot(kind='bar', x='categoria', y='valores', title='Gráfico de Barras')
plt.savefig('graficos/barra.png')

# Gráfico de linha
plt.figure()
df.plot(kind='line', x='datas', y='valores', title='Gráfico de Linha')
plt.savefig('graficos/linha.png')

# Histograma
plt.figure()
df['valores'].plot(kind='hist', title='Histograma')
plt.savefig('graficos/histograma.png')
