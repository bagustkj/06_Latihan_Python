import customtkinter as ctk
from tkinter import messagebox
import os
import sys

# Amankan path folder di HP/Pydroid 3
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import fungsi dari modul-modul milikmu
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat
from teks_helper import balik_teks, hitung_vokal
from logika_angka import konversi_celcius_ke_fahrenheit
from bangun_datar import luas_persegi_panjang
from matematic import hitung_luas_persegi, cek_bilangan_prima

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Multi-Modul")
        self.geometry("450x650")
        self.user_aktif = None

        self.tampilan_login()

    def bersih_layar(self):
        for widget in self.winfo_children():
            widget.destroy()

    # --- TAMPILAN 1: LOGIN ---
    def tampilan_login(self):
        self.bersih_layar()

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=40, fill="both", expand=True)

        ctk.CTkLabel(frame, text="PORTAL AKUN APLIKASI WEB", font=("Arial", 18, "bold")).pack(pady=20)

        self.input_user = ctk.CTkEntry(frame, placeholder_text="Email / Username")
        self.input_user.pack(pady=10, padx=20, fill="x")

        self.input_pass = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        self.input_pass.pack(pady=10, padx=20, fill="x")

        btn_login = ctk.CTkButton(frame, text="1. Login Akun", command=self.proses_login)
        btn_login.pack(pady=10, padx=20, fill="x")

        btn_reg = ctk.CTkButton(frame, text="2. Registrasi Akun Baru", fg_color="transparent", border_width=1, command=self.tampilan_register)
        btn_reg.pack(pady=5, padx=20, fill="x")

    # --- TAMPILAN 2: REGISTRASI ---
    def tampilan_register(self):
        self.bersih_layar()

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=30, fill="both", expand=True)

        ctk.CTkLabel(frame, text="REGISTRASI AKUN BARU", font=("Arial", 18, "bold")).pack(pady=15)

        self.reg_email = ctk.CTkEntry(frame, placeholder_text="Masukkan Email")
        self.reg_email.pack(pady=8, padx=20, fill="x")

        self.reg_uname = ctk.CTkEntry(frame, placeholder_text="Buat Username")
        self.reg_uname.pack(pady=8, padx=20, fill="x")

        self.reg_pass = ctk.CTkEntry(frame, placeholder_text="Buat Password", show="*")
        self.reg_pass.pack(pady=8, padx=20, fill="x")

        btn_daftar = ctk.CTkButton(frame, text="Daftar", fg_color="green", command=self.proses_register)
        btn_daftar.pack(pady=15, padx=20, fill="x")

        btn_batal = ctk.CTkButton(frame, text="Batal", fg_color="gray", command=self.tampilan_login)
        btn_batal.pack(pady=5, padx=20, fill="x")

    # --- TAMPILAN 3: DASHBOARD MAIN MENU ---
    def tampilan_dashboard(self):
        self.bersih_layar()

        lbl_user = ctk.CTkLabel(self, text=f"DASHBOARD | AKUN: {self.user_aktif.upper()}", font=("Arial", 14, "bold"))
        lbl_user.pack(pady=10)

        tabview = ctk.CTkTabview(self)
        tabview.pack(padx=15, pady=10, fill="both", expand=True)

        tab_teks = tabview.add("1. Olah Teks")
        tab_logika = tabview.add("2. Suhu")
        tab_bangun = tabview.add("3. Bangun Datar")
        tab_matem = tabview.add("4. Matematik")
        tab_riwayat = tabview.add("5. Riwayat")

        # 1. Modul Olah Teks
        ctk.CTkLabel(tab_teks, text="--- MODUL OLAH TEKS ---").pack(pady=5)
        self.ent_teks = ctk.CTkEntry(tab_teks, placeholder_text="Masukkan kata/kalimat")
        self.ent_teks.pack(pady=10, fill="x", padx=10)
        ctk.CTkButton(tab_teks, text="Proses Teks", command=self.aksi_teks).pack(pady=5)
        self.lbl_res_teks = ctk.CTkLabel(tab_teks, text="Hasil: -")
        self.lbl_res_teks.pack(pady=10)

        # 2. Modul Logika Angka
        ctk.CTkLabel(tab_logika, text="--- MODUL LOGIKA ANGKA ---").pack(pady=5)
        self.ent_suhu = ctk.CTkEntry(tab_logika, placeholder_text="Masukkan suhu (°C)")
        self.ent_suhu.pack(pady=10, fill="x", padx=10)
        ctk.CTkButton(tab_logika, text="Konversi Suhu", command=self.aksi_suhu).pack(pady=5)
        self.lbl_res_suhu = ctk.CTkLabel(tab_logika, text="Hasil: -")
        self.lbl_res_suhu.pack(pady=10)

        # 3. Modul Bangun Datar
        ctk.CTkLabel(tab_bangun, text="--- MODUL BANGUN DATAR ---").pack(pady=5)
        self.ent_p = ctk.CTkEntry(tab_bangun, placeholder_text="Masukkan panjang")
        self.ent_p.pack(pady=5, fill="x", padx=10)
        self.ent_l = ctk.CTkEntry(tab_bangun, placeholder_text="Masukkan lebar")
        self.ent_l.pack(pady=5, fill="x", padx=10)
        ctk.CTkButton(tab_bangun, text="Hitung Luas P.Panjang", command=self.aksi_bangun).pack(pady=5)
        self.lbl_res_bangun = ctk.CTkLabel(tab_bangun, text="Hasil: -")
        self.lbl_res_bangun.pack(pady=10)

        # 4. Modul Matematik
        ctk.CTkLabel(tab_matem, text="--- MODUL MATEMATIK ---").pack(pady=5)
        self.ent_sisi = ctk.CTkEntry(tab_matem, placeholder_text="Masukkan sisi persegi")
        self.ent_sisi.pack(pady=10, fill="x", padx=10)
        ctk.CTkButton(tab_matem, text="Hitung Luas Persegi", command=self.aksi_matem).pack(pady=5)
        self.lbl_res_matem = ctk.CTkLabel(tab_matem, text="Hasil: -")
        self.lbl_res_matem.pack(pady=10)

        # 5. Lihat Riwayat
        btn_refresh = ctk.CTkButton(tab_riwayat, text="Lihat Riwayat Saya", command=self.aksi_baca_riwayat)
        btn_refresh.pack(pady=5)
        self.txt_riwayat = ctk.CTkTextbox(tab_riwayat, width=350, height=230)
        self.txt_riwayat.pack(pady=5, fill="both", expand=True)

        ctk.CTkButton(self, text="6. Logout & Keluar", fg_color="red", command=self.tampilan_login).pack(pady=10)

    # --- LOGIKA TOMBOL & KONEKSI ---
    def proses_login(self):
        u = self.input_user.get()
        p = self.input_pass.get()
        status, username, pesan = login_user(u, p)
        if status:
            self.user_aktif = username
            messagebox.showinfo("Sukses", pesan)
            self.tampilan_dashboard()
        else:
            messagebox.showerror("Gagal", pesan)

    def proses_register(self):
        e = self.reg_email.get()
        u = self.reg_uname.get()
        p = self.reg_pass.get()
        status, pesan = daftar_user(e, u, p)
        if status:
            messagebox.showinfo("Sukses", pesan)
            self.tampilan_login()
        else:
            messagebox.showerror("Gagal", pesan)

    def aksi_teks(self):
        kata = self.ent_teks.get()
        hasil = f"Dibalik: {balik_teks(kata)} | Vokal: {hitung_vokal(kata)}"
        self.lbl_res_teks.configure(text=f"Hasil: {hasil}")
        msg = simpan_riwayat(self.user_aktif, "Olah Teks", hasil)
        messagebox.showinfo("Info Simpan", msg)

    def aksi_suhu(self):
        try:
            c = float(self.ent_suhu.get())
            hasil = f"{c}°C = {konversi_celcius_ke_fahrenheit(c)}°F"
            self.lbl_res_suhu.configure(text=f"Hasil: {hasil}")
            msg = simpan_riwayat(self.user_aktif, "Konversi Suhu", hasil)
            messagebox.showinfo("Info Simpan", msg)
        except ValueError:
            messagebox.showerror("Eror", "Masukkan angka suhu yang valid!")

    def aksi_bangun(self):
        try:
            p = float(self.ent_p.get())
            l = float(self.ent_l.get())
            luas = luas_persegi_panjang(p, l)
            hasil = f"Persegi Panjang P:{p} L:{l} => Luas: {luas}"
            self.lbl_res_bangun.configure(text=f"Hasil: {luas}")
            msg = simpan_riwayat(self.user_aktif, "Bangun Datar", hasil)
            messagebox.showinfo("Info Simpan", msg)
        except ValueError:
            messagebox.showerror("Eror", "Masukkan angka panjang dan lebar yang valid!")

    def aksi_matem(self):
        try:
            s = float(self.ent_sisi.get())
            luas_p = hitung_luas_persegi(s)
            hasil = f"Sisi: {s} => Luas Persegi: {luas_p}"
            self.lbl_res_matem.configure(text=f"Hasil: {luas_p}")
            msg = simpan_riwayat(self.user_aktif, "Matematik", hasil)
            messagebox.showinfo("Info Simpan", msg)
        except ValueError:
            messagebox.showerror("Eror", "Masukkan angka sisi yang valid!")

    def aksi_baca_riwayat(self):
        riwayat = lihat_riwayat(self.user_aktif)
        self.txt_riwayat.delete("1.0", "end")
        self.txt_riwayat.insert("1.0", str(riwayat))

if __name__ == "__main__":
    app = App()
    app.mainloop()
