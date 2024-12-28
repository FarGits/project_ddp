import streamlit as st
import krl  # Import file krl.py sebagai modul
import mrt 
import lrt
import airport

# Sidebar Navigation
st.sidebar.title("Navigasi")
menu = st.sidebar.selectbox("Pilih Halaman:", ["Home", "MRT", "KRL", "LRT", "AIRPORT"])

if menu == "Home":
    st.title("Selamat Datang di Website Penghitung Tarif Transportasi Umum")
    st.write("""
    Seiring dengan pesatnya perkembangan kota-kota besar di Indonesia, kebutuhan akan transportasi umum yang efisien dan terjangkau semakin meningkat. 
    KRL, MRT, LRT, dan transportasi bandara kini menjadi pilihan utama bagi masyarakat dalam beraktivitas sehari-hari.

    Untuk itu, penting menetapkan tarif yang wajar dan transparan agar sistem transportasi ini dapat terus berkembang, lebih banyak digunakan, 
    serta membantu mengurangi kemacetan dan polusi. 

    Perhitungan tarif yang tepat harus mempertimbangkan:
    - **Biaya operasional**
    - **Pemeliharaan**
    - **Pengembangan sistem transportasi**

    Hal ini dilakukan dengan tetap memastikan keadilan bagi semua lapisan masyarakat. Dengan tarif yang sesuai, diharapkan masyarakat semakin 
    tertarik menggunakan transportasi umum, yang pada akhirnya memberikan manfaat besar bagi masyarakat dan lingkungan.
    """)   
    st.write("""
Fungsi dari pembuatan website ini untuk masyarakat adalah:

1. **Menyediakan Informasi Tarif Transportasi dengan Cepat dan Mudah**  
   Website ini membantu pengguna menghitung tarif transportasi seperti KRL, MRT, LRT, dan penerbangan antar bandara di Pulau Jawa dengan akurat dan transparan.

2. **Meningkatkan Kesadaran tentang Transportasi Umum**  
   Dengan informasi yang jelas dan mudah diakses, masyarakat diharapkan lebih memahami pentingnya transportasi umum sebagai solusi untuk mobilitas harian.

3. **Mendorong Penggunaan Transportasi Umum**  
   Dengan mengetahui tarif yang terjangkau, masyarakat diharapkan semakin tertarik untuk menggunakan transportasi umum, yang dapat mengurangi kemacetan dan polusi di kota-kota besar.

4. **Meningkatkan Efisiensi Perjalanan**  
   Website ini membantu pengguna merencanakan perjalanan dengan lebih baik, termasuk menentukan rute dan estimasi biaya perjalanan mereka.

5. **Memberikan Nilai Edukasi**  
   Website ini juga dapat menjadi alat edukasi untuk meningkatkan pemahaman masyarakat tentang sistem tarif transportasi umum dan cara menghitungnya.

6. **Mendukung Tujuan Pembangunan Berkelanjutan**  
   Dengan mendorong lebih banyak orang menggunakan transportasi umum, website ini secara tidak langsung mendukung upaya pengurangan emisi karbon dan pembangunan kota yang berkelanjutan.
""")

elif menu == "MRT":
    st.title("Halaman MRT")
    mrt.main()
elif menu == "KRL":
    st.title("Halaman KRL")
    krl.main()  # Panggil fungsi main() di dalam krl.py
elif menu == "LRT":
    st.title("Halaman LRT")
    lrt.main()
elif menu == "AIRPORT":
    st.title("Halaman AIRPORT")
    airport.main()

# Rute Navigation
st.sidebar.title("Rute")
menu = st.sidebar.selectbox("Pilih Transportasi", ["Pilih", "MRT", "KRL", "LRT"], index=0)

# Cek apakah gambar sudah ditampilkan
if menu == "Pilih":
    st.write("Silakan pilih transportasi dari menu di sidebar.")
elif menu == "MRT":
    st.title("")
    if "show_image_mrt" not in st.session_state:
        st.session_state.show_image_mrt = True
    
    # Tampilkan gambar MRT jika belum ditampilkan
    if st.session_state.show_image_mrt:
        st.image("mrt.png", caption="Ilustrasi MRT", use_container_width=True)
        if st.button("Lanjut ke Pemilihan Rute"):
            st.session_state.show_image_mrt = False
            st.rerun()  # Ganti experimental_rerun dengan rerun()

    # Setelah gambar disembunyikan, tampilkan pilihan stasiun
    if not st.session_state.show_image_mrt:
        st.write(f"Sudah menentukan pilihan anda?silahkan pilih di Navigasi")
        
elif menu == "KRL":
    st.title("")
    if "show_image_krl" not in st.session_state:
        st.session_state.show_image_krl = True
    
    # Tampilkan gambar KRL jika belum ditampilkan
    if st.session_state.show_image_krl:
        st.image("krl.png", caption="Ilustrasi KRL", use_container_width=True)
        if st.button("Lanjut ke Pemilihan Rute"):
            st.session_state.show_image_krl = False
            st.rerun()  # Ganti experimental_rerun dengan rerun()

    # Setelah gambar disembunyikan, tampilkan pilihan stasiun
    if not st.session_state.show_image_krl:
        st.write(f"Sudah menentukan pilihan anda?silahkan pilih di Navigasi")

elif menu == "LRT":
    st.title("")
    if "show_image_lrt" not in st.session_state:
        st.session_state.show_image_lrt = True
    
    # Tampilkan gambar LRT jika belum ditampilkan
    if st.session_state.show_image_lrt:
        st.image("lrt.png", caption="Ilustrasi LRT", use_container_width=True)
        if st.button("Lanjut ke Pemilihan Rute"):
            st.session_state.show_image_lrt = False
            st.rerun()  # Ganti experimental_rerun dengan rerun()

    # Setelah gambar disembunyikan, tampilkan pilihan stasiun
    if not st.session_state.show_image_lrt:
        st.write(f"Sudah menentukan pilihan anda?silahkan pilih di Navigasi")
