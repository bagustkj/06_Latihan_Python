from teks_helper import *
from logika_angka import *
from bangun_datar import *
from matematic import *

print("=== UJI COBA MODUL UTAMA (V2 LATIHAN CODING) ===")

# 1. Menguji fungsi dari modul teks_helper.py
print("\n--- MODUL TEKS HELPER ---")
print("Teks Dibalik   :", balik_teks("python"))
print("Jumlah Vokal   :", hitung_vokal("belajar python"))
print("Format Judul   :", format_judul("belajar python modular"))

# 2. Menguji fungsi dari modul logika_angka.py
print("\n--- MODUL LOGIKA ANGKA ---")
print("Suhu 30°C ke °F:", konversi_celcius_ke_fahrenheit(30))
print("Faktorial 5    :", hitung_faktorial(5))

# 3. Menguji fungsi dari modul bangun_datar.py
print("\n--- MODUL BANGUN DATAR ---")
print("Luas Persegi Panjang:", luas_persegi_panjang(5, 3))
print("Keliling Lingkaran  :", keliling_lingkaran(7))

# 4. Menguji fungsi dari modul matematic.py
print("\n--- MODUL MATEMATIC ---")
print("Luas Persegi        :", hitung_luas_persegi(4))
print("Apakah 7 Prima?     :", cek_bilangan_prima(7))
