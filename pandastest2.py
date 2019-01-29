import pandas as pd
list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

zipped = list(zip(list_keys, list_values))
data = dict(zipped)

df = pd.DataFrame(data)
print(df.head())