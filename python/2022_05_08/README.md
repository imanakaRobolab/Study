# Streamlit入門

StremlitはPythonのみで、データの可視化等のWebページを作成することのできるモジュールである。
基本的には下記URLに使用方法等が書かれている。
[StreamLitのチュートリアル](https://docs.streamlit.io/library/get-started/main-concepts)

## Streamlitを用いたWebページのはじめ

streamlitモジュールをimportして、writeメソッドを使用することによって、
Web上で文章を表示することができる。

```python
#  --*--coding:utf-8--*--
import streamlit as st
def main():
    st.write('''
    # Hello World
    stream can use markdown syntax.
    ''')
if __name__ == '__main__':
    main()
```

streamlitを起動するときは、他のpythonコードとは異なり、Streamモジュールを介して起動する必要がある。

```
python -m stream run <streamのpythonファイル>
```
streamlitモジュールではPandasのDataFrameクラスを描画することができる。
そのため、下記のようなコードが使用できる。このコードでは、まずDataFrameクラスを作成している。
その際にnumpyのarangeメソッド（組み込み関数rangeメソッドの拡張）で9列のndarrayクラスを作成して、
形を変更して3行3列の行列を作成している。その後、3行3列の行列をstreamlitを用いて出力するような処理を行っている。

```python
import pandas
import numpy
import streamlit as st

# 
df = pandas.DataFrame(data=numpy.arange(9).reshape(
    (3, 3)), columns=['col%d' % i for i in range(3)])
st.write(df)

```
## Streamlitを用いたグラフの作成
Streamlitでは折れ線グラフや棒グラフや円グラフを作成することができる。

基本的には下記処理手順となる
1. グラフのタイトル指定
2. グラフの種類とそれに応じたメソッドを呼び出し、引数にデータをしていする。

```python

```