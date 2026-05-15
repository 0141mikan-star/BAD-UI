import streamlit as st
import streamlit.components.v1 as components
import uuid

# 1. ページ設定
st.set_page_config(page_title="UI Warp Comparison", layout="centered")

# セッション状態のリセット管理
if 'game_id' not in st.session_state:
    st.session_state['game_id'] = str(uuid.uuid4())

def reset_game():
    st.session_state['game_id'] = str(uuid.uuid4())

# 2. サイドバー
st.sidebar.title("🧪 UI Laboratory")
mode = st.sidebar.radio(
    "どちらのゲームをプレイしますか？",
    ("BAD UI ゲーム", "GOOD UI ゲーム")
)

# --- モード1: BAD UI ゲーム (地獄) ---
if mode == "BAD UI ゲーム":
    st.title("BAD UI 特訓")
    st.write("「小さすぎるバツ」と「勝手にワープする広告」。誤クリックは減点です。")

    bad_code = f"""
    <div id="f" style="position:relative; width:100%; height:600px; background:#f8f9fa; border:3px solid #ddd; border-radius:12px; overflow:hidden; cursor:crosshair; user-select:none;">
        <div id="c" style="position:absolute; width:320px; height:480px; background:#fff; border:4px solid #333; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3); left:50%; top:50%; transform:translate(-50%, -50%); transition:none;">
            <div style="padding:15px; text-align:center; font-family:sans-serif;">
                <div style="background:#f00; color:#fff; display:inline-block; padding:2px 10px; font-weight:bold; margin-bottom:5px;">PR</div>
                <h2 style="color:#1a73e8; margin:10px 0; font-size:20px;">【熊本限定】爆釣の聖地公開！？</h2>
                <p style="font-size:12px; color:#555;">AIが解析した、今すぐ行くべき釣り場TOP10<br><span style="color:#d93025; font-weight:bold;">※公開終了まであと <span id="fake-timer">05</span> 秒</span></p>
                <div style="width:100%; height:180px; background:#ddd; margin:15px 0; display:flex; align-items:center; justify-content:center; border:1px dashed #999;">▶️</div>
                <div style="display:flex; justify-content:center; gap:10px;">
                    <button style="padding:10px 15px; background:#eee; border:1px solid #ccc;">後で見る</button>
                    <button id="s" style="padding:10px 15px; background:#1a73e8; color:#fff; border:none; font-weight:bold; border-radius:5px;">訓練開始</button>
                </div>
            </div>
            <div id="x" style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#ff4b4b; color:#fff; font-size:14px; font-weight:bold; line-height:16px; text-align:center; cursor:pointer; border-radius:2px; display:none;">×</div>
        </div>
        <div style="position:absolute; top:10px; left:10px; background:rgba(0,0,0,0.8); color:#fff; padding:10px; border-radius:5px; font-size:12px; font-family:sans-serif;">
            SCORE: <span id="sc" style="color:#0f0; font-weight:bold;">0</span> | TIME: <span id="t" style="font-weight:bold;">30</span>
        </div>
    </div>
    <script>
        const f=document.getElementById('f'), c=document.getElementById('c'), x=document.getElementById('x'), s=document.getElementById('s'), sce=document.getElementById('sc'), te=document.getElementById('t');
        let score=0, time=30, gI, jI, sz=16;
        function warp() {{
            const mx=f.clientWidth-c.clientWidth-20, my=f.clientHeight-c.clientHeight-20;
            c.style.transform='none'; c.style.left=(Math.random()*mx+10)+'px'; c.style.top=(Math.random()*my+10)+'px';
            if(score>40){{ sz=Math.max(6, 16-Math.floor(score/20)); x.style.width=sz+'px'; x.style.height=sz+'px'; x.style.fontSize=(sz-2)+'px'; x.style.lineHeight=sz+'px'; }}
        }}
        s.onclick=()=>{{
            score=0; time=30; s.style.display='none'; x.style.display='block'; warp();
            gI=setInterval(()=>{{ time--; te.innerText=time; if(time<=0){{ clearInterval(gI); clearInterval(jI); x.style.display='none'; s.style.display='block'; s.innerText="終了:"+score; }} }},1000);
            jI=setInterval(warp, 2500); // 2.5秒ごとに勝手にワープ
        }};
        x.onclick=(e)=>{{ e.stopPropagation(); score+=10; sce.innerText=score; warp(); clearInterval(jI); jI=setInterval(warp, 2500); }};
        c.onclick=(e)=>{{ if(e.target!==x && time>0 && s.style.display==='none'){{ score=Math.max(0,score-5); sce.innerText=score; c.style.borderColor='#f00'; setTimeout(()=>c.style.borderColor='#333',100); }} }};
    </script>
    """
    components.html(bad_code, height=620)

# --- モード2: GOOD UI ゲーム (天国) ---
elif mode == "GOOD UI ゲーム":
    st.title("GOOD UI ゲーム")
    st.write("「巨大なバツ印」と「クリック時のみワープする広告」。ストレスのないワープ体験。")

    good_code = f"""
    <div id="gf" style="position:relative; width:100%; height:550px; background:#e8f0fe; border:3px solid #1a73e8; border-radius:12px; overflow:hidden; user-select:none;">
        
        <div id="ui" style="position:absolute; top:10px; left:10px; background:rgba(255,255,255,0.9); color:#1a73e8; padding:10px 20px; border-radius:30px; font-family:sans-serif; box-shadow:0 2px 10px rgba(0,0,0,0.1); z-index: 1000;">
            <span style="font-weight:bold;">SCORE: <span id="gs">0</span> | TIME: <span id="gt">30</span></span>
        </div>
        
        <button id="gs-btn" style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); padding:20px 40px; font-size:24px; background:#1a73e8; color:#fff; border:none; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 10px 20px rgba(26,115,232,0.3); z-index: 2000;">
            ゲームを開始する
        </button>

        <div id="gc" style="
            position:absolute; width:340px; height:480px; background:#fff; border:4px solid #1a73e8; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1); 
            left:50%; top:50%; transform:translate(-50%, -50%); overflow:visible; display:none; font-family:sans-serif;
            transition: none; /* 滑らかなアニメーションを完全に無効化（ワープ形式） */
        ">
            <div style="padding: 40px 20px 20px 20px; text-align:center;">
                <div style="background:#1a73e8; color:#fff; display:inline-block; padding:2px 10px; font-weight:bold; margin-bottom:5px;">PR</div>
                <h2 id="gtit" style="color:#1a73e8; margin:10px 0; font-size:20px;">誠実な広告</h2>
                <p id="gdes" style="font-size:12px; color:#555; line-height:1.4;">
                    Good UIでは、ワープは「成功した時」にのみ発生します。<br>
                    勝手に場所が変わることはありません。
                </p>
                <div id="gimg" style="width:100%; height:160px; background:#e3f2fd; margin:15px 0; display:flex; align-items:center; justify-content:center; border:1px dashed #1a73e8; border-radius:5px;">
                    <span style="font-size:32px;">😊</span>
                </div>
                <div style="display:flex; justify-content:center; gap:10px;">
                    <button style="padding:10px 15px; background:#f0f2f6; border:1px solid #1a73e8; border-radius:5px;">安心</button>
                    <button style="padding:10px 15px; background:#1a73e8; color:#fff; border:none; border-radius:5px;">安全</button>
                </div>
            </div>

            <div id="gtgt" style="
                position:absolute; width:80px; height:80px; background:#fff; color:#1a73e8; border:4px solid #1a73e8;
                border-radius:50%; display:flex; align-items:center; justify-content:center;
                font-size:36px; font-weight:bold; cursor:pointer;
                right:-25px; top:-25px;
                box-shadow: 0 4px 15px rgba(26,115,232,0.2);
                z-index: 10001;
            ">×</div>
        </div>
        
        <div id="nice" style="position:absolute; bottom:30px; width:100%; text-align:center; font-family:sans-serif; color:#1a73e8; font-size:24px; font-weight:bold; opacity:0; transition:0.3s; pointer-events:none;">Nice Warp!</div>
    </div>

    <script>
        const gf=document.getElementById('gf'), gc=document.getElementById('gc'), gtgt=document.getElementById('gtgt'), gsb=document.getElementById('gs-btn'), gse=document.getElementById('gs'), gte=document.getElementById('gt'), ni=document.getElementById('nice'), gtit=document.getElementById('gtit'), gdes=document.getElementById('gdes'), gimg=document.getElementById('gimg');
        let gsc=0, gt=30, gI;

        const spots = [
            {{ t: "【阿蘇周辺】渓流釣りスポット", d: "豊かな自然の中で、ヤマメやイワナと触れ合える秘密のポイント。初心者も歓迎！", c: "#e0f2f1" }},
            {{ t: "【天草方面】海釣り公園", d: "トイレや売店完備で安心。手軽に色々な魚が釣れる、家族連れに最適なスポット。", c: "#fff8e1" }},
            {{ t: "【球磨川水系】鮎釣りの魅力", d: "日本三大急流の一つ、球磨川で体験する鮎の友釣り。圧巻のスケールとスリル。", c: "#e3f2fd" }}
        ];

        function teleportGood() {{
            const mx = gf.clientWidth - gc.clientWidth - 40;
            const my = gf.clientHeight - gc.clientHeight - 40;
            gc.style.transform = 'none';
            gc.style.left = (Math.random() * mx + 20) + 'px';
            gc.style.top = (Math.random() * my + 20) + 'px';
            
            const s = spots[Math.floor(Math.random() * spots.length)];
            gtit.innerText = s.t; gdes.innerText = s.d; gimg.style.backgroundColor = s.c;
            gtgt.style.transform = 'scale(1)';
        }}

        gsb.onclick=()=>{{
            gsc=0; gt=30; gse.innerText=gsc; gte.innerText=gt; gsb.style.display='none'; gc.style.display='block'; teleportGood();
            gI=setInterval(()=>{{ gt--; gte.innerText=gt; if(gt<=0){{ clearInterval(gI); gc.style.display='none'; gsb.style.display='block'; gsb.innerText="終了:"+gsc+" (再挑戦)"; }} }},1000);
        }};

        gtgt.onclick=()=>{{
            gsc+=100; gse.innerText=gsc;
            gtgt.style.transform='scale(0.8)';
            ni.style.opacity='1'; setTimeout(()=>ni.style.opacity='0', 400);
            teleportGood(); // クリックした瞬間だけパッと移動（ワープ）
        }};
        gtgt.onmouseover=()=>{{ gtgt.style.background='#f1f3f4'; }};
        gtgt.onmouseout=()=>{{ gtgt.style.background='#fff'; }};
    </script>
    """
    components.html(good_code, height=620)

# 3. 完全リセットボタン
st.markdown("---")
if st.button("🔄 ゲーム全体を完全リセット"):
    reset_game()
    st.rerun()
