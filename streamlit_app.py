import streamlit as st

# =========================================
# CONFIG PAGE (Harus ada di file utama)
# =========================================
st.set_page_config(
    page_title="Dashboard Standardisasi Larutan",
    page_icon="🧪",
    layout="wide"
)

# Definisi halaman-halaman aplikasi
halaman_kalkulator = st.Page(
    "views/Kalkulator.py", 
    title="Kalkulator Standardisasi", 
    icon="🧮", 
    default=True
)
halaman_panduan = st.Page(
    "views/Panduan.py", 
    title="Panduan & Rumus", 
    icon="📚"
)

# Membuat navigasi di sidebar samping
pg = st.navigation([halaman_kalkulator, halaman_panduan])
pg.run()
