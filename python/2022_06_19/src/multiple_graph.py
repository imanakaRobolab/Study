import pandas
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import numpy


def main():
    df1 = web.DataReader('GOOG', 'yahoo', start='2021-06-17', end='2022-06-17')
    df2 = web.DataReader('AAPL', 'yahoo', start='2021-06-17', end='2022-06-17')
    df3 = web.DataReader(
        'FB-USD', 'yahoo', start='2021-06-17', end='2022-06-17')
    fig = plt.figure()
    axes1 = fig.add_subplot(2, 2, 1)
    axes1.grid()
    axes2 = fig.add_subplot(2, 2, 2)
    axes3 = fig.add_subplot(2, 2, 3)
    axes4 = fig.add_subplot(2, 2, 4)
    fig.tight_layout()
    axes1.hist(df1['Open'], bins=10)
    axes2.plot(df2.index, df2['Open'])
    axes3.plot(df3.index, df3['Open'])
    axes1.set_title('GOOG')
    axes2.set_title('AAPL')
    axes3.set_title('FB-USD')
    x = numpy.arange(0, 2*numpy.pi, 0.1)
    axes4.plot(x, numpy.sin(x))
    fig.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,
                        wspace=0.35)
    plt.show()


if __name__ == '__main__':
    main()
