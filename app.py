import streamlit as st
import pandas as pd
import datetime
import time
from data.database import get_singing_playlist
from components.player_component import render_player


# --- サーバー側ログ出力用関数 ---
def log_status(message, level="INFO"):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(f"[{current_time}] [{level}] {message}")

log_status("=== App Sequence Started ===")
boot_start = time.time()

# キャッシュ機能の定義
# ttl=3600 は1時間キャッシュを保持するという意味です
@st.cache_data(ttl=3600)
def get_playlist_cached():
    log_status("Cache missed or expired. Fetching data from database...", "DEBUG")
    data = get_singing_playlist()
    log_status(f"Database query complete. Found {len(data)} items.", "SUCCESS")
    return data

st.set_page_config(
    page_title="aXIs Web Player", 
    page_icon="🦋", 
    layout="wide"
)

st.markdown("""
    <style>
    .block-container { 
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: none !important;
    }
    header, footer { visibility: hidden; height: 0; }
    .stApp { background-color: #0e1117; }
    [data-testid="stVerticalBlock"] > div:first-child {
        margin-top: -20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- データ取得フェーズ ---
try:
    load_start = time.time()
    all_playlist = get_playlist_cached()
    
    if not all_playlist:
        log_status("Playlist is empty after loading!", "WARNING")
    else:
        # データの整合性チェック（最初の1件をサンプルとしてログ出し）
        sample = all_playlist[0]
        log_status(f"Payload ready: {len(all_playlist)} tracks.")
        log_status(f"Sample Check: Title='{sample.get('title')}', Date='{sample.get('date_short')}'", "DEBUG")

except Exception as e:
    log_status(f"Critical error during boot: {str(e)}", "ERROR")
    all_playlist = []

# --- コンポーネント描画フェーズ ---
log_status("Injecting data into Player Component...")
render_player(all_playlist)

boot_end = time.time()
log_status(f"=== App Ready (Total Time: {boot_end - boot_start:.2f}s) ===")