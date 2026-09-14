import customtkinter as ctk
from tkinter import messagebox
import requests

# Import modul-modul milikmu
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat
from teks_helper import balik_teks, hitung_vokal, format_judul
from logika_angka import ganjil_genap, konversi_celcius_ke_fahrenheit
from bangun_datar import luas_persegi_panjang, keliling_lingkaran, luas_segitiga
from matematic import hitung_luas_persegi, cek_bilangan_prima

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Multi-Modul + AI Belajar")
        self.geometry("480x700")
        self.user_aktif = None

        self.tampilan_login()

    def bersih_layar(self):
        for widget in self.winfo_children():
            widget.destroy()

    # ==================== PORTAL LOGIN & REGISTRASI ====================
    def tampilan_login(self):
        self.bersih_layar()

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=40, fill="both", expand=True)

        ctk.CTkLabel(frame, text="PORTAL BELAJAR & MODUL", font=("Arial", 20, "bold")).pack(pady=20)

        self.input_user = ctk.CTkEntry(frame, placeholder_text="Email / Username")
        self.input_user.pack(pady=10, padx=20, fill="x")

        self.input_pass = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        self.input_pass.pack(pady=10, padx=20, fill="x")

        btn_login = ctk.CTkButton(frame, text="Login Akun", command=self.proses_login)
        btn_login.pack(pady=10, padx=20, fill="x")

        btn_reg = ctk.CTkButton(frame, text="Registrasi Baru", fg_color="transparent", border_width=1, command=self.tampilan_register)
        btn_reg.pack(pady=5, padx=20, fill="x")

    def tampilan_register(self):
        self.bersih_layar()

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=30, fill="both", expand=True)

        ctk.CTkLabel(frame, text="REGISTRASI AKUN", font=("Arial", 20, "bold")).pack(pady=15)

        self.reg_email = ctk.CTkEntry(frame, placeholder_text="Email Baru")
        self.reg_email.pack(pady=8, padx=20, fill="x")

        self.reg_uname = ctk.CTkEntry(frame, placeholder_text="Username Baru")
        self.reg_uname.pack(pady=8, padx=20, fill="x")

        self.reg_pass = ctk.CTkEntry(frame, placeholder_text="Password Baru", show="*")
        self.reg_pass.pack(pady=8, padx=20, fill="x")

        btn_daftar = ctk.CTkButton(frame, text="Daftar Sekarang", fg_color="green", command=self.proses_register)
        btn_daftar.pack(pady=15, padx=20, fill="x")

        btn_batal = ctk.CTkButton(frame, text="Kembali ke Login", fg_color="gray", command=self.tampilan_login)
        btn_batal.pack(pady=5, padx=20, fill="x")

    # ==================== DASHBOARD UTAMA ====================
    def tampilan_dashboard(self):
        self.bersih_layar()

        lbl_user = ctk.CTkLabel(self, text=f"Siswa: {self.user_aktif.upper()}", font=("Arial", 14, "bold"))
        lbl_user.pack(pady=5)

        tabview = ctk.CTkTabview(self)
        tabview.pack(padx=10, pady=5, fill="both", expand=True)

        tab_bangun = tabview.add("Bangun Datar")
        tab_logika = tabview.add("Suhu & Angka")
        tab_teks = tabview.add("Olah Teks")
        tab_ai = tabview.add("🤖 AI Tutor")
        tab_riwayat = tabview.add("Riwayat")

        # ---------------- TAB 1: BANGUN DATAR ----------------
        ctk.CTkLabel(tab_bangun, text="Kalkulator Bangun Datar", font=("Arial", 14, "bold")).pack(pady=5)
        
        self.ent_p = ctk.CTkEntry(tab_bangun, placeholder_text="Panjang / Alas / Sisi / Jari-jari (r)")
        self.ent_p.pack(pady=4, fill="x", padx=10)
        self.ent_l = ctk.CTkEntry(tab_bangun, placeholder_text="Lebar / Tinggi (Khusus Segitiga & P.Panjang)")
        self.ent_l.pack(pady=4, fill="x", padx=10)

        frame_btn_bd = ctk.CTkFrame(tab_bangun, fg_color="transparent")
        frame_btn_bd.pack(pady=5)
        
        ctk.CTkButton(frame_btn_bd, text="Luas P.Panjang", width=110, command=self.aksi_luas_pp).grid(row=0, column=0, padx=3, pady=3)
        ctk.CTkButton(frame_btn_bd, text="Luas Segitiga", width=110, command=self.aksi_luas_segitiga).grid(row=0, column=1, padx=3, pady=3)
        ctk.CTkButton(frame_btn_bd, text="Luas Persegi", width=110, command=self.aksi_luas_persegi).grid(row=1, column=0, padx=3, pady=3)
        ctk.CTkButton(frame_btn_bd, text="Keliling Lingkaran", width=110, command=self.aksi_kel_lingkaran).grid(row=1, column=1, padx=3, pady=3)

        self.txt_penjelasan_bd = ctk.CTkTextbox(tab_bangun, height=180)
        self.txt_penjelasan_bd.pack(pady=5, fill="both", expand=True, padx=5)
        self.txt_penjelasan_bd.insert("1.0", "💡 Penjelasan & Langkah Penyelesaian akan muncul di sini...")

        # ---------------- TAB 2: SUHU & ANGKA ----------------
        ctk.CTkLabel(tab_logika, text="Logika Angka & Suhu", font=("Arial", 14, "bold")).pack(pady=5)
        self.ent_angka = ctk.CTkEntry(tab_logika, placeholder_text="Masukkan Angka / Suhu (°C)")
        self.ent_angka.pack(pady=5, fill="x", padx=10)

        frame_btn_la = ctk.CTkFrame(tab_logika, fg_color="transparent")
        frame_btn_la.pack(pady=5)
        ctk.CTkButton(frame_btn_la, text="Konversi Suhu", width=110, command=self.aksi_suhu).grid(row=0, column=0, padx=3)
        ctk.CTkButton(frame_btn_la, text="Ganjil / Genap", width=110, command=self.aksi_ganjil_genap).grid(row=0, column=1, padx=3)
        ctk.CTkButton(frame_btn_la, text="Cek Prima", width=110, command=self.aksi_cek_prima).grid(row=0, column=2, padx=3)

        self.txt_penjelasan_la = ctk.CTkTextbox(tab_logika, height=180)
        self.txt_penjelasan_la.pack(pady=5, fill="both", expand=True, padx=5)
        self.txt_penjelasan_la.insert("1.0", "💡 Penjelasan & Langkah Penyelesaian akan muncul di sini...")

        # ---------------- TAB 3: OLAH TEKS ----------------
        ctk.CTkLabel(tab_teks, text="Modul Olah Teks", font=("Arial", 14, "bold")).pack(pady=5)
        self.ent_teks = ctk.CTkEntry(tab_teks, placeholder_text="Masukkan kata/kalimat")
        self.ent_teks.pack(pady=5, fill="x", padx=10)
        
        ctk.CTkButton(tab_teks, text="Proses & Jelaskan Teks", command=self.aksi_teks).pack(pady=5)
        self.txt_penjelasan_teks = ctk.CTkTextbox(tab_teks, height=180)
        self.txt_penjelasan_teks.pack(pady=5, fill="both", expand=True, padx=5)
        self.txt_penjelasan_teks.insert("1.0", "💡 Hasil analisis teks akan muncul di sini...")

        # ---------------- TAB 4: AI TUTOR ----------------
        ctk.CTkLabel(tab_ai, text="🤖 AI Asisten Belajar", font=("Arial", 14, "bold")).pack(pady=5)
        self.ent_tanya_ai = ctk.CTkEntry(tab_ai, placeholder_text="Tanyakan soal/konsep (misal: Apa itu bilangan prima?)")
        self.ent_tanya_ai.pack(pady=5, fill="x", padx=10)
        ctk.CTkButton(tab_ai, text="Tanyakan ke AI", fg_color="purple", command=self.aksi_tanya_ai).pack(pady=5)
        
        self.txt_respon_ai = ctk.CTkTextbox(tab_ai, height=200)
        self.txt_respon_ai.pack(pady=5, fill="both", expand=True, padx=5)
        self.txt_respon_ai.insert("1.0", "Hai! Aku AI Tutor. Tanyakan apa saja terkait matematika atau matematika komputer di sini!")

        # ---------------- TAB 5: RIWAYAT ----------------
        ctk.CTkButton(tab_riwayat, text="Muat Riwayat dari Google Sheets", command=self.aksi_baca_riwayat).pack(pady=5)
        self.txt_riwayat = ctk.CTkTextbox(tab_riwayat, width=350, height=250)
        self.txt_riwayat.pack(pady=5, fill="both", expand=True)

        ctk.CTkButton(self, text="Logout", fg_color="red", command=self.tampilan_login).pack(pady=8)

    # ==================== LOGIKA PENJELASAN & PERHITUNGAN ====================
    def tampilkan_detail(self, widget_textbox, judul, penjelasan):
        widget_textbox.delete("1.0", "end")
        widget_textbox.insert("1.0", f"=== {judul} ===\n\n{penjelasan}")

    def aksi_luas_pp(self):
        try:
            p = float(self.ent_p.get())
            l = float(self.ent_l.get())
            luas = luas_persegi_panjang(p, l)
            detail = (
                f"📌 RUMUS: Luas = Panjang x Lebar\n"
                f"📝 DIKETAHUI:\n - Panjang (p) = {p}\n - Lebar (l) = {l}\n\n"
                f"⚙️ LANGKAH PENYELESAIAN:\n Luas = {p} x {l}\n Luas = {luas}\n\n"
                f"✅ HASIL AKHIR: {luas}"
            )
            self.tampilkan_detail(self.txt_penjelasan_bd, "Luas Persegi Panjang", detail)
            simpan_riwayat(self.user_aktif, "Luas P.Panjang", f"P:{p} L:{l} => Luas:{luas}")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan angka pada kolom Panjang dan Lebar!")

    def aksi_luas_segitiga(self):
        try:
            a = float(self.ent_p.get())
            t = float(self.ent_l.get())
            luas = luas_segitiga(a, t)
            detail = (
                f"📌 RUMUS: Luas = 0.5 x Alas x Tinggi\n"
                f"📝 DIKETAHUI:\n - Alas (a) = {a}\n - Tinggi (t) = {t}\n\n"
                f"⚙️ LANGKAH PENYELESAIAN:\n Luas = 0.5 x {a} x {t}\n Luas = {luas}\n\n"
                f"✅ HASIL AKHIR: {luas}"
            )
            self.tampilkan_detail(self.txt_penjelasan_bd, "Luas Segitiga", detail)
            simpan_riwayat(self.user_aktif, "Luas Segitiga", f"A:{a} T:{t} => Luas:{luas}")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan angka alas di kolom pertama & tinggi di kolom kedua!")

    def aksi_luas_persegi(self):
        try:
            s = float(self.ent_p.get())
            luas = hitung_luas_persegi(s)
            detail = (
                f"📌 RUMUS: Luas = Sisi x Sisi (s²)\n"
                f"📝 DIKETAHUI:\n - Sisi (s) = {s}\n\n"
                f"⚙️ LANGKAH PENYELESAIAN:\n Luas = {s} x {s}\n Luas = {luas}\n\n"
                f"✅ HASIL AKHIR: {luas}"
            )
            self.tampilkan_detail(self.txt_penjelasan_bd, "Luas Persegi", detail)
            simpan_riwayat(self.user_aktif, "Luas Persegi", f"Sisi:{s} => Luas:{luas}")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan panjang sisi di kolom pertama!")

    def aksi_kel_lingkaran(self):
        try:
            r = float(self.ent_p.get())
            kel = keliling_lingkaran(r)
            detail = (
                f"📌 RUMUS: Keliling = 2 x π x r  (π ≈ 3.14)\n"
                f"📝 DIKETAHUI:\n - Jari-jari (r) = {r}\n\n"
                f"⚙️ LANGKAH PENYELESAIAN:\n Keliling = 2 x 3.14 x {r}\n Keliling = {kel}\n\n"
                f"✅ HASIL AKHIR: {kel}"
            )
            self.tampilkan_detail(self.txt_penjelasan_bd, "Keliling Lingkaran", detail)
            simpan_riwayat(self.user_aktif, "Keliling Lingkaran", f"r:{r} => Keliling:{kel}")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan jari-jari di kolom pertama!")

    def aksi_suhu(self):
        try:
            c = float(self.ent_angka.get())
            f = konversi_celcius_ke_fahrenheit(c)
            detail = (
                f"📌 RUMUS: °F = (°C x 9/5) + 32\n"
                f"📝 DIKETAHUI:\n - Suhu Celcius = {c}°C\n\n"
                f"⚙️ LANGKAH PENYELESAIAN:\n 1. Kalikan celcius dengan 9/5: {c} x 1.8 = {c*1.8}\n 2. Tambahkan 32: {c*1.8} + 32 = {f}\n\n"
                f"✅ HASIL AKHIR: {c}°C = {f}°F"
            )
            self.tampilkan_detail(self.txt_penjelasan_la, "Konversi Suhu", detail)
            simpan_riwayat(self.user_aktif, "Konversi Suhu", f"{c}°C = {f}°F")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan angka suhu di kolom input!")

    def aksi_ganjil_genap(self):
        try:
            x = int(self.ent_angka.get())
            res = ganjil_genap(x)
            sisa = x % 2
            detail = (
                f"📌 METODE: Pembagian Sisa Modulo (% 2)\n"
                f"📝 ANGKA: {x}\n\n"
                f"⚙️ LANGKAH ANALISIS:\n {x} dibagi 2 mendapatkan sisa {sisa}.\n - Jika sisa 0 = Bilangan Genap\n - Jika sisa bukan 0 = Bilangan Ganjil\n\n"
                f"✅ KESIMPULAN: {res}"
            )
            self.tampilkan_detail(self.txt_penjelasan_la, "Analisis Ganjil Genap", detail)
            simpan_riwayat(self.user_aktif, "Ganjil Genap", f"{x} -> {res}")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan bilangan bulat di kolom input!")

    def aksi_cek_prima(self):
        try:
            n = int(self.ent_angka.get())
            is_prima = cek_bilangan_prima(n)
            status_teks = "merupakan Bilangan Prima" if is_prima else "BUKAN Bilangan Prima"
            detail = (
                f"📌 DEFINISI: Bilangan prima adalah bilangan > 1 yang hanya bisa dibagi 1 dan dirinya sendiri.\n"
                f"📝 ANGKA YANG DICEK: {n}\n\n"
                f"⚙️ ANALISIS KETERBAGIAN:\n Kriteria pengecekan pembagi dari 2 hingga √{n}.\n\n"
                f"✅ KESIMPULAN: Angka {n} {status_teks}."
            )
            self.tampilkan_detail(self.txt_penjelasan_la, "Cek Bilangan Prima", detail)
            simpan_riwayat(self.user_aktif, "Cek Prima", f"{n} -> {status_teks}")
        except ValueError:
            messagebox.showerror("Input Salah", "Masukkan bilangan bulat di kolom input!")

    def aksi_teks(self):
        t = self.ent_teks.get()
        if not t:
            messagebox.showwarning("Kosong", "Masukkan kata/kalimat terlebih dahulu!")
            return
        
        dibalik = balik_teks(t)
        vokal = hitung_vokal(t)
        judul = format_judul(t)

        detail = (
            f"📝 TEKS ASLI: \"{t}\"\n\n"
            f"🔹 1. TEKS DIBALIK (Reversed Text):\n -> \"{dibalik}\"\n (Cara: Urutan karakter dibalik dari belakang ke depan)\n\n"
            f"🔹 2. JUMLAH HURUF VOKAL (A, I, U, E, O):\n -> {vokal} huruf vokal\n (Cara: Memeriksa setiap karakter apakah masuk himpunan vokal)\n\n"
            f"🔹 3. FORMAT JUDUL (Title Case):\n -> \"{judul}\"\n (Cara: Mengubah huruf pertama setiap kata menjadi kapital)"
        )
        self.tampilkan_detail(self.txt_penjelasan_teks, "Analisis Olah Teks", detail)
        simpan_riwayat(self.user_aktif, "Olah Teks", f"'{t}' => Dibalik:'{dibalik}', Vokal:{vokal}")

    # ==================== FITUR INTEGRASI AI TUTOR ====================
    def aksi_tanya_ai(self):
        pertanyaan = self.ent_tanya_ai.get()
        if not pertanyaan:
            messagebox.showwarning("Kosong", "Tuliskan pertanyaanmu dulu!")
            return

        self.txt_respon_ai.delete("1.0", "end")
        self.txt_respon_ai.insert("1.0", "⏳ AI sedang berpikir dan menyusun penjelasan...")
        self.update()

        try:
            # Menggunakan DuckDuckGo Lite API untuk respon gratis & cepat tanpa butuh API Key
            url = f"https://api.duckduckgo.com/?q={requests.utils.quote(pertanyaan)}&format=json&no_html=1"
            res = requests.get(url, timeout=5).json()
            jawaban = res.get("AbstractText", "")

            if not jawaban:
                # Jawaban alternatif sederhana jika tidak ditemukan di abstrak
                jawaban = f"Konsep '{pertanyaan}':\nMerupakan bagian dari ilmu matematika/komputer. Silakan pelajari rumus dasar dan latihan soal terkait untuk pemahaman lebih mendalam."

            teks_akhir = f"❓ PERTANYAAN: {pertanyaan}\n\n🤖 AI PENJELASAN:\n{jawaban}"
            self.tampilkan_detail(self.txt_respon_ai, "Penjelasan AI Tutor", teks_akhir)
        except Exception as e:
            # Fallback edukatif jika koneksi internet offline
            teks_offline = f"❓ PERTANYAAN: {pertanyaan}\n\n🤖 AI ASSISTANT (Modus Offline):\nUntuk memahami '{pertanyaan}', kamu bisa mengecek modul rumus yang tersedia pada aplikasi ini atau gunakan jaringan internet yang stabil."
            self.tampilkan_detail(self.txt_respon_ai, "AI Tutor", teks_offline)

    # ==================== LOGIKA KONEKSI DATABASE ====================
    def proses_login(self):
        u = self.input_user.get()
        p = self.input_pass.get()
        status, username, pesan = login_user(u, p)
        if status:
            self.user_aktif = username
            messagebox.showinfo("Berhasil", pesan)
            self.tampilan_dashboard()
        else:
            messagebox.showerror("Gagal", pesan)

    def proses_register(self):
        e = self.reg_email.get()
        u = self.reg_uname.get()
        p = self.reg_pass.get()
        status, pesan = daftar_user(e, u, p)
        if status:
            messagebox.showinfo("Berhasil", pesan)
            self.tampilan_login()
        else:
            messagebox.showerror("Gagal", pesan)

    def aksi_baca_riwayat(self):
        data = lihat_riwayat(self.user_aktif)
        self.txt_riwayat.delete("1.0", "end")
        self.txt_riwayat.insert("1.0", str(data))

if __name__ == "__main__":
    app = App()
    app.mainloop()

