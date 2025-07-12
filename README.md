# Bio TikTok Auto Updater (Total Views Version)

Script ini secara otomatis menghitung total views dari semua video pada akun TikTok kamu, lalu mengupdate bagian bio TikTok dengan angka tersebut.

## 🚀 Fitur
- Mengambil total view dari semua video TikTok.
- Mengupdate bio TikTok secara otomatis.
- Tidak menggunakan browser atau Selenium.
- Menggunakan TikTok Web API tidak resmi (`requests` based).

## 📦 Struktur Folder
```
Bio_Tiktok_API_Total_Views/
├── main.py
├── tiktok_api.py
├── .env
├── requirements.txt
└── README.md
```

## 🛠️ Cara Penggunaan

1. Clone repositori ini atau download ZIP:
```bash
git clone https://github.com/nama_kamu/Bio_Tiktok_API_Total_Views.git
cd Bio_Tiktok_API_Total_Views
```

2. Install dependency:
```bash
pip install -r requirements.txt
```

3. Atur file `.env`:
```
SESSIONID=isi_dengan_sessionid_anda
USERNAME=username_tiktok_kamu
```

4. Jalankan script:
```bash
python main.py
```

## ⚠️ Catatan
- Script ini **tidak resmi** dari TikTok.
- Gunakan dengan bijak untuk akun pribadi.
- Gagal update bio bisa karena TikTok rate limit atau session kedaluwarsa.
