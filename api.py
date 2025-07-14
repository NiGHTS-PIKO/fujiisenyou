import requests
import pandas as pd
import time

# ✅ 取得済のGoogle APIキーを入力
API_KEY = ''  # ←ここに実際のAPIキーを入力してください
SEARCH_ENGINE_ID = ''  # ナイツさん専用CSE ID

# 🔍 検索対象語句
keywords = ['最高すぎる', '最低すぎる', '最高', '最低']
results_all = []

for query in keywords:
    print(f'🔍 検索中: {query}')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
        'lr': 'lang_ja',
        'num': 10  # 1回あたり最大10件
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        for item in data.get('items', []):
            results_all.append({
                'keyword': query,
                'title': item.get('title'),
                'link': item.get('link'),
                'snippet': item.get('snippet')
            })
        time.sleep(1.5)  # 優しさのインターバル
    except Exception as e:
        print(f'⚠️ エラー: {query} → {e}')
        time.sleep(2)

# 🗂️ DataFrameに変換・CSV保存
df = pd.DataFrame(results_all)
df.to_csv('search_results_sugiru_style.csv', index=False, encoding='utf-8-sig')
print('✅ 検索結果保存完了！件数:', len(df))
