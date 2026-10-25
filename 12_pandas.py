import pandas as pd

df = pd.read_csv('weight-height.csv', sep=';')
print(df)
print(type(df))

print(df.head())
print(df.tail())

print(df['Height'])  # zawsze działa
print(df.Height)     # uproszenie, z niektórymi nazwami nie działa

print(df.Gender.value_counts())
df.Height *= 2.54
df.Weight /= 2.2
print(df)

df['BMI'] = df['Weight'] / df['Height'] / df['Height']
print(df)
del df['BMI']
df.to_csv('weight-height_nowe.csv', index=False)

print(df.shape)
print(f'Liczba wierszy: {df.shape[0]}\nLiczba kolumn: {df.shape[1]}')
print(df.info())
print(df.describe().T.round(2).to_string())

import matplotlib.pyplot as plt
plt.hist(df.query("Gender == 'Male'")['Weight'], bins=50)
# plt.show()
plt.hist(df.query("Gender == 'Female'")['Weight'], bins=50)
plt.show()
