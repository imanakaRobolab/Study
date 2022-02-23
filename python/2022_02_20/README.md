# 2022_02_20

## 本日の目標

- Pandas の DataFrame を用いて、データを作成する
  テーブル構造は下のようなものを想定している。
  id | height | weight | telephone | calendar
  ---|--------|--------|-----------|---------
  A001| 180| 80| 000-9999-8888| 2022/02/20

- Pandas を用いてデータの生成
  本日作成するデータは在庫管理システム用（仮）のデータを作成することとする。
  今回のデータ構造は特殊で多対多のデータを作成することとする。例えば下記のように。

  **商品**

  | id   | name | category_id | price |
  | ---- | ---- | ----------- | ----- |
  | A001 | Pen1 | C001        | 800   |
  | A001 | Pen1 | C002        | 800   |

  **カテゴリー**<br>

  | id   | category_name |
  | ---- | ------------- |
  | C001 | Stationary    |
  | C002 | Category2     |

  **カテゴリー商品リスト**

  | id   | name | category_id | price | category_name |
  | ---- | ---- | ----------- | ----- | ------------- |
  | A001 | Pen1 | C001        | 800   | Category1     |
  | A001 | Pen1 | C002        | 800   | Category2     |

**注意**：多対多のテーブルを作成する際には商品とカテゴリーを作成してから、カテゴリー商品リストを作成する。

- Python の正規表現をまとめる。