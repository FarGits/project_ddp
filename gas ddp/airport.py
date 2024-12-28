import streamlit as st

# Data bandara dan jarak antar bandara (dalam kilometer)
bandara = {
    "Soekarno-Hatta (Jakarta)": {"Juanda (Surabaya)": 785, "Adisutjipto (Yogyakarta)": 563, "Ahmad Yani (Semarang)": 472, "Kertajati (Majalengka)": 128},
    "Juanda (Surabaya)": {"Soekarno-Hatta (Jakarta)": 785, "Adisutjipto (Yogyakarta)": 327, "Ahmad Yani (Semarang)": 312, "Kertajati (Majalengka)": 657},
    "Adisutjipto (Yogyakarta)": {"Soekarno-Hatta (Jakarta)": 563, "Juanda (Surabaya)": 327, "Ahmad Yani (Semarang)": 118, "Kertajati (Majalengka)": 435},
    "Ahmad Yani (Semarang)": {"Soekarno-Hatta (Jakarta)": 472, "Juanda (Surabaya)": 312, "Adisutjipto (Yogyakarta)": 118, "Kertajati (Majalengka)": 387},
    "Kertajati (Majalengka)": {"Soekarno-Hatta (Jakarta)": 128, "Juanda (Surabaya)": 657, "Adisutjipto (Yogyakarta)": 435, "Ahmad Yani (Semarang)": 387}
}

# Harga per kilometer
harga_per_km = 2000  # Rp

def main():
    st.title("Hitung Tarif Penerbangan Antar Bandara di Pulau Jawa")
    
    # Input form untuk memilih bandara asal dan tujuan
    asal = st.selectbox("Pilih Bandara Asal:", list(bandara.keys()))
    tujuan = st.selectbox("Pilih Bandara Tujuan:", [b for b in bandara.keys() if b != asal])

    # Tombol submit untuk menghitung tarif
    if st.button("Hitung Tarif"):
        # Perhitungan tarif
        jarak = bandara[asal][tujuan]
        tarif = jarak * harga_per_km

        # Menampilkan hasil
        st.success("**Hasil Perhitungan Tarif:**")
        st.write(f"**Bandara Asal:** {asal}")
        st.write(f"**Bandara Tujuan:** {tujuan}")
        st.write(f"**Jarak:** {jarak} km")
        st.write(f"**Tarif:** Rp {tarif:,}")

if __name__ == "__main__":
    main()
