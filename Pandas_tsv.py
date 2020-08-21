import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'    
chipo = pd.read_csv(url, sep = '\t')

print(chipo.info())
print(chipo.head())

# lambda is a way to create fake functions
dollarizer = lambda x: float(x[1:-1])
chipo['item_price'] = chipo['item_price'].apply(dollarizer)

print(chipo.info())
print(chipo.head())