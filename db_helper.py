import requests

# TEMPEL URL WEB APP GOOGLE APPS SCRIPT BERAKHIRAN /exec DI SINI
URL_SCRIPT = "https://script.google.com/macros/s/AKfycbxO-gZwtZe-Y273tTXo4mZ9GVdexLu6FQ6XoFDt3QxkWQBB9_-UVTkH1MlLnqlwIcX1zg/exec"

def daftar_user(email, username, password):
    payload = {"action": "register", "email": email, "username": username, "password": password}
    try:
        res = requests.post(URL_SCRIPT, json=payload).json()
        return res.get("status", False), res.get("msg", "Gagal terhubung.")
    except Exception as e:
        return False, f"Error: {e}"

def login_user(identifier, password):
    payload = {"action": "login", "identifier": identifier, "password": password}
    try:
        res = requests.post(URL_SCRIPT, json=payload).json()
        return res.get("status", False), res.get("username", None), res.get("msg", "Gagal login.")
    except Exception as e:
        return False, None, f"Error: {e}"

def simpan_riwayat(username, aktivitas, hasil):
    teks_simpan = f"{aktivitas}: {hasil}"
    payload = {"action": "simpan", "username": username, "hasil": teks_simpan}
    try:
        res = requests.post(URL_SCRIPT, json=payload).json()
        return res.get("msg", "Tersimpan.")
    except Exception as e:
        return f"Error: {e}"

def lihat_riwayat(username):
    payload = {"action": "baca", "username": username}
    try:
        res = requests.post(URL_SCRIPT, json=payload).json()
        return res.get("data", "Belum ada riwayat.")
    except Exception as e:
        return f"Error: {e}"
