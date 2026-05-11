import streamlit as st
import streamlit.components.v1 as components
import uuid

# 1. ページ全体の共通設定
st.set_page_config(page_title="UI Comparison Lab", layout="centered")

# セッション状態でBad UI側のリセット用IDを管理
if 'game_id' not in st.session_state:
    st.session_state['game_id'] = str(uuid.uuid4())

# リセット処理
def reset_bad_game():
    st.session_state['game_id'] = str(uuid.uuid4())

# 2. サイドバーでメニューを選択
st.sidebar.title("🛠 UI Laboratory")
mode = st.sidebar.radio(
    "体験するモードを選択してください",
    ("BAD UI", "GOOD UI")
)

# --- 項目1: BAD UI (ワープする・バツが小さい・文字が怪しい) ---
if mode == "BAD UI":
    st.title("BAD UI ゲーム")
    st.write("ユーザーを欺き、ストレスを与え、誤クリックを誘発する最悪の体験です。")

    bad_game_code = f"""
    <div id="game-field" style="position:relative; width:100%; height:600px; background:#f8f9fa; border:3px solid #ddd; border-radius:12px; overflow:hidden; cursor:crosshair; user-select:none;">
        <div id="ad-card" style="position:absolute; width:320px; height:480px; background:#fff; border:4px solid #333; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3); overflow:hidden; transition:none; left:50%; top:50%; transform:translate(-50%, -50%);">
            <div style="padding:15px; text-align:center; font-family:sans-serif;">
                <div style="background:#f00; color:#fff; display:inline-block; padding:2px 10px; font-weight:bold; margin-bottom:5px;">PR</div>
                <h2 style="color:#1a73e8; margin:10px 0; font-size:20px;">【熊本限定】爆釣の聖地公開！？</h2>
                <p style="font-size:12px; color:#555;">AIが解析した釣り場TOP10<br><span style="color:#d93025; font-weight:bold;">※公開終了まであと <span id="timer">05</span> 秒</span></p>
                <div style="width:100%; height:180px; background:#ddd; margin:15px 0; display:flex; align-items:center; justify-content:center; border:1px dashed #999; border-radius:5px;">
                    <span style="font-size:32px;">▶️</span>
                </div>
                <div style="display:flex; justify-content:center; gap:10px;">
                    <button style="padding:10px 15px; background:#eee; border:1px solid #ccc; cursor:pointer;">後で見る</button>
                    <button id="start-btn" style="padding:10px 15px; background:#1a73e8; color:#fff; border:none; font-weight:bold; cursor:pointer; border-radius:5px;">訓練開始</button>
                </div>
            </div>
            <div id="close-btn" style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#ff4b4b; color:#fff; font-size:14px; font-weight:bold; line-height:16px; text-align:center; z-index:10000; cursor:pointer; border-radius:2px; display:none; font-family:Arial,sans-serif;">×</div>
        </div>
        <div style="position:absolute; top:10px; left:10px; z-index:10; background:rgba(0,0,0,0.8); color:#fff; padding:10px; border-radius:5px; font-size:12px; font-family:sans-serif;">
            SCORE: <span id="score" style="color:#0f0; font-size:18px; font-weight:bold;">0</span> | TIME: <span id="time" style="font-size:18px; font-weight:bold;">30</span>
        </div>
    </div>
    <script>
        const field = document.getElementById('game-field');
        const card = document.getElementById('ad-card');
        const close = document.getElementById('close-btn');
        const start = document.getElementById('start-btn');
        let score = 0, timeLeft = 30, gInt, jInt, size = 16;
        function warp() {{
            const mx = field.clientWidth - card.clientWidth - 20, my = field.clientHeight - card.clientHeight - 20;
            card.style.transform = 'none'; card.style.left = (Math.random()*mx+10)+'px'; card.style.top = (Math.random()*my+10)+'px';
            if(score>40){{ size=Math.max(6, 16-Math.floor(score/20)); close.style.width=size+'px'; close.style.height=size+'px'; close.style.fontSize=(size-2)+'px'; close.style.lineHeight=size+'px'; }}
        }}
        start.onclick = () => {{
            score=0; timeLeft=30; start.style.display='none'; close.style.display='block'; warp();
            gInt = setInterval(()=>{{ timeLeft--; document.getElementById('time').innerText=timeLeft; if(timeLeft<=0){{ clearInterval(gInt); clearInterval(jInt); close.style.display='none'; start.style.display='block'; start.innerText="終了 Score:"+score; }} }}, 1000);
            jInt = setInterval(warp, 2500);
        }};
        close.onclick = (e) => {{ e.stopPropagation(); score+=10; document.getElementById('score').innerText=score; warp(); clearInterval(jInt); jInt=setInterval(warp, 2500); }};
        card.onclick = (e) => {{ if(e.target!==close && timeLeft>0 && start.style.display==='none'){{ score=Math.max(0,score-5); document.getElementById('score').innerText=score; card.style.borderColor='#f00'; setTimeout(()=>card.style.borderColor='#333',100); }} }};
    </script>
    """
    components.html(bad_game_code, height=620)
    
    if st.button("ゲーム全体を完全リセット"):
        reset_bad_game()
        st.rerun()

# --- 項目2: GOOD UI (明確・予測可能・安心) ---
elif mode == "GOOD UI":
    st.title("✅ GOOD UI ")
    st.write("ユーザーの目的を尊重し、安心感とスムーズな操作を提供する誠実な体験です。")

    good_ui_code = """
    <div style="display:flex; justify-content:center; align-items:center; width:100%; height:500px; background:#f0f2f6; border-radius:12px; font-family:sans-serif;">
        <div style="position:relative; width:350px; background:#fff; padding:30px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.05); text-align:center;">
            <button id="g-close" title="閉じる" style="position:absolute; top:12px; right:12px; width:44px; height:44px; background:#f1f3f4; border:none; border-radius:50%; cursor:pointer; font-size:20px; color:#5f6368; transition:0.2s; display:flex; align-items:center; justify-content:center;">✕</button>
            <script>
                const btn = document.getElementById('g-close');
                btn.onmouseover = () => { btn.style.background = '#e8eaed'; btn.style.color = '#202124'; };
                btn.onmouseout = () => { btn.style.background = '#f1f3f4'; btn.style.color = '#5f6368'; };
                btn.onclick = () => alert('誠実なUI：このボタンは常にここにあり、押しやすいサイズです。');
            </script>
            <div style="margin-top:10px;">
                <div style="color:#1a73e8; font-weight:bold; margin-bottom:10px;">アクセシビリティ対応済</div>
                <h3 style="margin:0 0 10px; color:#202124;">心地よいデザイン</h3>
                <p style="font-size:14px; color:#5f6368; line-height:1.6;">
                    Good UIは、ユーザーに「探させる」「焦らせる」といった負担を一切かけません。
                </p>
                <div style="margin:20px 0; padding:15px; background:#e8f0fe; border-radius:8px; font-size:13px; color:#1967d2; text-align:left;">
                    💡 <b>ここがGood：</b><br>
                    ・バツボタンが44px以上のサイズ（標準規格）<br>
                    ・ホバー時に視覚的な変化がある<br>
                    ・閉じる機能が明確に独立している
                </div>
                <button style="width:100%; padding:14px; background:#1a73e8; color:#fff; border:none; border-radius:8px; font-weight:bold; cursor:pointer; transition:0.2s;" onmouseover="this.style.background='#174ea6'" onmouseout="this.style.background='#1a73e8'">
                    詳細を見る
                </button>
            </div>
        </div>
    </div>
    """
    components.html(good_ui_code, height=520)

# 3. 解説（サイドバー下部）
st.sidebar.markdown("---")
st.sidebar.caption("DS（データサイエンス）の現場でも、ダッシュボードの使いやすさは分析効率を左右する重要な要素です。")
