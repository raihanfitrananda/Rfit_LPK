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
""")
