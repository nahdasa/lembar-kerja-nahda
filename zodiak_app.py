import streamlit as st
from datetime import datetime
import random
import calendar
import matplotlib.pyplot as plt

# MEMBUAT CONFIG
st.set_page_config(page_title="Mengecek Zodiak", page_icon="🪐", layout="centered")

# MEMBUAT STYLE CSS 
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #ffe6f0, #ffffff);
        color: #4d004d;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h1, h2, h3, h4 {
        color: #cc3399;
    }
    .stButton > button {
        background-color: #ff66b3;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 8px 20px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #e0559c;
    }
    .stSelectbox, .stDateInput {
        background-color: #ffe6f0 !important;
        border-radius: 10px;
        color: #4d004d;
    }
    .css-1v3fvcr {
        background-color: #ffe6f0 !important;
        border-radius: 10px;
        color: #4d004d;
    }
    </style>
""", unsafe_allow_html=True)

# ISI DATA SEMUA JENIS ZODIAK
deskripsi = {
    "Aries": "Penuh semangat, percaya diri, dan suka tantangan.",
    "Taurus": "Stabil, setia, dan menyukai kenyamanan.",
    "Gemini": "Ceria, pintar berkomunikasi, dan penuh rasa ingin tahu.",
    "Cancer": "Peka, perhatian, dan penyayang.",
    "Leo": "Karismatik, berani, dan suka jadi pusat perhatian.",
    "Virgo": "Perfeksionis, analitis, dan suka membantu.",
    "Libra": "Adil, harmonis, dan cinta keindahan.",
    "Scorpio": "Intens, misterius, dan sangat fokus.",
    "Sagittarius": "Petualang, jujur, dan optimis.",
    "Capricorn": "Ambisius, pekerja keras, dan disiplin.",
    "Aquarius": "Inovatif, mandiri, dan suka hal unik.",
    "Pisces": "Penuh imajinasi, sensitif, dan penuh kasih."
}

love_match = {
    "Aries": "Leo, Sagittarius",
    "Taurus": "Virgo, Capricorn",
    "Gemini": "Libra, Aquarius",
    "Cancer": "Scorpio, Pisces",
    "Leo": "Aries, Sagittarius",
    "Virgo": "Taurus, Capricorn",
    "Libra": "Gemini, Aquarius",
    "Scorpio": "Cancer, Pisces",
    "Sagittarius": "Aries, Leo",
    "Capricorn": "Taurus, Virgo",
    "Aquarius": "Gemini, Libra",
    "Pisces": "Cancer, Scorpio"
}

ramalan_harian = [
    "Hari ini cocok untuk memulai hal baru 🌱",
    "Seseorang mungkin sedang memikirkan kamu 💌",
    "Fokuslah pada dirimu sendiri hari ini ✨",
    "Rejeki tak terduga akan datang 🔮",
    "Cinta bisa tumbuh dari persahabatan 💕"
]

# MENENTUKAN FUNGSI
def get_zodiac(day, month):
    if   (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20): return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittarius"
    else: return "Capricorn"

# MEMBUAT HEADER
st.markdown("""
    <div style='background-color:#fff0f5; padding: 25px; border-radius: 15px; text-align:center;'>
        <h1 style='color:#cc3399;'>✨ Zodiak Harian by Nahda ✨</h1>
        <p style='color:#800040;'>Temukan zodiak, cinta & ramalan harimu hari ini</p>
    </div>
""", unsafe_allow_html=True)

# MENGINPUT
st.subheader("🗖️ Masukkan Tanggal Lahirmu:")

tahun = st.selectbox("Tahun", list(range(2000, 2026)), index=10)
bulan_nama = list(calendar.month_name)[1:]
bulan_dict = {nama: i+1 for i, nama in enumerate(bulan_nama)}
bulan = st.selectbox("Bulan", bulan_nama)
jumlah_hari = calendar.monthrange(tahun, bulan_dict[bulan])[1]
hari = st.selectbox("Hari", list(range(1, jumlah_hari+1)))

tanggal = datetime(tahun, bulan_dict[bulan], hari)

# HASIL
if tanggal:
    zodiak = get_zodiac(tanggal.day, tanggal.month)

    st.markdown(f"### 💫 Zodiak Kamu: **{zodiak}**")
    st.markdown(f"#### ✨ Kepribadian:")
    st.info(deskripsi[zodiak])

    st.markdown("#### ❤️ Cocok dengan:")
    st.success(love_match[zodiak])

    st.markdown("#### 🔮 Ramalan Hari Ini:")
    st.warning(random.choice(ramalan_harian))

    # CHART
    # For demo, show a bar chart of all zodiac and some random popularity scores
    st.markdown("### 📊 Popularitas Zodiak")
    zodiac_names = list(deskripsi.keys())
    popularity_scores = [random.randint(20, 100) for _ in zodiac_names]

    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(zodiac_names, popularity_scores, color="#ff66b3")
    ax.set_ylabel("Skor Popularitas")
    ax.set_title("Popularitas Zodiak")

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='#4d004d', fontweight='bold')

    st.pyplot(fig)

# FOOTER
st.markdown("""
    <hr style='border: 1px solid #ffb3d9;'/>
    <p style='text-align: center; font-size: small; color: gray;'>✨ Dibuat oleh Nahda ✨</p>
""", unsafe_allow_html=True)