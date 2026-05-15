import streamlit as st
import streamlit.components.v1 as components
import uuid

# 1. ページ設定
st.set_page_config(page_title="UI Comparison Game Lab", layout="centered")

# セッション状態でゲームのリセットを管理
if 'game_id' not in st.session_state:
    st.session_state['game_id'] = str(uuid.uuid4())

def reset_game():
    st.session_state['game_id'] = str(uuid.uuid4())

# 2. サイドバー
st.sidebar.title("🧪 UI Laboratory")
mode = st.sidebar.radio(
    "どちらのゲームをプレイしますか？",
    ("👹 地獄の BAD UI ゲーム", "✨ 天国の GOOD UI ゲーム")
)

# --- モード1: BAD UI ゲーム (ストレス特訓) ---
if mode == "👹 地獄の BAD UI ゲーム":
    st.title("👹 地獄の BAD UI 特訓")
    st.write("「小さすぎるバツ印」と「ワープする広告」に耐えられるか。")

    bad_code = f"""
    <div id="f" style="position:relative; width:100%; height:600px; background:#f8f9fa; border:3px solid #ddd; border-radius:12px; overflow:hidden; cursor:crosshair; user-select:none;">
        <div id="c" style="position:absolute; width:320px; height:480px; background:#fff; border:4px solid #333; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3); left:50%; top:50%; transform:translate(-50%, -50%); transition:none;">
            <div style="padding:15px; text-align:center; font-family:sans-serif;">
                <div style="background:#f00; color:#fff; display:inline-block; padding:2px 10px; font-weight:bold; margin-bottom:5px;">PR</div>
                <h2 style="color:#1a73e8; margin:10px 0; font-size:20px;">【熊本限定】爆釣の聖地公開！？</h2>
                <div style="width:100%; height:180px; background:#ddd; margin:15px 0; display:flex; align-items:center; justify-content:center; border:1px dashed #999;">▶️</div>
                <button id="s" style="padding:10px 15px; background:#1a73e8; color:#fff; border:none; font-weight:bold; cursor:pointer; border-radius:5px;">訓練開始</button>
            </div>
            <div id="x" style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#ff4b4b; color:#fff; font-size:14px; font-weight:bold; line-height:16px; text-align:center; cursor:pointer; border-radius:2px; display:none; font-family:Arial,sans-serif;">×</div>
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
            jI=setInterval(warp, 2500);
        }};
        x.onclick=(e)=>{{ e.stopPropagation(); score+=10; sce.innerText=score; warp(); clearInterval(jI); jI=setInterval(warp, 2500); }};
        c.onclick=(e)=>{{ if(e.target!==x && time>0 && s.style.display==='none'){{ score=Math.max(0,score-5); sce.innerText=score; c.style.borderColor='#f00'; setTimeout(()=>c.style.borderColor='#333',100); }} }};
    </script>
    """
    components.html(bad_code, height=620)

# --- モード2: GOOD UI ゲーム (癒やし体験) ---
# 文字の被りを修正（パディング調整）、広告全体が穏やかに動くアニメーションを追加した修正版
elif mode == "天国の GOOD UI ゲーム":
    st.title("✨ 天国の GOOD UI ゲーム")
    st.write("「押しやすさ」を極めたデザイン。ターゲットは大きく、誠実な広告全体が穏やかに動き、常にユーザーを尊重します。")

    # CSSアニメーション：広告全体をゆっくり動かします
    move_ad_gently_keyframes = """
    @keyframes moveAdGently {
        0%   { left: 0%; top: 20px; } /* 左端、上端（バツのはみ出しを考慮） */
        25%  { left: calc(100% - 320px); top: 20px; } /* 右端 */
        50%  { left: calc(100% - 320px); top: calc(100% - 480px); } /* 右下 */
        75%  { left: 0%; top: calc(100% - 480px); } /* 左下 */
        100% { left: 0%; top: 20px; }
    }
    """

    good_code = f"""
    <div id="gf" style="position:relative; width:100%; height:550px; background:#e8f0fe; border:3px solid #1a73e8; border-radius:12px; overflow:hidden; user-select:none;">
        <div id="ui" style="position:absolute; top:10px; left:10px; background:rgba(255,255,255,0.9); color:#1a73e8; padding:10px 20px; border-radius:30px; font-family:sans-serif; box-shadow:0 2px 10px rgba(0,0,0,0.1);">
            <span style="font-weight:bold;">SCORE: <span id="gs">0</span> | TIME: <span id="gt">30</span></span>
        </div>
        
        <button id="gs-btn" style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); padding:20px 40px; font-size:24px; background:#1a73e8; color:#fff; border:none; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 10px 20px rgba(26,115,232,0.3); z-index: 200;">
            ゲームを開始する
        </button>

        <div id="moving-container-good" style="
            position: absolute;
            width: 320px;
            height: 480px;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            user-select: none;
            cursor: crosshair;
            animation: moveAdGently 25s infinite linear running; /* Good UI用にゆっくり */
            display: none; /* 開始まで非表示 */
            z-index: 100;
        ">
            <div id="ad-card-good" style="
                position: relative;
                width: 100%;
                height: 100%;
                background-color: #fff;
                border: 4px solid #1a73e8;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                overflow: hidden;
                font-family: sans-serif;
                padding: 20px 80px 20px 20px; /* 文字が被らないように右側に余白を作る（80px） */
            ">
                <div style="padding:15px; text-align:center;">
                    <div style="background:#1a73e8; color:#fff; display:inline-block; padding:2px 10px; font-weight:bold; margin-bottom:5px;">PR</div>
                    <h2 id="ad-title-good" style="color:#1a73e8; margin:10px 0; font-size:20px;">【熊本限定】爆釣の聖地公開！？</h2>
                    <p id="ad-desc-good" style="font-size:12px; color:#555;">AIが解析した、今週末おすすめ釣り場TOP10。熊本の豊かな海と川の魅力をお届け。</p>
                    
                    <div id="ad-image-good" style="width:100%; height:180px; background:#ddd; margin:15px 0; display:flex; align-items:center; justify-content:center; border:1px dashed #1a73e8; border-radius: 5px;">
                        <span style="font-size:32px;">▶️</span>
                    </div>

                    <div style="display:flex; justify-content:center; gap:10px;">
                        <button style="padding:10px 15px; background:#f0f2f6; border:1px solid #1a73e8; cursor:pointer; color: #1a73e8; border-radius: 5px;">後で見る</button>
                        <button style="padding:10px 15px; background:#1a73e8; color:#fff; border:none; font-weight:bold; cursor:pointer; border-radius: 5px;">詳細をチェック</button>
                    </div>
                </div>

                <div id="gtgt" style="
                    position:absolute; width:80px; height:80px; background:#fff; color:#1a73e8; border:4px solid #1a73e8;
                    border-radius:50%; display:flex; align-items:center; justify-content:center;
                    font-size:36px; font-weight:bold; cursor:pointer;
                    transition: transform 0.1s;
                    box-shadow: 0 4px 15px rgba(26,115,232,0.2);
                    right: -20px; top: -20px; /* 広告カードからはみ出して配置 */
                    font-family: Arial, sans-serif;
                    z-index: 10001;
                ">×</div>
            </div>
        </div>
        
        <div id="nice" style="position:absolute; bottom:30px; width:100%; text-align:center; font-family:sans-serif; color:#1a73e8; font-size:24px; font-weight:bold; opacity:0; transition:0.3s; pointer-events:none; z-index: 10;">Good Click!</div>
    </div>
    <style>
        /* CSSの波括弧を {{ }} に修正、アニメーションを追加 */
        {move_ad_gently_keyframes}
    </style>
    <script>
        const gf=document.getElementById('gf'), movingContainerGood=document.getElementById('moving-container-good'), adCardGood=document.getElementById('ad-card-good'), gtgt=document.getElementById('gtgt'), gsb=document.getElementById('gs-btn'), gse=document.getElementById('gs'), gte=document.getElementById('gt'), ni=document.getElementById('nice'), adTitleGood=document.getElementById('ad-title-good'), adDescGood=document.getElementById('ad-desc-good'), adImageGood=document.getElementById('ad-image-good');
        let gsc=0, gt=30, gI;

        // 釣り場情報の配列
        const fishingSpots = [
            {{ title: "【熊本限定】爆釣の聖地公開！？", desc: "AIが解析した、今週末おすすめ釣り場TOP10。熊本の豊かな海と川の魅力をお届け。", imageColor: "#ddd" }},
            {{ title: "【阿蘇周辺】癒しの渓流釣りスポット", desc: "豊かな自然の中で、ヤマメやイワナと触れ合える秘密のポイント。初心者も歓迎！", imageColor: "#e0f2f1" }},
            {{ title: "【天草方面】海釣り公園でファミリーフィッシング", desc: "トイレや売店完備で安心。手軽に色々な魚が釣れる、家族連れに最適なスポット。", imageColor: "#fff8e1" }},
            {{ title: "【球磨川水系】鮎釣りの魅力に迫る", desc: "日本三大急流の一つ、球磨川で体験する鮎の友釣り。圧巻のスケールとスリル。", imageColor: "#e3f2fd" }}
        ];

        // 広告コンテンツを変更する関数
        function changeContent() {{
            const spot = fishingSpots[Math.floor(Math.random() * fishingSpots.length)];
            adTitleGood.innerText = spot.title;
            adDescGood.innerText = spot.desc;
            adImageGood.style.backgroundColor = spot.imageColor;
            gtgt.style.transform='scale(1)';
        }}

        gsb.onclick=()=>{{
            gsc=0; gt=30; gse.innerText=gsc; gte.innerText=gt; gsb.style.display='none'; 
            movingContainerGood.style.display='block'; /* アニメーションさせる親コンテナを表示 */
            changeContent();
            gI=setInterval(()=>{{ gt--; gte.innerText=gt; if(gt<=0){{ clearInterval(gI); 
            movingContainerGood.style.display='none'; /* 終了時に親コンテナを非表示 */
            gsb.style.display='block'; gsb.innerText="終了:"+gsc+" (再挑戦)"; }} }},1000);
        }};

        // バツボタンクリック時の処理 (コンテンツ切り替え)
        gtgt.onclick=()=>{{
            gsc+=100; gse.innerText=gsc;
            gtgt.style.transform='scale(0.8)';
            ni.style.opacity='1'; setTimeout(()=>ni.style.opacity='0', 400);
            setTimeout(changeContent, 200);
        }};
        gtgt.onmouseover=()=>gtgt.style.background='#f1f3f4';
        gtgt.onmouseout=()=>gtgt.style.background='#fff';
    </script>
    """
    components.html(good_code, height=620)

# 3. 完全リセットボタン（全モード共通）
st.markdown("---")
if st.button("🔄 ゲーム全体を完全リセット"):
    reset_game()
    st.rerun()

# 4. サイドバー下部の解説
st.sidebar.markdown("---")
st.sidebar.write("**【今回の改善点】**")
st.sidebar.write("* バツ印を赤い四角の中に文字として配置しました（Bad UIモード）。")
st.sidebar.write("* リセットボタンを独立させ、UUIDによる強制再読み込みを実装しました。")
st.sidebar.write("* **Good UIモードで文字が隠れる問題を修正し、広告全体が穏やかに動くアニメーションを追加しました。**")
