import streamlit as st

class KalkulatorTarifMRT:
    def __init__(self, stasiun, tarif_dasar=3000, tarif_per_stasiun=2000):
        # Inisialisasi data stasiun dan tarif
        self.stasiun = stasiun
        self.tarif_dasar = tarif_dasar
        self.tarif_per_stasiun = tarif_per_stasiun

    def hitung_tarif(self, stasiun_awal, stasiun_tujuan):
        # Menghitung jarak berdasarkan posisi stasiun
        index_awal = self.stasiun.index(stasiun_awal)
        index_tujuan = self.stasiun.index(stasiun_tujuan)
        jarak = abs(index_awal - index_tujuan)  # Hitung jumlah stasiun yang dilalui
        return jarak

    def tarif_total(self, stasiun_awal, stasiun_tujuan):
        # Menghitung tarif total berdasarkan jarak
        jarak = self.hitung_tarif(stasiun_awal, stasiun_tujuan)
        if jarak == 0:
            return None  # Jika stasiun awal dan tujuan sama, tarif tidak dihitung
        else:
            return self.tarif_dasar + (jarak - 1) * self.tarif_per_stasiun


def main():
    # Judul aplikasi
    st.title("Kalkulator Tarif MRT Jakarta")

    # Data stasiun MRT
    stasiun = [
        "Lebak Bulus",
    "Fatmawati",
    "Cipete Raya",
    "Haji Nawi",
    "Blok A",
    "Blok M",
    "Asean",
    "Senayan",
    "Istora Mandiri",
    "Bendungan Hilir",
    "Setiabudi Astra",
    "Dukuh Atas",
    "Bundaran HI"
    ]

    # Pilih stasiun awal dan tujuan
    stasiun_awal = st.selectbox("Pilih Stasiun Awal:", stasiun)
    stasiun_tujuan = st.selectbox("Pilih Stasiun Tujuan:", stasiun)

    # Membuat objek KalkulatorTarifMRT
    kalkulator = KalkulatorTarifMRT(stasiun)

    # Hitung tarif saat tombol ditekan
    if st.button("Hitung Tarif"):
        tarif = kalkulator.tarif_total(stasiun_awal, stasiun_tujuan)
        if tarif is None:
            st.error("Stasiun awal dan tujuan tidak boleh sama!")
        else:
            st.success(f"Tarif dari {stasiun_awal} ke {stasiun_tujuan} adalah Rp {tarif}.")

    # Catatan
    st.info("Tarif dihitung berdasarkan tarif dasar dan tambahan per stasiun.")


# Menjalankan aplikasi Streamlit
if __name__ == "__main__":
    main()
