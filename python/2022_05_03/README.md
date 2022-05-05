# 2022_05_03の目標

- Pythonを用いた正規表現の学習
  - 簡単な内容で数値の10桁の判別を行う。
  - またアルファベット10文字の判別を行う。
  - 最後に「●●●-●●●-●●●●」といった電話番号の判別を行う

- 文章を単語区切りでリストに格納するような処理を作成する。
- reのmatchとsplitとfindallを用いたプログラムを作成する。
  - matchに関しては、startメソッドとendメソッドを使用すること

## 正規表現簡単表

最低限正規表現を使用する時に覚えておかないといけないももの

- 正規表現の特殊な文字を表す記号
正規表現の文字 | 意味
------- | -------
\s | 空白
\S | 空白以外
\b | 単語の先頭の空白
\B | 単語の先頭の空白以外の文字列
\w | [a-z,0-9,A-Z]のAsciiコードの文字（_を含む）
\W | [a-z,0-9,A-Z]以外の文字列
\d | 数字（0-9）
\D | 数字以外

- 複数回などの意味を持つ文字

特殊なもの | 意味
------- | -------
? | 空白
\* | 空白以外
+ | 単語の先頭の空白
. | 単語の先頭の空白以外の文字列

## 正規表現の例

```python
# --*--coding:utf-8--*--
import re

str1 = '01234'
# 4文字の数字の連続を含むか判断している
m = re.match(pattern='\d{4}',string = str1)
if bool(m):
    print('4桁の数字を含まない')
else:
    print('4桁の数字を含む')

# 名前のカンマと空白で区切ってリストに格納している
str2 = '安藤, 田中, 佐藤, 吉田'
list1 = re.split(',\s',str2)
print(list1)

# 数字の並びを抽出
str3 = '012-888-919'
list3 = re.findall(pattern='\d+',string=str3)
print(list3)

# ()とsplitを用いた処理
str4 = '123a567b789'
list4 = re.split(pattern='[a-z,A-Z]', string=str4)
print(list4)
list5 = re.split(pattern='([a-z,A-Z])', string=str4)
print(list5)
```

## 参照

基本的な上記の演習が終了したら、下記リンクを読む事
[正規表現のリンク](https://docs.python.org/ja/3/library/re.html)

# 2022_05_04の目標

- pythonを用いたTextI/Oの基本を習得する事
- pythonを用いて、簡単なUnixコマンドを実行すること
  - lsなど
- Excelの簡単な動作プログラムの作成

## 簡単なText I/O まとめ

### pythonにおけるIOとは？

pythonのIOは大きく分けて3つ存在している。BynaryI/O TextI/O RawI/Oのが存在してるが、基本的に業務に使用したいものとしては、TextIOのためTextIOに注視する。

TextIOを用いた、主な作業としては、TextFileをPythonプログラム内でOpenして、編集して、閉じる3つの作業なので、この3作業をどのように行うかを下記する。

- TextファイルのOpen 
  TextファイルをOpenするときには、組み込み関数のOpenを使用する。
- Textファイルの編集
  Textファイルの編集にはwriteメソッドまたはwritelinesメソッドを使用する。
  この二つの違いはwriteメソッドは文字列型を引数にもち、引数の文字列を下記込む動作を行う。writelinesメソッドでは、リストまたは文字列型を引数にもって
  引数を書き込むことができる。（正直なところどっちでもよい）
- Textファイルの閲覧
  Textファイルを閲覧したい時もあると思う（基本的にはTextEditorでみれば良いので正直使用用途はバイナリファイルを見るとき以外ないような気がするが）
  その際にはreadオブジェクトを使用する。
- Textファイルのclose
  TextファイルをOpenしたときには、Fileオブジェクトを閉じるために、closeメソッドを呼び出す必要が必ずある。
  closeを呼び出さないと、メモリを圧迫するだけではなく、最悪の場合、編集の際に実施した処理が保存されないなどの場合が生じる。

### 例
  ```python
  ofile = open('../text_file/sample.html','r')
  for ofile_str in ofile:
    print(ofile_str)
  ofile_str.close()
  ```

### fileモジュールのOpenモード表

modeの文字列 |意味
------- | -------
r | 読み取り専用
w | 書き込み専用（このモードで開いたときは、開いたファイルの過去の書き込みを削除してから開かれる）
a | 追記（開くファイルの過去の書き込みを消したくない際に使用する)

### 課題
- text_file/sample.htmlファイルのbodyメソッドの中身はloremで自動生成した文字列である。bodyメソッドの中身のみを出力するプログラムを作成しなさい
- bodyメソッドの中身の単語数を出力するプログラムを作成しないさい
解答はtext_io_html.pyに記載しているが、単語数のチェックには問題がある。例えば「Mike’s pen」などの場合は正規表現の関係で、3単語としてカウントされてしまう。

## Pythonを用いて、Unixコマンドを使用する

osモジュールをインポートして、そこに記述されているメソッドを使用する

## Openpyxl入門

OpenpyxlとはpythonからExcelの編集を行うことができるフリーのモジュールである。
Excel2010に対応しているが、基本的な動作は2016などにも対応している。

###　課題
- Openpyxlを用いてExcelファイルを作成する
  解答はExcel_make_worksheet.pyのExecute1メソッドに記述する
- Excelの関数の挿入をpythonから行う。
  解答はExcel_make_worksheet.pyのExecute2メソッドに記述する
- コマンドライン上からパス＋キーワードを作成して、grep機能を作成する。
  解答はExcel_make_worksheet.pyのExecute1メソッドに記述する
  解答はExcel_make_worksheet.pyに記載している
- Excelのグラフを作成できるようにする。

### 調べる課題
- セルの着色を変更したい時はどのようにすればよい？(検索ワード Color Cell)
- 罫線を引きたい時はどのようにすればよい（検索ワードBorder)
  - [border_style](https://openpyxl.readthedocs.io/en/latest/api/openpyxl.styles.borders.html?highlight=Border)
- itel_colsとitel_rowsとは？
- delete_colとは？
- worksheet.dimensionとは？（セルの横幅をいじりたい時はどのようにする？）

## pythonを用いてExcelでグラフを作成する方法

一旦飛ばす

## 頭の体操
- カレントディレクトリを取得するプログラムを作成しなさい（フルパス）
- 相対ディレクトリ⇒フルパスにするプログラムを作成しなさい
  解答はmondai.pyに記す。

## selenium入門