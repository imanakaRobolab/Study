
import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('./moviedataset.csv')
pandas.set_option('display.max_rows', 10000)
# print(df)
group = df.groupby(by=['Genre'], axis=0)
group2 = df.groupby(by=['Year of release'], axis=0)
# print(group.size())

# group.plot()
# print(group.groups)
# print(group.indices)
# for i in group.__iter__():
#     print(i)
# plt.bar()

# print(group.size().keys())
print(group.size().index)
print(group.size().values)
# plt.bar(x=group.size().index, height=group.size().values)
# plt.show()
print(group['Budget (million $)'].sum())
print(group2.sum())
# plt.plot(group2.sum().index, group2.sum().values)
# plt.show()
