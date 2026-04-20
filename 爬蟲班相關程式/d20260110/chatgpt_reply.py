import time
import random
import requests
import json
import csv
from typing import Optional

# ---------- 可調參數 ----------
DATE = "20200109"               # 要抓的日期（可改）
TABLE_INDEX = 6                 # 原本你取第七個資訊 -> index 6
CSV_FILENAME = "每日收盤行情.csv"

# User-Agent 範例清單（可自行補充更多）
UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36"
]

# URL 模板（_ 參數會是時間戳記或隨機數）
URL_TEMPLATE = "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date}&type=MS&response=json&_={ts}"
# ---------- end 可調參數 ----------

def make_headers() -> dict:
    ua = random.choice(UA_LIST)
    headers = {
        'User-Agent': ua,
        'Accept-Language': 'zh-TW,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1'
    }
    return headers

def fetch_json_with_retries(date: str, attempts: int = 3, min_sleep: float = 1.0, max_sleep: float = 3.0) -> Optional[dict]:
    """
    使用 Session，隨機 UA、時間戳記參數，並在失敗時重試（含遞增延遲）。
    回傳解析後的 JSON（dict），若全部失敗回傳 None。
    """
    session = requests.Session()
    for attempt in range(1, attempts + 1):
        # 每次嘗試都更新 headers（包含隨機 UA）
        headers = make_headers()
        session.headers.update(headers)

        # 使用毫秒時間戳記（也可以改成 random.randint(...) 來產生隨機）
        ts = int(time.time() * 1000)
        url = URL_TEMPLATE.format(date=date, ts=ts)

        # 在發 request 前短暫隨機等待（避免太快連續請求）
        sleep_before = random.uniform(min_sleep, max_sleep)
        print(f"[嘗試 {attempt}/{attempts}] 等待 {sleep_before:.2f}s 後向 {url} 發出請求（User-Agent: {session.headers['User-Agent'][:60]}...）")
        time.sleep(sleep_before)

        try:
            resp = session.get(url, timeout=15)
            resp.raise_for_status()
            # 嘗試直接解析 JSON
            data = resp.json()
            print(f"[嘗試 {attempt} 成功] HTTP {resp.status_code}，已解析 JSON，時間戳記 = {ts}")
            return data
        except requests.exceptions.RequestException as e:
            # 網路/狀態錯誤
            print(f"[嘗試 {attempt} 失敗] RequestException: {e}")
        except ValueError as e:
            # JSON 解析錯誤
            print(f"[嘗試 {attempt} 失敗] JSON decode error: {e}")

        # 若還有下一次嘗試，等待更長一點的隨機時間（退避）
        if attempt < attempts:
            backoff = random.uniform(min_sleep * attempt, max_sleep * attempt)
            print(f"  -> 重新嘗試前再等待 {backoff:.2f}s")
            time.sleep(backoff)

    print("已達最大重試次數，無法取得資料。")
    return None

def main():
    jsontext = fetch_json_with_retries(DATE, attempts=3, min_sleep=1.0, max_sleep=2.5)
    if jsontext is None:
        return

    # 防守性檢查：確認 tables 存在且長度足夠
    tables = jsontext.get('tables', [])
    if not isinstance(tables, list) or len(tables) <= TABLE_INDEX:
        print(f"錯誤：回傳的 JSON 裡沒有第 {TABLE_INDEX} 個 table (總共 {len(tables)} 個)。請檢查 date 或 API 回傳。")
        # 若想要看完整 JSON 的 keys 以便 debug，可以取消下一行註解
        # print(json.dumps(jsontext, ensure_ascii=False)[:2000])
        return

    table = tables[TABLE_INDEX]
    title = table.get('title', '')
    field = table.get('fields', [])
    data = table.get('data', [])

    if not field:
        print("警告：fields 為空，請檢查 API 回傳結構。")
    if not data:
        print("警告：data 為空（抓不到資料）。")

    # 寫入 CSV
    with open(CSV_FILENAME, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        # 如果 field 不是 list，先嘗試處理
        if isinstance(field, list):
            writer.writerow(field)
        else:
            writer.writerow([str(field)])
        for row in data:
            writer.writerow(row)
    print(f"已成功寫入：{CSV_FILENAME} (title: {title})")

if __name__ == "__main__":
    main()
