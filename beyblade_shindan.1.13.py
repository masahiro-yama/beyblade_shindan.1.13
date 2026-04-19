import streamlit as st
import random

# ------------------------
# 初期化
# ------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.questions = []

# ------------------------
# 質問データ
# ------------------------
base_questions = [
    ("やすみじかん、なにしてる？", [
        "A 🏃 はしりまわってあそぶ",
        "B 👀 みんなのようすを見てうごく",
        "C 🧩 すわってしずかにあそぶ",
        "D 🎲 きぶんであそびをかえる"
    ]),
    ("ともだちとけんかしたら？", [
        "A 🔥 すぐいいかえす",
        "B 🧠 いちどきいてからはなす",
        "C 😌 あまり気にしない",
        "D 🤝 あいてにあわせてかえる"
    ]),
    ("ゲームでだいじなのは？", [
        "A ⚡ はやくかつこと",
        "B 🛡 まけないこと",
        "C 🔄 さいごまでやること",
        "D 🎯 あいてにあわせること"
    ]),
    ("しゅくだいはどうする？", [
        "A 💨 いっきにおわらせる",
        "B ✏️ ていねいにやる",
        "C 📅 すこしずつやる",
        "D 🎲 きぶんでやりかたをかえる"
    ]),
    ("あたらしいあそびをするときは？", [
        "A 🚀 とりあえずやってみる",
        "B 📖 ルールを見てからやる",
        "C 🐢 ゆっくりなれていく",
        "D 👥 みんなにあわせる"
    ]),
]

extra_questions = [
    ("ヒーローになるなら？", [
        "A 💥 とにかくこうげき",
        "B 🛡 まもりをかためる",
        "C 🔄 さいごまであきらめない",
        "D ⚡ なんでもできる"
    ])
]

def generate_questions():
    q = base_questions.copy()
    q.append(random.choice(extra_questions))
    random.shuffle(q)
    return q

# ------------------------
# 判定
# ------------------------
def get_result(answers):
    count = {"A":0, "B":0, "C":0, "D":0}
    for a in answers:
        count[a] += 1

    max_score = max(count.values())
    top = [k for k, v in count.items() if v == max_score]

    if len(top) > 1:
        return "バランス"

    return {
        "A": "アタック",
        "B": "ディフェンス",
        "C": "スタミナ",
        "D": "バランス"
    }[top[0]]

# ------------------------
# ベイブレードデータ（ここが重要）
# ------------------------
bey_data = {
    "アタック": [
        ("ドランソード", "https://m.media-amazon.com/images/I/6123No2dRdL._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0C52R16P1"),
        ("フェニックスウイング", "https://m.media-amazon.com/images/I/715NtHVPy-L._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0CMZSRJ3Q")
    ],
    "ディフェンス": [
        ("ナイトフォートレス", "https://m.media-amazon.com/images/I/61N7ksTpjhL._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0GMDYS21K"),
        ("レオンクレスト", "https://m.media-amazon.com/images/I/71AMNY-FmqL._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0D91K2WMS")
    ],
    "スタミナ": [
        ("ウィザードアーク", "https://m.media-amazon.com/images/I/61qO6OBNzBL._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0DWSRHP7J"),
        ("クロックミラージュ", "https://m.media-amazon.com/images/I/61kLEYAvp4L._AC_SY450_.jpg", "https://www.amazon.co.jp/%E3%82%BF%E3%82%AB%E3%83%A9%E3%83%88%E3%83%9F%E3%83%BC-TAKARA-TOMY-%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E3%83%96%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%AF%E3%83%AD%E3%83%83%E3%82%AF%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%E3%82%BB%E3%83%AC%E3%82%AF%E3%83%88/dp/B07XBR36N3/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3DPEFXZQZEPW9&dib=eyJ2IjoiMSJ9.fnVkq238v_XiCr01CR2RLfoOKBLBPAqxQ6rCQa_ceoi96OZAri_wmixL9Th-CuHred9gSLm6MXDWj7FYtVvA8ksDITgnKeBKhuDlPUd1FINbcVVJo26TjBB-zN7mFqawNAO4w4sd0AAUAB1HjbPf0GQJn6Dk9fXC-TfnnpToDacXy3LwMhtZLvH_50mKYmxTRwfnhlsSmibC9wHixgUeoWoTsr7bTDxRBiKFWpb5dS98HvdTbS8Lx-EiYmesIG2-UxgVhttwiGcgdIWi0Nz8bUY04hJjZDmzGdL-0ILMWsA.AD5S87EdYAllrr4FNUozEu7JvdU_YYxBnse5dRcipmc&dib_tag=se&keywords=%E3%82%AF%E3%83%AD%E3%83%83%E3%82%AF%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5&qid=1776556097&sprefix=%E3%82%AF%E3%83%AD%E3%83%83%E3%82%AF%E3%83%9F%E3%83%A9%E3%83%BC%E3%82%B8%E3%83%A5%2Caps%2C213&sr=8-2")
    ],
    "バランス": [
        ("エンペラーマイト", "https://m.media-amazon.com/images/I/61WEAT7WNKL._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0FV6Y4MH4"),
        ("スコーピオスピア", "https://m.media-amazon.com/images/I/712keT+tMML._AC_SY450_.jpg", "https://www.amazon.co.jp/dp/B0F47G3QJT")
    ]
}

# ------------------------
# TOP
# ------------------------
if st.session_state.step == 0:
    st.title("🌀 ベイブレードX しんだん")

    # ✅ 修正①：画像追加
    st.image("https://beyblade.takaratomy.co.jp/beyblade-x/guide/_image/guide_keyvisual.png")

    if st.button("▶ スタート！"):
        st.session_state.questions = generate_questions()
        st.session_state.answers = []
        st.session_state.step = 1
        st.rerun()

# ------------------------
# 質問
# ------------------------
elif st.session_state.step <= len(st.session_state.questions):
    q_index = st.session_state.step - 1
    question, options = st.session_state.questions[q_index]

    # ✅ 修正②：進捗バー追加
    st.progress(st.session_state.step / len(st.session_state.questions))

    st.subheader(question)

    for opt in options:
        if st.button(opt):
            st.session_state.answers.append(opt[0])
            st.session_state.step += 1
            st.rerun()

# ------------------------
# 結果
# ------------------------
else:
    result = get_result(st.session_state.answers)

    st.title("🎉 けっか！")
    st.header(f"{result}タイプ！")

    st.write("👇 キミにおすすめのベイブレード！")

    col1, col2 = st.columns(2)

    bey_list = bey_data[result]

    with col1:
        name, img, link = bey_list[0]
        st.image(img)
        st.write(name)
        st.link_button("👉 見てみる", link)

    with col2:
        name, img, link = bey_list[1]
        st.image(img)
        st.write(name)
        st.link_button("👉 見てみる", link)

    if st.button("🔁 もういちどやる"):
        st.session_state.step = 0
        st.rerun()