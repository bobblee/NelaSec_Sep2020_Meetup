import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv'
cars2 = pd.read_csv(url)

print('------------------')

# Info gives Column Count, Row Count, Column Names, number of "Not Null" fields, Data Tpee
print(cars2.info())
print('------------------')

# describe gives basic descriptive statistics for the columns in the datafame
print(cars2.describe())
print('------------------')
## include = 'all' also adds details on non-numberic fields
print(cars2.describe(include='all'))
print('------------------')

# head(x) is used to peak at the first x number of records
## if no value is provided 10 records are shown
print(cars2.head())
print('------------------')

# tail(x) is similar to head, but shows the last records
print(cars2.tail(5))
print('------------------')

# Select by column value (equal)
print(cars2[cars2['car'] == 'volkswagen rabbit custom diesel'])
print('------------------')

#Select by column value (equal)
print(cars2[cars2['mpg']>40])
print('------------------')

#Select by an index value
print(cars2.iloc[[196,111]])
print('------------------')