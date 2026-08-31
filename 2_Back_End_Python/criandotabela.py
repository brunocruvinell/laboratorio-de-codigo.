import pandas as pd
# DataFrame é uma estrutua de dados,semelhante a uma tabela.
dados = {
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [23, 31, 29]
}

df = pd.DataFrame(dados)
print(df)