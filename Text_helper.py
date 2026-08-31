def balik_teks(teks):
    return teks[::-1]

def hitung_vokal(teks):
    vokal = "aiueoAIUEO"
    return sum(1 for char in teks if char in vokal)

def format_judul(teks):
    return teks.title()
