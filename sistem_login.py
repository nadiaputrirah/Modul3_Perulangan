print("===== SISTEM LOGIN SEDERHANA =====")
def login_system():
    login_data = {
        "nadiaputri": "nadia"
    }
    attempts = 3

    while attempts > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in login_data and password == login_data[username]:
            print("Login berhasil! Selamat datang", username)
            break
        else:
            attempts -= 1
            print(f"Username atau password salah. Sisa percobaan: {attempts}")

    if attempts == 0:
        print("Anda telah melebihi batas percobaan. Tidak dapat melakukan login kembali.")

login_system()
