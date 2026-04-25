# 🦋 aXIs Web Player ⛓

XIDENさんの歌唱配信（歌枠）を、より深く、シームレスに楽しむための非公式Webプレイヤー。
データベースに基づいた楽曲管理と、ストレスのない自動遷移機能を提供します。

## ◢ Overview
このプロジェクトは、YouTubeの歌唱ログをアーカイブし、独自のインターフェースで再生することを目的に開発されました。
UIはXIDENさんをイメージしネオンパープルのアクセントで構築されています。

## ◢ Features
- **Seamless Transition**: 歌唱終了時刻に合わせて次の楽曲へ自動スキップ。
- **Database Integration**: SQLite3 (`utawaku.db`) による楽曲・配信データの集中管理。
- **Gothic-Mode UI**: 没入感を高めるフルワイド・ダークモードインターフェース。
- **Custom Search**: アーティストやタイトルに基づいたフィルタリング機能。

## 🛠 Tech Stack
- **Language**: Python
- **Framework**: Streamlit
- **Database**: SQLite3
- **API**: YouTube IFrame Player API
- **Styling**: Custom CSS (Gothic-Modern Style)

## ◢ Setup & Installation

```bash
# リポジトリのクローン
git clone [https://github.com/あなたのユーザー名/axis-web-player.git](https://github.com/あなたのユーザー名/axis-web-player.git)
cd axis-web-player

# ライブラリのインストール
pip install -r requirements.txt

# アプリの起動
streamlit run app.py