import streamlit as st

def main():
    # Daftar stasiun LRT
    stasiun_lrt = [
        "Dukuh Atas", "Setiabudi", "Rasuna Said", "Kuningan", "Pancoran", "Cikoko", 
        "Ciliwung", "Cawang", "Halim", "Jatibening Baru", "Cikunir 1", "Cikunir 2", 
        "Bekasi Barat", "Jati Mulya", "TMII", "Kampung Rambutan", "Ciracas", "Harjamukti"
    ]

    # Tarif dasar dan per stasiun
    tarif_dasar = 5000  # Rp
    tarif_per_stasiun = 2000  # Rp

    # Judul aplikasi
    st.title("Kalkulator Tarif LRT Jakarta")
    
    # Input untuk memilih stasiun awal dan tujuan
    stasiun_awal = st.selectbox("Pilih Stasiun Awal:", stasiun_lrt, key="stasiun_awal_lrt")
    stasiun_tujuan = st.selectbox("Pilih Stasiun Tujuan:", [st for st in stasiun_lrt if st != stasiun_awal], key="stasiun_tujuan_lrt")

    # Tombol untuk menghitung tarif
    if st.button("Hitung Tarif", key="tombol_hitung_lrt"):
        # Validasi input
        jarak = 0
        index_awal = stasiun_lrt.index(stasiun_awal)
        index_tujuan = stasiun_lrt.index(stasiun_tujuan)

        # Menggunakan while untuk menghitung jarak
        i = min(index_awal, index_tujuan)
        while i < max(index_awal, index_tujuan):
            jarak += 1
            i += 1

        # Hitung tarif
        tarif_total = tarif_dasar + (jarak - 1) * tarif_per_stasiun

        # Menampilkan hasil
        st.success(f"Tarif dari **{stasiun_awal}** ke **{stasiun_tujuan}** adalah Rp {tarif_total:,}.")

    # Pesan informasi
    st.info("Tarif dihitung berdasarkan tarif dasar Rp 5.000 dan tambahan Rp 2.000 per stasiun yang dilalui.")
