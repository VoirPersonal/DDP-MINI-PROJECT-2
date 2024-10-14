# DDP-MINI-PROJECT-2

- Nama : Fikri Abiyyu Rahman.
- Kelas : B
- NIM : 2409116063

## Membuat tampilan tabel dengan menggunakan PreattyTable
```python
from prettytable import PrettyTable
```

Ini buat import modul PrettyTable yang kita pakai buat menampilkan data kendaraan dalam bentuk tabel yang rapi.

## Menyimpan data di Dictionary
```python
data_mobil = {}
admin = {"username": "pikriganteng", "password": "030806"}
```

Di sini terdapat dua variabel yang penting:
- data_mobil: Menyimpan data kendaraan yang ada di parkiran.
- admin: Menyimpan username dan password admin buat login.

## Login admin
```python
    def login_admin():
        print("\n=== LOGIN ADMIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username == admin["username"] and password == admin["password"]:
            print("Login berhasil! Halooo Admin tercinta")
            fitur_admin()
        else:
            print("Username atau password salah!")
```

Fungsi ini buat login sebagai admin. Kalau username dan passwordnya benar akan lanjut ke menu admin, kalau salah, ya gagal login.

## Menampilkan fitur admin
```python
    def fitur_admin():
        while True:
            print("\n=== MENU ADMIN ===")
            print("1. Tambah Data Kendaraan (Create)")
            print("2. Lihat Data Kendaraan (Read)")
            print("3. Perbarui Data Kendaraan (Update)")
            print("4. Hapus Data Kendaraan (Delete)")
            print("5. Kembali ke Menu Utama")
```

Fungsi ini untuk menampilkan apa saja fitur-fitur yang ada pada user admin, seperti:

- Tambah Data Kendaraan (Create)
- Lihat Data Kendaraan (Read)
- Perbarui Data Kendaraan (Update)
- Hapus Data Kendaraan (Delete)
- Kembali ke Menu Utama

## Fungsi admin tambah data kendaraan
```python
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
```

Admin bisa nambahin data kendaraan baru di sini. Kalau nomor plat kendaraan yang dimasukin udah ada, sistem bakal kasih tahu kalau kendaraan itu udah ada di sistem.

## Fungsi admin lihat data kendaraan
```python
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
```

Di sini kita bisa ngelihat semua data kendaraan yang lagi ada di parkiran dalam bentuk tabel yang rapi.

## Fungsi admin perbarui data kendaraan
```python
    def perbarui_data_kendaraan():
        nomor_plat = input("Masukkan Nomor Plat Kendaraan yang ingin diperbarui: ")
        if nomor_plat in data_mobil:
            status_baru = input("Masukkan Status Baru (Masuk/Keluar): ")
            data_mobil[nomor_plat]['status_mobil'] = status_baru
            print(f"Status kendaraan dengan nomor plat {nomor_plat} telah diperbarui menjadi '{status_baru}'.")
        else:
            print("Kendaraan dengan nomor plat tersebut tidak ditemukan.")
```

Kalau ada perubahan status kendaraan, misalnya dari Masuk jadi Keluar, admin bisa mengubah datanya melalui fungsi ini.

## Fungsi admin hapus data kendaraan
```python
    def hapus_data_kendaraan():
        nomor_plat = input("Masukkan Nomor Plat Kendaraan yang ingin dihapus: ")
        if nomor_plat in data_mobil:
            del data_mobil[nomor_plat]
            print(f"Kendaraan dengan nomor plat {nomor_plat} berhasil dihapus.")
        else:
            print("Kendaraan dengan nomor plat tersebut tidak ditemukan.")
```

Kalau ada kendaraan yang sudah tidak perlu lagi disimpan datanya, admin bisa menghapus dari sistem lewat fungsi ini.

## Fungsi user kendaraan masuk
```python
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
```

Fitur ini buat input data kendaraan yang baru masuk ke parkiran. Data kendaraan bakal langsung disimpan dan nomor parkir bakal dikasih otomatis.

## Fungsi user kendaraan keluar
```python
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
```

Kalau kendaraan mau keluar dari parkiran, kita input nomor parkirnya. Setelah itu, sistem bakal hitung biaya parkir berdasarkan durasi parkir kendaraan itu. Struk parkir juga akan dicetak buat pemilik kendaraan.

## Menu utama
```python
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
```

Fungsi ini menampilkan tampilan menu yang terdiri dari:

- Kendaraan Masuk
- Kendaraan Keluar
- Lihat Data Kendaraan
- Admin Login
- Keluar dari Sistem

## Cara menggunakan program

- Jalankan program dan pilih opsi yang sesuai dengan kebutuhanmu.
- Jika kamu adalah admin, silakan login terlebih dahulu untuk mengakses fitur admin.
- Untuk proses keluar masuk kendaraan, bisa melalui fitur yang telah tersedia di menu utama.
- Jika sudah selesai menggunakan fitur admin, jangan lupa keluar
