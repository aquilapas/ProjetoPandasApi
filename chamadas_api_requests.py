# Etapa 5: Consumo de APIs com requests
import requests
import pandas as pd

# GET simples
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    posts = response.json()
    df_posts = pd.DataFrame(posts)
    print(df_posts.head())

# POST simulando envio de dados
payload = {'title': 'Teste', 'body': 'Exemplo de conteúdo', 'userId': 1}
res_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print(res_post.status_code, res_post.json())
