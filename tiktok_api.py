import os
import requests
from dotenv import load_dotenv

load_dotenv()

SESSIONID = os.getenv("SESSIONID")
USERNAME = os.getenv("USERNAME") or "your_tiktok_username"

HEADERS = {
    "Cookie": f"sessionid={SESSIONID}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_total_views():
    url = f"https://www.tiktok.com/@{USERNAME}"
    res = requests.get(url, headers=HEADERS)
    if "SIGI_STATE" not in res.text:
        raise Exception("Gagal mengambil data. Cek SESSIONID atau USERNAME.")
    data_str = res.text.split("SIGI_STATE=")[1].split(";</script>")[0]
    import json
    data = json.loads(data_str)
    items = data.get("ItemModule", {})
    return sum(item.get("stats", {}).get("playCount", 0) for item in items.values())

def update_tiktok_bio(bio_text):
    url = "https://www.tiktok.com/passport/web/account/update_profile/"
    res = requests.post(url, data={"bio_description": bio_text}, headers=HEADERS)
    if res.status_code == 200:
        print("✅ Bio berhasil diupdate!")
    else:
        print("❌ Gagal update bio:", res.text)
