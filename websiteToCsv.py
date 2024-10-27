import requests
from bs4 import BeautifulSoup
import os
import time
import csv
import json
import re
import logging


def get_tag(tagName, className):
    """
    関数の概要: tagの種類とclassを指定して要素を抽出

    引数:
    tag: 置換したい<br> を含むtag
    tagType: tagの種類

    戻り値:
    型: 戻り値の説明

    例:
    >>> function_name(引数の例)
    戻り値の例
    """
    getClassName = className
    getNameTag = soup.find(tagName, class_=getClassName)
    getData = getNameTag.get_text(strip=True)
    return getData


# 各自の環境に応じて編集
logFilePath = '' # logの出力場所
csvFilePath = '' # csvの出力場所
mainUrl = 'https://hogehoge?id='
startIndex = 0 # ID部分のループ（開始）
endIndex = 1 # ID部分のループ（終了）
idFillNumber = 2 # IDを0埋めしたいときの桁数（例：01なら2）
sleepTime = 3 # ループごとの待ち時間（サーバーに負荷をかけないように）


# ロギングの設定
logging.basicConfig(filename=logFilePath, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

error_count = 0 #3になったら次へ（break）
# 処理開始時刻を記録
start_time = time.perf_counter()

for i in range(startIndex, endIndex):
    time.sleep(sleepTime)
    # URLの設定
    url = mainUrl + str(i).zfill(2)   # ここに画像があるWebページのURLを入力
    data = []
    try:
        # ページを取得
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # ここら辺は合わせる
        hoge1 = get_tag('tagName', 'className')
        if(hoge1 is None):
            continue
        hoge2 = get_tag('tagName', 'className')
        if(hoge2 is None):
            continue
        data.append([hoge1,hoge2])

        with open(csvFilePath, 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in data:
                csv_writer.writerow(row)
            logging.info(data)
    except Exception as e:
        logging.error(str(url) + "：エラーが発生しました: %s", e)


# 処理終了時刻を記録
end_time = time.perf_counter()
# 経過時間を計算
elapsed_time = end_time - start_time

print(f"処理にかかった時間: {elapsed_time:.4f} 秒")



