def konversi_celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def hitung_faktorial(n):
    if n <= 1:
        return 1
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil
