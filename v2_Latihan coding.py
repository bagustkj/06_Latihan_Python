import math

# === FUNGSI TAMBAHAN: Cek Bilangan Prima ===
def cek_bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
# === TUGAS 1: Versi Sekali Run ===
x = int(input("Masukkan angka: "))
if x % 2 == 0:
    print("genap")
else:
    print("ganjil")

print("\n--- Sekarang lanjut ke Tugas 2 (Perulangan) ---\n")

# === TUGAS 2: Versi Perulangan ===
while True:
    x = int(input("Masukkan angka (untuk berhenti, tutup programnya): "))
    if x % 2 == 0:
        print("genap")
    else:
        print("ganjil")
     # Mengecek apakah bilangan prima
    if cek_bilangan_prima(x) == True:
        print("bilangan prima")
    else:
        print("bukan bilangan prima")

