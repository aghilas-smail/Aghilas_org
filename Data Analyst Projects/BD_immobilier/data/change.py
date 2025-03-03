import pandas as pd

# df = pd.read_csv('bien.csv', delimiter=';')
                 
# df.to_csv('bien_corr.csv', index=False, sep=',')

df1 = pd.read_csv('vente.csv', delimiter=';')

df1.to_csv('vente_corr.csv', index=False, sep=',')