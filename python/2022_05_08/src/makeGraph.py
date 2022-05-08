import matplotlib.pyplot as plt
import pandas


data = pandas.read_csv('../data/data.csv')
# print(data.abs())
# print(data['date'].type)
data = data.astype({'date': 'datetime64'})
data = data.sort_values('date', ascending=False)
plt.bar(height=data['moveDistance'], x=data['date'])
plt.show()
