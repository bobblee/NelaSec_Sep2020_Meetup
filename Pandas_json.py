import pandas as pd
from pandas.io.json import json_normalize
import xlsxwriter

url = 'https://fakerapi.it/api/v1/persons?'
person = pd.read_json(url)

print(person.info())
print('------------------')

print(person.head())
print('------------------')

person_flat = json_normalize(person['data'])
print(person_flat)
print('------------------')

person_flat.to_csv('person_flat.csv')
person_flat.to_excel('person_flat.xlsx', engine = 'xlsxwriter')
# Pandas also has a to_sql for the database folks