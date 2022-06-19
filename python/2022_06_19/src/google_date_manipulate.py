# --*-- encoding : utf-8 --*--
# pandasのインポート
import pandas
import matplotlib.pyplot as plt

# Dataのインポート
# CSVファイルのインポート
df = pandas.read_csv('../data_src/GOOG.csv')
# Date列の変換
df['Date'] = pandas.to_datetime(df['Date'])
df.info()
# Date列をインデックスにする
df.index = df['Date']
df.head()

# year列とday列とquerter列の追加
df['year'] = df['Date'].dt.year
df['day'] = df['Date'].dt.day
df['quarter'] = df['Date'].dt.quarter

# 各年ごとの平均（会計年度でないから意味がないかもだが）
df.groupby('year').mean()

# Dateの作成
print(pandas.date_range('2022-03-01', '2022-06-01', freq='B'))

plt.plot(df['Date'], df['Open'], 'o')
plt.plot(df['Date'], df['High'], 'o')
plt.plot(df['Date'], df['Low'], 'o')
plt.plot(df['Date'], df['Close'], 'o')

plt.show()
