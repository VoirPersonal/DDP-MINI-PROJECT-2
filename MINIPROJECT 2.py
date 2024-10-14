from prettytable import PrettyTable

data_mobil = {}
admin = {"username": "pikriganteng", "password": "030806"}

try :
    def login_admin():
        print("\n=== LOGIN ADMIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username == admin["username"] and password == admin["password"]:
            print("Login berhasil! Halooo Admin tercinta")
            fitur_admin()
        else:
            print("Username atau password salah!")

    def fitur_admin():
        while True:
            print("\n=== MENU ADMIN ===")
            print("1. Tambah Data Kendaraan (Create)")
            print("2. Lihat Data Kendaraan (Read)")
            print("3. Perbarui Data Kendaraan (Update)")
            print("4. Hapus Data Kendaraan (Delete)")
            print("5. Kembali ke Menu Utama")

            pilihan = input("Pilih opsi (1-5): ")
            if pilihan == '1':
                tambah_data_kendaraan()
            elif pilihan == '2':
                lihat_data_kendaraan()
            elif pilihan == '3':
                perbarui_data_kendaraan()
            elif pilihan == '4':
                hapus_data_kendaraan()
            elif pilihan == '5':
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

    def tambah_data_kendaraan():
        nomor_plat = input("Masukkan Nomor Plat Kendaraan: ")
        if nomor_plat in data_mobil:
            print("Kendaraan sudah ada dalam sistem.")
        else:
            status_mobil = "Masuk"
            data_mobil[nomor_plat] = {
                "status_mobil": status_mobil,
                'Nomor Parkir': len(data_mobil) + 1
            }
            print(f"Data kendaraan dengan nomor plat {nomor_plat} berhasil ditambahkan.")

    def lihat_data_kendaraan():
        print("\n=== DATA KENDARAAN ===")
        if data_mobil:
            tabel = PrettyTable()
            tabel.field_names = ["Nomor Polisi", "Status", "Nomor Parkir"]
            for nomor_polisi, info in data_mobil.items():
                tabel.add_row([nomor_polisi, info['status_mobil'], info['Nomor Parkir']])
            print(tabel)
        else:
            print("Tidak ada data kendaraan yang tersimpan.")

    def perbarui_data_kendaraan():
        nomor_plat = input("Masukkan Nomor Plat Kendaraan yang ingin diperbarui: ")
        if nomor_plat in data_mobil:
            status_baru = input("Masukkan Status Baru (Masuk/Keluar): ")
            data_mobil[nomor_plat]['status_mobil'] = status_baru
            print(f"Status kendaraan dengan nomor plat {nomor_plat} telah diperbarui menjadi '{status_baru}'.")
        else:
            print("Kendaraan dengan nomor plat tersebut tidak ditemukan.")

    def hapus_data_kendaraan():
        nomor_plat = input("Masukkan Nomor Plat Kendaraan yang ingin dihapus: ")
        if nomor_plat in data_mobil:
            del data_mobil[nomor_plat]
            print(f"Kendaraan dengan nomor plat {nomor_plat} berhasil dihapus.")
        else:
            print("Kendaraan dengan nomor plat tersebut tidak ditemukan.")

    def kendaraan_masuk():
        nomor_plat = input("Masukkan Nomor Plat: ")
        status_mobil = "Masuk"

        if nomor_plat in data_mobil:
            print("Kendaraan sudah ada")
        else:
            data_mobil[nomor_plat] = {
                "status_mobil": status_mobil,
                'Nomor Parkir': len(data_mobil) + 1
            }
            print(f"Data kendaraan disimpan. Nomor parkir anda adalah: {data_mobil[nomor_plat]['Nomor Parkir']}")

    def kendaraan_keluar():
        nomor_parkir = int(input("Masukkan Nomor Parkir Kendaraan: "))
        kendaraan_ditemukan = None
        for nomor_polisi, info in data_mobil.items():
            if info['Nomor Parkir'] == nomor_parkir:
                kendaraan_ditemukan = nomor_polisi
                break

        if kendaraan_ditemukan is None:
            print("Kendaraan dengan nomor parkir tidak ada")
        else:
            try:
                durasi_parkir = float(input("Masukkan durasi parkir (dalam jam): "))
                if durasi_parkir < 0:
                    print("Durasi parkir tidak valid.")
                    return
            except ValueError:
                print("Input durasi parkir harus berupa angka.")
                return
            
            tarif_per_jam = 20000
            biaya_parkir = durasi_parkir * tarif_per_jam
            
            data_mobil[kendaraan_ditemukan]['status_mobil'] = "Keluar"
            struk = PrettyTable()
            struk.field_names = ["Keterangan", "Detail"]
            struk.add_row(["Nomor Polisi", kendaraan_ditemukan])
            struk.add_row(["Nomor Parkir", nomor_parkir])
            struk.add_row(["Durasi Parkir (jam)", f"{durasi_parkir:.2f} jam"])
            struk.add_row(["Biaya Parkir", f"Rp {biaya_parkir:,.0f}"])
            struk.add_row(["Status", "Keluar"])
            print("\n=== Struk Parkir ===")
            print(struk)
            print("Terima kasih telah menggunakan layanan parkir kami!")

    def menu_utama():
        while True:
            print("\n=== PARKIR MOBIL GACOR ===")
            print("1. Kendaraan Masuk")
            print("2. Kendaraan Keluar")
            print("3. Lihat Data Kendaraan")
            print("4. Admin Login")
            print("5. Keluar dari Sistem")

            pilihan = input("Pilih opsi (1-5): ")
            if pilihan == '1':
                kendaraan_masuk()
            elif pilihan == '2':
                kendaraan_keluar()
            elif pilihan == '3':
                lihat_data_kendaraan()
            elif pilihan == '4':
                login_admin()
            elif pilihan == '5':
                print("Terima kasih, sampai jumpa lagi!!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")
except:
    print("Tidak Valid")

menu_utama()