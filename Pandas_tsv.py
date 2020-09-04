import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'    
chipo = pd.read_csv(url, sep = '\t')

print(chipo.info())
print('------------------')

print(chipo.head())
print('------------------')
# lambda is a way to create fake functions
dollarizer = lambda x: float(x[1:-1])
chipo['item_price'] = chipo['item_price'].apply(dollarizer)

print(chipo.info())
print('------------------')

print(chipo.head())
print('------------------')

chipo_avg_order = chipo.groupby('order_id').agg({'item_price':'sum'})
print(chipo_avg_order)
print('------------------')

chipo_avg_order['item_price'].plot(kind='hist',bins=20)
plt.show()