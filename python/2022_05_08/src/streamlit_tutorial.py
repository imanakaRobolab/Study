#  --*--coding:utf-8--*--

import streamlit as st
import pandas
import numpy


def main():
    st.write('''
    # Hello World
    stream can use markdown syntax.
    ''')
    df = pandas.DataFrame(data=numpy.arange(9).reshape(
        (3, 3)), columns=['col%d' % i for i in range(3)])
    st.write(df)


if __name__ == '__main__':
    main()
