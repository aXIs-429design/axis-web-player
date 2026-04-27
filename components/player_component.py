import streamlit.components.v1 as components
import json

def render_player(playlist):
    playlist_json = json.dumps(playlist)
    
    html_code = f"""
    <div style="width: 100%; height: 900px; background: #050505; padding: 0 0 40px 0; display: flex; justify-content: center; box-sizing: border-box;">
        <div id="main-layout" style="display: flex; height: 850px; width: calc(100% - 10px); background: #050505; font-family: 'Inter', sans-serif; color: #D1C4E9; overflow: hidden; border: 1px solid #4A148C; border-radius: 12px; box-sizing: border-box; box-shadow: 0 0 25px rgba(123, 31, 162, 0.3);">
            
            <div id="player-side" style="flex: 0 0 65%; padding: 25px; display: flex; flex-direction: column; justify-content: center; border-right: 1px solid #1A0A23; box-sizing: border-box; transition: flex 0.3s ease;">
                <div id="player" style="width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; border: 1px solid #1A0A23;"></div>
                
                <div id="now-playing" style="margin-top: 20px;">
                    <div id="timer-display" style="font-family: 'Courier New', monospace; font-size: 0.7rem; color: #9575CD; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                        <span id="timer-label" style="letter-spacing: 1px;">INITIALIZING...</span>
                        <div style="flex:1; height:2px; background:#1A0A23;"><div id="timer-bar" style="width:0%; height:100%; background:#B287FD; box-shadow: 0 0 8px #7B1FA2; transition: width 0.5s;"></div></div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                        <div style="flex: 1;">
                            <p id="stream-name" 
   onclick="openSourceVideo()" 
   style="font-size: 0.75rem; color: #7B1FA2; margin: 0; font-weight: 700; letter-spacing: 2px; font-family: 'Courier New', monospace; cursor: pointer; display: inline-block; user-select: none;" 
   title="YouTubeで配信画面を開く">
</p>
                            <h2 id="song-title" style="margin: 5px 0; font-size: 1.8rem; font-weight: 800; color: #FFFFFF; text-shadow: 0 0 10px rgba(178, 135, 253, 0.3);">Selecting...</h2>
                            
                            <div style="display: flex; align-items: center; gap: 15px; margin-top: 5px;">
                                <p id="artist-name" style="margin: 0; color: #B287FD; font-size: 1.1rem; font-weight: 500;"></p>
                                <span id="stream-date" style="font-size: 0.75rem; color: #9575CD; font-family: 'Courier New', monospace; border: 1px solid #4A148C; padding: 2px 6px; border-radius: 4px;"></span>
                            </div>
                        </div>
                        <button id="show-list-btn" class="ctrl-btn" onclick="togglePlaylist()" style="display: none; padding: 6px 12px;">SHOW LIST</button>
                    </div>
                </div>
            </div>

            <div id="playlist-side" style="flex: 1; display: flex; flex-direction: column; background: #0D0512; height: 100%; overflow: hidden; box-sizing: border-box; transition: flex 0.3s ease;">
                <div id="filter-area" style="padding: 15px 20px; border-bottom: 1px solid #1A0A23; background: #0D0512; box-sizing: border-box;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <h3 style="color: #9575CD; font-size: 0.6rem; font-weight: 800; margin: 0; letter-spacing: 2px; font-family: 'Courier New', monospace;">SYSTEM.CONTROLS</h3>
                        <div style="display: flex; gap: 4px;">
                            <button class="ctrl-btn" onclick="togglePlayer()" id="tgl-player-btn">HIDE PLAYER</button>
                            <button class="ctrl-btn" onclick="togglePlaylist()">HIDE LIST</button>
                        </div>
                    </div>
                    
                    <input type="text" id="search-input" placeholder="曲名・歌手を検索..." style="width: 100%; box-sizing: border-box; padding: 10px; background: #1A0A23; border: 1px solid #7B1FA2; color: #D1C4E9; border-radius: 6px; outline: none; font-size: 0.8rem; margin-bottom: 12px; transition: 0.3s;">
                    
                    <div class="custom-select-wrapper" id="stream-select-wrapper">
                        <div class="custom-select-trigger" onclick="toggleSelect()">
                            <span id="selected-stream-text">すべての配信から表示</span>
                            <div class="arrow"></div>
                        </div>
                        <div class="custom-options" id="stream-options-container">
                            <div class="custom-option selected" data-value="All" onclick="selectOption('All', 'すべての配信から表示')">すべての配信から表示</div>
                        </div>
                    </div>

                    <div class="filter-section" style="margin-top: 15px;">
                        <div style="color: #9575CD; font-size: 0.6rem; font-weight: 800; margin-bottom: 5px; margin-left: 5px; letter-spacing: 1px; font-family: 'Courier New', monospace;">SYSTEM.SORT_ORDER</div>
                        <div class="custom-select-wrapper" id="sort-select-wrapper">
                            <div class="custom-select-trigger" onclick="toggleSortSelect()">
                                <span id="selected-sort-text">最新順</span>
                                <div class="arrow"></div>
                            </div>
                            <div class="custom-options" id="sort-options-container">
                                <div class="custom-option selected" data-value="newest" onclick="selectSortOption('newest', '最新順')">最新順</div>
                                <div class="custom-option" data-value="oldest" onclick="selectSortOption('oldest', '古い順')">古い順</div>
                                <div class="custom-option" data-value="hot" onclick="selectSortOption('hot', 'おすすめ（盛り上がり順）')">おすすめ（盛り上がり順）</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="playlist-items" style="flex: 1; overflow-y: auto; padding: 10px; box-sizing: border-box; background: #050505;"></div>
            </div>
        </div>
    </div>

    <script>
        var allTracks = {playlist_json};
        var filteredTracks = allTracks;
        var currentIndex = 0;
        var currentKey = null; 
        var player;
        var isPlayerVisible = true;
        var isPlaylistVisible = true;
        var currentFilterVal = "All";
        var trackStartTime = 0;

        if (!window.ytApiLoaded) {{
            var tag = document.createElement('script'); tag.src = "https://www.youtube.com/iframe_api";
            document.getElementsByTagName('script')[0].parentNode.insertBefore(tag, null);
            window.ytApiLoaded = true;
        }}

        window.onYouTubeIframeAPIReady = function() {{ 
            setupFilters(); 
            loadTrack(0); 
            setInterval(monitorPlayback, 800); 
        }};

        function monitorPlayback() {{
            if (!player || typeof player.getCurrentTime !== 'function') return;
            var state = player.getPlayerState();
            if (state === YT.PlayerState.PLAYING || state === YT.PlayerState.BUFFERING) {{
                var currentTime = player.getCurrentTime();
                var t = filteredTracks[currentIndex];
                var endTime = (t && t.end) ? t.end : player.getDuration();

                if (endTime > 0 && endTime > t.start) {{
                    var remaining = Math.max(0, Math.floor(endTime - currentTime));
                    document.getElementById('timer-label').innerText = "NEXT IN: " + remaining + "s";
                    document.getElementById('timer-bar').style.width = Math.min(100, (currentTime / endTime) * 100) + "%";

                    if (remaining <= 0.8 && (Date.now() - trackStartTime > 3000)) {{
                        loadTrack(currentIndex + 1);
                    }}
                }} else {{
                    document.getElementById('timer-label').innerText = "LIVE / CALIBRATING...";
                }}
            }}
        }}

        window.loadTrack = function(index) {{
            if (filteredTracks.length === 0 || index >= filteredTracks.length) return;
            
            currentIndex = index;
            var t = filteredTracks[index];
            currentKey = t.video_id + t.start; 
            trackStartTime = Date.now();
            
            document.getElementById('song-title').innerText = t.title;
            document.getElementById('artist-name').innerText = t.artist || "";
            document.getElementById('stream-name').innerText = "SOURCE: " + t.stream_title;
            // 配信日を代入
            document.getElementById('stream-date').innerText = t.date_short;

            if (!player) {{
                player = new YT.Player('player', {{
                    height: '100%', width: '100%', videoId: t.video_id,
                    playerVars: {{ 'start': t.start, 'autoplay': 0, 'controls': 1, 'rel': 0 }},
                    events: {{ 'onStateChange': (e) => {{ if(e.data == YT.PlayerState.ENDED) loadTrack(currentIndex+1); }} }}
                }});
            }} else {{
                player.loadVideoById({{ videoId: t.video_id, startSeconds: t.start }});
            }}
            renderPlaylist();
        }};

        window.openSourceVideo = function() {{
    var t = filteredTracks[currentIndex];
    if (t && t.video_id) {{
        var url = "https://www.youtube.com/watch?v=" + t.video_id + "&t=" + t.start + "s";
        window.open(url, '_blank');
    }}
}};

        window.toggleSelect = function() {{
            var wrapper = document.getElementById('stream-select-wrapper');
            wrapper.classList.toggle('open');
            document.getElementById('sort-select-wrapper').classList.remove('open');
        }};

        window.toggleSortSelect = function() {{
            var wrapper = document.getElementById('sort-select-wrapper');
            wrapper.classList.toggle('open');
            document.getElementById('stream-select-wrapper').classList.remove('open');
        }};

        window.selectOption = function(val, text) {{
            currentFilterVal = val;
            document.getElementById('selected-stream-text').innerText = text;
            var options = document.querySelectorAll('#stream-options-container .custom-option');
            options.forEach(opt => opt.classList.remove('selected'));
            event.currentTarget.classList.add('selected');
            applyFilters();
            document.getElementById('stream-select-wrapper').classList.remove('open');
            event.stopPropagation();
        }};

        window.selectSortOption = function(val, text) {{
            document.getElementById('selected-sort-text').innerText = text;
            var options = document.querySelectorAll('#sort-options-container .custom-option');
            options.forEach(opt => opt.classList.remove('selected'));
            event.currentTarget.classList.add('selected');
            sortTracks(val);
            document.getElementById('sort-select-wrapper').classList.remove('open');
            event.stopPropagation();
        }};

        window.sortTracks = function(type) {{
            if (type === 'newest') {{
                allTracks.sort((a, b) => b.date_short.localeCompare(a.date_short) || b.stream_title.localeCompare(a.stream_title) || (a.start - b.start));
            }} else if (type === 'oldest') {{
                allTracks.sort((a, b) => a.date_short.localeCompare(b.date_short) || a.stream_title.localeCompare(b.stream_title) || (a.start - b.start));
            }} else if (type === 'hot') {{
                allTracks.sort((a, b) => (Number(b.density) || 0) - (Number(a.density) || 0));
            }}
            applyFilters();
        }};

        function applyFilters() {{
            var q = document.getElementById('search-input').value.toLowerCase();
            var streamVal = currentFilterVal;
            filteredTracks = allTracks.filter(t => {{
                var matchSearch = t.title.toLowerCase().includes(q) || (t.artist && t.artist.toLowerCase().includes(q));
                var matchStream = (!streamVal || streamVal === "All") || (t.date_short + " │ " + t.stream_title === streamVal);
                return matchSearch && matchStream;
            }});
            if (currentKey) {{
                var foundIndex = filteredTracks.findIndex(t => (t.video_id + t.start) === currentKey);
                currentIndex = foundIndex;
            }}
            renderPlaylist();
        }}

        function setupFilters() {{
            var container = document.getElementById('stream-options-container');
            var streamMap = new Map();
            allTracks.forEach(t => {{ var key = t.date_short + " │ " + t.stream_title; streamMap.set(key, true); }});
            Array.from(streamMap.keys()).sort().reverse().forEach(key => {{
                var div = document.createElement('div');
                div.className = 'custom-option';
                div.innerText = key;
                div.onclick = (e) => selectOption(key, key);
                container.appendChild(div);
            }});
            document.getElementById('search-input').addEventListener('input', () => applyFilters());
        }}

        function renderPlaylist() {{
            var container = document.getElementById('playlist-items');
            if (!container) return;
            var html = "";
            filteredTracks.forEach((item, i) => {{
                var itemKey = item.video_id + item.start;
                var isActive = (itemKey === currentKey); 
                html += `<div onclick="loadTrack(${{i}})" class="playlist-row ${{isActive ? 'active-track' : ''}}">
                    <span class="track-index">${{i + 1}}</span>
                    <div class="track-info-container">
                        <span class="track-name">${{item.title}}</span>
                        <div class="track-details">
                            <div>${{item.date_short}}</div>
                            <div class="stream-title-sub">${{item.stream_title}}</div>
                        </div>
                    </div>
                </div>`;
            }});
            container.innerHTML = html + '<div style="height:120px;"></div>';
        }}

        window.togglePlayer = function() {{
            var playerSide = document.getElementById('player-side');
            var btn = document.getElementById('tgl-player-btn');
            if (isPlayerVisible) {{
                playerSide.style.display = 'none'; btn.innerText = 'SHOW PLAYER';
                if (!isPlaylistVisible) togglePlaylist();
            }} else {{
                playerSide.style.display = 'flex'; btn.innerText = 'HIDE PLAYER';
            }}
            isPlayerVisible = !isPlayerVisible;
        }};

        window.togglePlaylist = function() {{
            var pls = document.getElementById('playlist-side'); var ps = document.getElementById('player-side'); var btn = document.getElementById('show-list-btn');
            if (isPlaylistVisible) {{
                pls.style.display = 'none'; ps.style.flex = '0 0 100%'; ps.style.borderRight = 'none'; btn.style.display = 'block';
                if (!isPlayerVisible) togglePlayer();
            }} else {{
                pls.style.display = 'flex'; ps.style.flex = '0 0 65%'; ps.style.borderRight = '1px solid #1A0A23'; btn.style.display = 'none';
            }}
            isPlaylistVisible = !isPlaylistVisible;
        }};
    </script>

    <style>
        * {{ box-sizing: border-box; }}
        .ctrl-btn {{ background-color: #1A0A23; color: #B287FD; border: 1px solid #7B1FA2; border-radius: 4px; font-size: 0.55rem; padding: 3px 6px; cursor: pointer; transition: 0.3s; font-family: 'Courier New', monospace; letter-spacing: 1px; }}
        .ctrl-btn:hover {{ border: 1px solid #B287FD; box-shadow: 0 0 10px #7B1FA2; color: #FFFFFF; }}
        #search-input:focus {{ border-color: #B287FD !important; box-shadow: 0 0 8px rgba(123, 31, 162, 0.5); }}
        .playlist-row {{ display: flex; align-items: flex-start; padding: 12px 15px; cursor: pointer; border-bottom: 1px solid #0D0512; margin-bottom: 2px; border-radius: 4px; transition: 0.2s; background: #050505; }}
        .playlist-row:hover {{ background: #1A0A23; border-color: #7B1FA2; }}
        .track-index {{ flex: 0 0 35px; font-size: 0.7rem; color: #4A148C; margin-top: 2px; font-family: 'Courier New', monospace; }}
        .track-name {{ font-size: 0.85rem; color: #D1C4E9; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block; }}
        .active-track {{ background: #1A0A23 !important; border-left: 3px solid #B287FD; box-shadow: inset 0 0 10px rgba(123, 31, 162, 0.2); }}
        .active-track .track-index {{ color: #B287FD; text-shadow: 0 0 5px #7B1FA2; }}
        .active-track .track-name {{ color: #FFFFFF; font-weight: bold; }}
        .track-details {{ font-size: 0.65rem; max-height: 0; opacity: 0; overflow: hidden; transition: 0.3s ease; color: #9575CD; }}
        .playlist-row:hover .track-details {{ max-height: 120px; opacity: 1; margin-top: 6px; }}
        .stream-title-sub {{ color: #7B1FA2; opacity: 0.8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; transition: 0.2s; }}
        .playlist-row:hover .stream-title-sub {{ white-space: normal; color: #9575CD; }}
        .custom-select-wrapper {{ position: relative; width: 100%; user-select: none; }}
        .custom-select-trigger {{ padding: 10px 12px; background: #1A0A23; border: 1px solid #7B1FA2; border-radius: 6px; font-size: 0.75rem; color: #B287FD; cursor: pointer; display: flex; justify-content: space-between; align-items: center; min-height: 38px; }}
        .custom-options {{ position: absolute; top: 100%; left: 0; right: 0; background: #0D0512; border: 1px solid #7B1FA2; border-top: none; z-index: 100; display: none; max-height: 300px; overflow-y: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.8); }}
        .open .custom-options {{ display: block; }}
        .custom-option {{ padding: 10px 12px; font-size: 0.75rem; color: #9575CD; cursor: pointer; border-bottom: 1px solid #1A0A23; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        .custom-option:hover {{ background: #1A0A23; color: #FFFFFF; white-space: normal; overflow: visible; }}
        .custom-option.selected {{ color: #B287FD; background: #1A0A23; font-weight: bold; }}
        .arrow {{ width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 5px solid #4A148C; transition: 0.3s; }}
        .open .arrow {{ transform: rotate(180deg); border-top-color: #B287FD; }}
        #playlist-items::-webkit-scrollbar, .custom-options::-webkit-scrollbar {{ width: 6px; }}
        #playlist-items::-webkit-scrollbar-track, .custom-options::-webkit-scrollbar-track {{ background: #050505; }}
        #playlist-items::-webkit-scrollbar-thumb, .custom-options::-webkit-scrollbar-thumb {{ background: #4A148C; border-radius: 10px; }}
        #playlist-items::-webkit-scrollbar-thumb:hover, .custom-options::-webkit-scrollbar-thumb:hover {{ background: #7B1FA2; }}
        /* styleタグの中に追加 */
#stream-name:hover {{
    color: #B287FD !important;
    text-decoration: underline;
}}
    </style>
    """
    return components.html(html_code, height=900)