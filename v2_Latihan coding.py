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
