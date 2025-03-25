# Etapa 6: Processamento de Linguagem Natural (PLN)
import pandas as pd
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Exemplo de texto
df = pd.DataFrame({
    'texto': [
        'Eu amo aprender Python!',
        'Esse conteúdo é horrível.',
        'Estou satisfeita com o progresso.'
    ]
})

# Limpeza e tokenização
stop_words = set(stopwords.words('portuguese'))

def limpar_texto(texto):
    tokens = word_tokenize(texto.lower())
    return ' '.join([t for t in tokens if t.isalpha() and t not in stop_words])

df['texto_limpo'] = df['texto'].apply(limpar_texto)

# Análise de sentimento
df['sentimento'] = df['texto_limpo'].apply(lambda x: TextBlob(x).sentiment.polarity)

print(df)
