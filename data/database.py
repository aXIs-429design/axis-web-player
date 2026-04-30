import sqlite3
import os
import csv

def get_singing_playlist():
    # パスの設定
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(os.getcwd(), 'utawaku.db')
    csv_path = os.path.join(base_dir, 'song_durations.csv')

    # 1. CSVから曲の長さを読み込む
    song_durations = {}
    if os.path.exists(csv_path):
        # quotechar='"' を指定することで、"..." 内のカンマを無視します
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f, skipinitialspace=True, quotechar='"')
            for row in reader:
                try:
                    # 曲名にカンマがあっても、row['title'] に正しく入ります
                    title = row['title'].strip()
                    song_durations[title] = int(row['duration_sec'])
                except (ValueError, KeyError):
                    continue

    # 2. データベース接続
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    # XIDENに絞り込み
    # database.py 内の SQLを修正
    sql = """
    SELECT DISTINCT
        m.title, 
        m.artist, 
        s.stream_title, 
        s.published_at,
        l.stream_id as video_id, 
        l.start_time as start,
        l.density
    FROM t_singing_logs l
    JOIN m_contents m ON l.content_id = m.content_id
    JOIN t_streams s ON l.stream_id = s.stream_id
    /*WHERE m.artist = 'XIDEN' */
    WHERE m.category = 'Singing'
    ORDER BY s.published_at DESC, l.start_time ASC
    """
    
    cur.execute(sql)
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()

    # 3. 終了時間の計算 (開始秒数 + 曲の長さ + 10秒)
    playlist = []
    for row in rows:
        db_title = row['title'].strip() # DB側の空白対策
        duration = song_durations.get(db_title, 240) # 念のためdb_titleで検索
        row['end'] = row['start'] + duration + 10
        # 配信日から日付（先頭10文字）だけを抽出して新しくキーを作る
        row['date_short'] = row['published_at'][:10] if row['published_at'] else "Unknown"
        playlist.append(row)
        
    return playlist