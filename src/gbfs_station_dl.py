import json
import requests
import pandas as pd
from io import StringIO

# URLへアクセスしてデータを取得
# url = requests.get("https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_information.json")
# url = requests.get("https://api-public.odpt.org/api/v4/gbfs/docomo-cycle/station_information.json")
url = requests.get("https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json")

text = url.text

# JSONデータを読み込む
data = json.loads(text)

# ネスト（入れ子）構造になっている"data"という項目を展開する
df_json = pd.json_normalize(data['data']['stations'])

# JSONをCSVへ変換して文字コードをutf8で出力
# df_json.to_csv("docomo_cycle_tokyo_station.csv", encoding='utf8', index=False)
# df_json.to_csv("docomo_cycle_station.csv", encoding='utf8', index=False)
df_json.to_csv("hellocycling_station.csv", encoding='utf8', index=False)

print('処理終了')
