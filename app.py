import streamlit as st
import pandas as pd
from data.database import get_singing_playlist
from components.player_component import render_player

# キャッシュ機能の定義
# ttl=3600 は1時間キャッシュを保持するという意味です
@st.cache_data(ttl=3600)
def get_playlist_cached():
    return get_singing_playlist()

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

all_playlist = get_playlist_cached() # キャッシュ版を呼び出すように変更
if all_playlist:
    # 初期状態として最新順にソートして渡す
    df = pd.DataFrame(all_playlist)
    if not df.empty:
        df = df.sort_values(["date_short", "stream_title", "start"], ascending=[False, False, True])
        all_playlist = df.to_dict('records')
    
    render_player(all_playlist)