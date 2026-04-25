import streamlit as st
from data.database import get_singing_playlist
from components.player_component import render_player

st.set_page_config(
    page_title="aXIs Web Player", 
    page_icon="🦋", 
    layout="wide"
)

st.markdown("""
    <style>
    /* block-container の上部パディングを 0 に近い値まで削る */
    .block-container { 
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0rem !important;  /* 横の余白：ここをお好みで調整 */
        padding-right: 0rem !important; /* 横の余白：ここをお好みで調整 */
        max-width: none !important;
    }
    header, footer { visibility: hidden; height: 0; }
    .stApp { background-color: #0e1117; }
    
    /* 画面上部の謎の隙間（stVerticalBlockの余白）を消す */
    [data-testid="stVerticalBlock"] > div:first-child {
        margin-top: -20px !important;
    }
    </style>
""", unsafe_allow_html=True)

all_playlist = get_singing_playlist()
if all_playlist:
    render_player(all_playlist)