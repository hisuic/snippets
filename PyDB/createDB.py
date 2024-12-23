import pandas as pd
import sqlite3

# エクセルファイルとシート名
excel_file = "" # エクセルファイル名 e.g. filename.xlsx
sheet_name = "" # 読み込むシート名 e.g. sheet1

# SQLite3データベースファイル名
db_file = "" # Output db file name e.g. database.db
table_name = "words"  # 作成するテーブル名

# エクセルデータを読み込む
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# データ型の変換（1列目をint型に、2列目と3列目をtext型に変換）
df.columns = ["word_id", "word", "meaning"]  # 列名を設定
df["word_id"] = df["word_id"].astype(int)   # 主キー用にint型に変換

# SQLite3データベースに保存
with sqlite3.connect(db_file) as conn:
    # テーブルを作成（主キーの指定を含む）
    conn.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        word_id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        meaning TEXT NOT NULL
    )
    """)

    # データを挿入（データの競合を避けるため置き換え）
    df.to_sql(table_name, conn, if_exists="replace", index=False)

print(f"エクセルファイルの内容がSQLite3データベース {db_file} に保存されました。")

