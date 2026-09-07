import os
import sys

# Jalur aman agar tidak ModuleNotFoundError di Pydroid 3
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from teks_helper import *
from logika_angka import *
from bangun_datar import *
from matematic import *
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat

user_aktif = None

# --- PORTAL LOGIN / REGISTRASI (GAYA WEBSITE) ---
while True:
    print("========================================")
    print("      PORTAL AKUN APLIKASI WEB          ")
    print("========================================")
    print("1. Login Akun")
    print("2. Registrasi Akun Baru")
    print("3. Keluar Aplikasi")
    pilihan_akses = input("Pilih menu (1-3): ")
    
    if pilihan_akses == "1":
        print("\n--- MENU LOGIN ---")
        identifier = input("Email / Username : ")
        pwd = input("Password         : ")
        status, username, pesan = login_user(identifier, pwd)
        print(f" -> {pesan}\n")
        if status:
            user_aktif = username
            break
            
    elif pilihan_akses == "2":
        print("\n--- REGISTRASI AKUN BARU ---")
        email = input("Masukkan Email    : ")
        uname = input("Buat Username     : ")
        pwd   = input("Buat Password     : ")
        status, pesan = daftar_user(email, uname, pwd)
        print(f" -> {pesan}\n")
        
    elif pilihan_akses == "3":
        print("\nProgram dihentikan.")
        sys.exit()
    else:
        print("\nPilihan tidak valid.\n")

# --- DASHBOARD APLIKASI (SETELAH LOGIN) ---
while True:
    print("\n========================================")
    print(f" DASHBOARD APLIKASI | AKUN: {user_aktif.upper()}")
    print("========================================")
    print("1. Modul Olah Teks")
    print("2. Modul Logika Angka")
    print("3. Modul Bangun Datar")
    print("4. Modul Matematik & Prima")
    print("5. Lihat Riwayat Tersimpan di Akun Saya")
    print("6. Logout & Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == "1":
        print("\n--- MODUL OLAH TEKS ---")
        kata = input("Masukkan kata/kalimat: ")
        hasil = f"Dibalik: {balik_teks(kata)} | Vokal: {hitung_vokal(kata)}"
        print(" ->", hasil)
        
        simpan = input("Simpan hasil ke akun? (y/n): ")
        if simpan.lower() == 'y':
            msg = simpan_riwayat(user_aktif, "Olah Teks", hasil)
            print(" ->", msg)
        
    elif pilihan == "2":
        print("\n--- MODUL LOGIKA ANGKA ---")
        c = float(input("Masukkan suhu (°C): "))
        hasil = f"{c}°C = {konversi_celcius_ke_fahrenheit(c)}°F"
        print(" ->", hasil)
        
        simpan = input("Simpan hasil ke akun? (y/n): ")
        if simpan.lower() == 'y':
            msg = simpan_riwayat(user_aktif, "Konversi Suhu", hasil)
            print(" ->", msg)
        
    elif pilihan == "3":
        print("\n--- MODUL BANGUN DATAR ---")
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        luas = luas_persegi_panjang(p, l)
        hasil = f"Persegi Panjang P:{p} L:{l} => Luas: {luas}"
        print(" -> Luas Persegi Panjang:", luas)
        
        simpan = input("Simpan hasil ke akun? (y/n): ")
        if simpan.lower() == 'y':
            msg = simpan_riwayat(user_aktif, "Bangun Datar", hasil)
            print(" ->", msg)

    elif pilihan == "4":
        print("\n--- MODUL MATEMATIK & PRIMA ---")
        s = float(input("Masukkan sisi persegi: "))
        luas_p = hitung_luas_persegi(s)
        hasil = f"Sisi: {s} => Luas Persegi: {luas_p}"
        print(" -> Luas Persegi:", luas_p)
        
        simpan = input("Simpan hasil ke akun? (y/n): ")
        if simpan.lower() == 'y':
            msg = simpan_riwayat(user_aktif, "Matematik", hasil)
            print(" ->", msg)

    elif pilihan == "5":
        print(f"\n--- RIWAYAT DATA TERATAS AKUN: {user_aktif} ---")
        riwayat = lihat_riwayat(user_aktif)
        if not riwayat:
            print("Belum ada data yang tersimpan di akun ini.")
        else:
            for item in riwayat:
                print(f"[{item[2]}] {item[0]} -> {item[1]}")
                
    elif pilihan == "6":
        print(f"\nLogout berhasil. Sampai jumpa lagi, {user_aktif}!")
        break
    else:
        print("\nPilihan salah, masukkan angka 1-6.")
