kalkulator_lab/
│
├── app.py               # Script utama (Navigasi)
└── views/
    ├── Kalkulator.py    # Script kalkulator kamu
    └── Panduan.py       # Script info tambahan
    mport streamlit as st

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
import streamlit as st

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>
.main { background-color: #F8FAFC; }
h1, h2, h3 { color: #0F172A; }
.stButton>button {
    background-color: #14B8A6;
    color: black;
    border-radius: 12px;
    border: none;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}
.stButton>button:hover { background-color: #0D9488; color: white; }
div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 15px;
}
div[data-testid="stNumberInput"], div[data-testid="stSelectbox"], div[data-testid="stRadio"] {
    background-color: #FFFFFF;
    border-radius: 10px;
    padding: 5px;
}
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================
st.markdown("<h1 style='text-align: center;'>🧪 Calculator Standardisasi Larutan</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px; color:#475569;'>Kalkulator untuk menghitung konsentrasi Normalitas/Molaritas beserta %RPD hasil standardisasi larutan.</p>", unsafe_allow_html=True)
st.divider()

# =========================================
# DATABASE
# =========================================
database = {
    "Asam Oksalat": {"BM": 126.07, "valensi": 2},
    "Boraks": {"BM": 381.37, "valensi": 2},
    "Kalium Dikromat": {"BM": 294.18, "valensi": 6},
    "CaCO3": {"BM": 100.09, "valensi": 2}
}

# =========================================
# PILIH METODE
# =========================================
metode = st.selectbox(
    "🧪 Pilih Metode Standardisasi",
    ["Alkalimetri", "Asidimetri", "Permanganometri", "Iodometri", "Kompleksometri"]
)

# =========================================
# DATA OTOMATIS
# =========================================
if metode == "Alkalimetri":
    baku, titran, default_massa = "Asam Oksalat", "NaOH", 630
elif metode == "Asidimetri":
    baku, titran, default_massa = "Boraks", "HCl", 500
elif metode == "Permanganometri":
    baku, titran, default_massa = "Asam Oksalat", "KMnO4", 630
elif metode == "Iodometri":
    baku, titran, default_massa = "Kalium Dikromat", "Tiosulfat", 500
elif metode == "Kompleksometri":
    baku, titran, default_massa = "CaCO3", "EDTA", 100

BM = database[baku]["BM"]
valensi = database[baku]["valensi"]

# =========================================
# LAYOUT
# =========================================
col1, col2 = st.columns([1,1])

# =========================================
# INPUT
# =========================================
with col1:
    st.subheader("📥 Input Data")
    massa = st.number_input("Massa standar baku", value=float(default_massa))
    satuan = st.selectbox("Satuan Massa", ["mg", "g"])
    massa_mg = massa * 1000 if satuan == "g" else massa

    st.info(f"Hasil konversi massa = {massa_mg:.2f} mg")
    st.markdown("### ⚗️ Volume Titran")
    vol1 = st.number_input(f"Volume {titran} pertama (mL)", min_value=0.0)
    vol2 = st.number_input(f"Volume {titran} kedua (mL)", min_value=0.0)

    st.markdown("### 🧪 Pengenceran")
    pengenceran = st.radio("Apakah menggunakan pengenceran?", ["Ya", "Tidak"])
    if pengenceran == "Ya":
        volume_total = st.number_input("Volume total pengenceran (mL)", value=100.0)
        volume_pipet = st.number_input("Volume yang dipipet untuk titrasi (mL)", value=25.0)
        FP = volume_total / volume_pipet
    else:
        FP = 1

    st.success(f"Faktor Pengali (FP) = {FP:.2f}")
    st.markdown("### 🧬 Database Otomatis")
    BM_input = st.number_input("BM", value=float(BM))
    valensi_input = st.number_input("Valensi", value=float(valensi))

    if metode != "Kompleksometri":
        BE_input = BM_input / valensi_input
        st.info(f"BE = {BE_input:.4f} mg/mgrek")

    hitung = st.button("🔍 Hitung Sekarang")

# =========================================
# OUTPUT
# =========================================
with col2:
    st.subheader("📤 Output Perhitungan")
    if hitung:
        if vol1 == 0 or vol2 == 0:
            st.error("Volume titran tidak boleh 0")
        else:
            if metode != "Kompleksometri":
                N1 = massa_mg / (FP * vol1 * BE_input)
                N2 = massa_mg / (FP * vol2 * BE_input)
                N_rata = (N1 + N2) / 2
                RPD = abs((N1 - N2) / N_rata) * 100

                st.metric("Normalitas 1", f"{N1:.4f} N")
                st.metric("Normalitas 2", f"{N2:.4f} N")
                st.metric("Rerata Normalitas", f"{N_rata:.4f} N")
                st.metric("%RPD", f"{RPD:.2f}%")

                st.markdown("## 📋 Kesimpulan")
                if RPD < 10:
                    st.success(f"Hasil standardisasi menunjukkan rerata konsentrasi sebesar {N_rata:.4f} N dengan nilai %RPD sebesar {RPD:.2f}%.\n\nPresisi pengujian dinyatakan baik karena %RPD < 10%.")
                else:
                    st.warning(f"Hasil standardisasi menunjukkan rerata konsentrasi sebesar {N_rata:.4f} N dengan nilai %RPD sebesar {RPD:.2f}%.\n\nPresisi pengujian dinyatakan kurang baik karena %RPD > 10%.")

                st.divider()
                st.markdown("## 🧮 Transparansi Perhitungan")
                st.write("### Rumus Berat Ekuivalen")
                st.latex(r'BE = \frac{BM}{Valensi}')
                st.write(f"BE = {BE_input:.4f} mg/mgrek")

                st.write("### Rumus Normalitas")
                st.latex(r'N = \frac{massa\ standar\ baku}{FP \times Volume \times BE}')
                st.write(f"N1 = {N1:.4f} N | N2 = {N2:.4f} N | Rerata = {N_rata:.4f} N")

                st.write("### Rumus %RPD")
                st.latex(r'\%RPD = \left| \frac{X_1 - X_2}{X_{rerata}} \right| \times 100\%')
                st.write(f"%RPD = {RPD:.2f}%")
            else:
                M1 = massa_mg / (FP * vol1 * BM_input)
                M2 = massa_mg / (FP * vol2 * BM_input)
                M_rata = (M1 + M2) / 2
                RPD = abs((M1 - M2) / M_rata) * 100

                st.metric("Molaritas 1", f"{M1:.4f} M")
                st.metric("Molaritas 2", f"{M2:.4f} M")
                st.metric("Rerata Molaritas", f"{M_rata:.4f} M")
                st.metric("%RPD", f"{RPD:.2f}%")

                st.markdown("## 📋 Kesimpulan")
                if RPD < 10:
                    st.success(f"Hasil standardisasi menunjukkan rerata konsentrasi sebesar {M_rata:.4f} M dengan nilai %RPD sebesar {RPD:.2f}%.\n\nPresisi pengujian dinyatakan baik karena %RPD < 10%.")
                else:
                    st.warning(f"Hasil standardisasi menunjukkan rerata konsentrasi sebesar {M_rata:.4f} M dengan nilai %RPD sebesar {RPD:.2f}%.\n\nPresisi pengujian dinyatakan kurang baik karena %RPD > 10%.")
                    import streamlit as st

st.title("📚 Panduan Teori & Prosedur Standardisasi")
st.write("Halaman ini berisi acuan dasar penentuan konsentrasi larutan standar di laboratorium.")

st.divider()

st.header("🔬 Pengertian Dasar")
st.info("""
**Standardisasi** adalah proses penentuan konsentrasi larutan secara akurat menggunakan zat standar primer. 
* **Larutan Standar Primer:** Zat yang memiliki kemurnian tinggi, stabil, dan berat ekuivalen besar (contoh: Asam Oksalat, Boraks).
* **Larutan Standar Sekunder:** Larutan yang konsentrasinya ditentukan melalui titrasi dengan standar primer (contoh: NaOH, HCl).
""")

st.header("🧮 Ketentuan Nilai %RPD")
st.write("""
*Relative Percent Difference* (%RPD) digunakan untuk mengukur tingkat presisi atau kedekatan hasil antara dua kali pengerjaan titrasi (duplo).
* **%RPD < 10%:** Tingkat presisi pengerjaan di lab dinilai **Baik/Diterima**.
* **%RPD ≥ 10%:** Presisi **Kurang Baik**, disarankan melakukan titrasi ulang karena ada perbedaan volume yang cukup jauh antar-titrasi.
