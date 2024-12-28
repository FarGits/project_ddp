class KRLFareCalculatorBogorLine:
    def __init__(self):
        # Data jarak stasiun dalam kilometer untuk Bogor Line
        self.station_distances = {
            "Bogor": 0,
            "Cilebut": 6,
            "Bojonggede": 10,
            "Citayam": 15,
            "Depok": 20,
            "Depok Baru": 22,
            "Pondok Cina": 26,
            "Universitas Indonesia": 25,
            "Universitas Pancasila": 27,
            "Lenteng Agung": 30,
            "Tanjung Barat": 32,
            "Pasar Minggu": 34,
            "Pasar Minggu Baru": 36,
            "Duren Kalibata": 38,
            "Cawang": 40,
            "Tebet": 42,
            "Manggarai": 45,
            "Cikini": 58,
            "Gondangdia": 59,
            "Juanda": 62,
            "Sawah Besar": 62,
            "Mangga Besar": 63,
            "Jayakarta": 64,
            "Jakarta Kota": 60,
            "Cikarang": 78,
            "Metland Telaga Murni": 75,
            "Cibitung": 72,
            "Tambun": 67,
            "Bekasi Timur": 63,
            "Bekasi": 61,
            "Kranji": 62,
            "Cakung": 60,
            "Klender Baru": 56,
            "Buaran": 54,
            "Klender": 54,
            "Jatinegara": 54,
            "Mantraman": 45,
            "Sudirman": 48,
            "Bni City": 59,
            "Karet": 36,
            "Tanah Abang": 60,
            "Duri": 65,
            "Angke": 67,
            "Pondok Jati": 54,
            "Kramat": 57,
            "Gang Sentiong": 52,
            "Pasar Senen": 55,
            "Kemayoran": 61,
            "Rajawali": 63
        }
        self.base_fare = 3000  # Tarif dasar (Rp)
        self.additional_fare = 1000  # Tarif tambahan per 10 km
        self.min_distance = 25  # Batas minimum jarak (km)

    def calculate_fare(self, start_station, end_station):
        # Validasi stasiun
        start_station = start_station.strip().title()
        end_station = end_station.strip().title()

        if start_station not in self.station_distances or end_station not in self.station_distances:
            return "Stasiun tidak ditemukan."

        # Menghitung jarak
        start_distance = self.station_distances[start_station]
        end_distance = self.station_distances[end_station]
        distance = abs(end_distance - start_distance)

        # Menghitung tarif
        fare = self.base_fare
        extra_distance = 0  # Definisikan extra_distance dengan default 0
        if distance > self.min_distance:
            extra_distance = distance - self.min_distance
            fare += (extra_distance // 10) * self.additional_fare
            if extra_distance % 10 > 0:  # Jika ada sisa jarak, tambahkan tarif tambahan
                fare += self.additional_fare

        return f"Rp{fare}"

# Inisialisasi kalkulator
calculator = KRLFareCalculatorBogorLine()

# Aplikasi Streamlit
import streamlit as st

def main():

    st.title("KRL Fare Calculator - Bogor Line")
    st.header("Hitung Tarif Perjalanan KRL Anda")

    # Input dari pengguna dengan validasi while
    valid_start_station = False
    valid_end_station = False
    start_station = ""
    end_station = ""

    # Menggunakan while untuk validasi input stasiun awal
    while not valid_start_station:
        start_station = st.selectbox("Pilih Stasiun Awal", list(calculator.station_distances.keys()))
        if start_station in calculator.station_distances:
            valid_start_station = True
        else:
            st.error("Stasiun awal tidak ditemukan, silakan pilih stasiun yang valid.")

    # Menggunakan while untuk validasi input stasiun tujuan
    while not valid_end_station:
        end_station = st.selectbox("Pilih Stasiun Tujuan", list(calculator.station_distances.keys()))
        if end_station in calculator.station_distances:
            valid_end_station = True
        else:
            st.error("Stasiun tujuan tidak ditemukan, silakan pilih stasiun yang valid.")

    # Tombol untuk menghitung tarif
    if st.button("Hitung Tarif"):
        result = calculator.calculate_fare(start_station, end_station)
        st.write(f"Tarif perjalanan dari **{start_station}** ke **{end_station}** adalah: {result}")

if __name__ == "__main__":
    main()
