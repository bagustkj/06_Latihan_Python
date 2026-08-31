import math

def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_keliling_persegi(sisi):
    return 4 * sisi

def cek_bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hitung_luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
