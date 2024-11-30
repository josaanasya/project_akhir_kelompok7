# Database pengguna (username dan password)
users_db = {}
data_mahasiswa = {}

# Fungsi untuk registrasi
def registrasi():
    while True:
        print("==== Registrasi ====")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # Periksa apakah username sudah ada
        if username in users_db:
            print("Username sudah terdaftar. Coba lagi dengan username yang berbeda.")
        else:
            # Simpan username dan password dalam dictionary
            users_db[username] = password
            print("Registrasi berhasil!")
            break

# Fungsi untuk login
def login():
    while True:
        print("==== Login ====")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # Periksa apakah username ada di dalam database
        if username not in users_db:
            print("Username tidak ditemukan. Pastikan username sudah terdaftar.")
            kembali = input("Tekan 0 untuk kembali ke menu utama atau ketik 'skip' untuk lanjut login: ")
            if kembali == "0":
                menu()
                return  
            elif kembali.lower() == "skip":
                continue
        # Periksa apakah password yang dimasukkan sesuai dengan yang ada di database
        if users_db[username] == password:
            print("Login berhasil!")
            menu_mahasiswa()  # Masuk ke menu mahasiswa setelah login berhasil
            break
        else:
            print("Password salah")
            kembali = input("Tekan 0 untuk kembali ke menu utama atau ketik 'skip' untuk lanjut login: ")
            if kembali == "0":
                menu()
                return  
            elif kembali.lower() == "skip":
                continue

# Fungsi untuk menambah data mahasiswa
def tambah_mahasiswa():
    print("==== Menambah Data Mahasiswa ====")
    nim = len(data_mahasiswa) + 240441100000 + 1  # Membuat NIM secara otomatis berdasarkan jumlah data
    nama = input("Masukkan nama lengkap: ")
    nisn = input("Masukkan Nisn: ")
    tempat_lahir = input("Masukkan tempat lahir: ")
    tgl_lahir = input("Masukkan tanggal lahir (format: dd/mm/yyyy): ")
    jenis_kelamin = input("Masukkan jenis kelamin (Laki laki/Perempuan ): ")
    alamat = input("Masukkan alamat lengkap: ")
    no_telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan alamat email: ")
    jurusan = input("Masukkan kode jurusan ( TI (Teknologi Informasi)/ SI (Sistem Informasi)/ SIA (Sistem Informasi Akutansi)/ IK (Ilmu Komputer)/ MG (Manajemen)/ AK (Akutansi)): ")

    if jurusan == "TI" or jurusan == "ti": 
        namajurusan = "Teknologi Informasi"
        biaya = 3000000
    elif jurusan == "SI" or jurusan == "si":
        namajurusan = "Sistem Informasi"
        biaya = 2400000
    elif jurusan == "SIA" or jurusan == "sia":
        namajurusan = "Sistem Informasi Akutansi"
        biaya = 2000000
    elif jurusan == "IK" or jurusan == "ik":
        namajurusan = "Ilmu Komputer"
        biaya = 2000000
    elif jurusan == "MG" or jurusan == "mg":
        namajurusan = "Manajemen"
        biaya = 2000000
    elif jurusan == "AK" or jurusan == "ak":
        namajurusan = "Akutansi"
        biaya = 2000000
    else:
        namajurusan = "Kode yang Anda masukkan salah"
        biaya = 0

    simpan_data = input("Apakah kamu ingin menyimpan data ini? (y/t): ")
    if simpan_data.lower() == "t":
        print("Data tidak tersimpan.")
    elif simpan_data.lower() == "y":
        mahasiswa = {
            'Nama': nama,
            'NISN': nisn,
            'Tempat Lahir': tempat_lahir,
            'Tanggal Lahir': tgl_lahir,
            'Jenis Kelamin': jenis_kelamin,
            'Alamat': alamat,
            'No Telepon': no_telepon,
            'Email': email,
            'jurusan' : namajurusan,
            'kode Jurusan': jurusan,
            'Biaya': biaya
        }

        # Simpan data mahasiswa
        data_mahasiswa[nim] = mahasiswa
        print(f"Data mahasiswa berhasil disimpan dengan NIM {nim}.")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_data_mahasiswa():
    if not data_mahasiswa:
        print("Belum ada mahasiswa yang terdaftar.")
        return
    
    print("\n==== Data Mahasiswa ====")
    for nim, mahasiswa in data_mahasiswa.items():
        print(f"------------------------\nNIM: {nim}")
        for key, value in mahasiswa.items():
            print(f"{key}: {value}")
        print("--------------------------")

# Fungsi untuk mengubah data mahasiswa
def ubah_data_mahasiswa():
    nim = int(input("Masukkan NIM mahasiswa yang ingin diubah: "))
    
    if nim not in data_mahasiswa:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        return
    
    print("Pilih data yang ingin diubah:")
    print("1. Nama")
    print("2. NISN")
    print("3. Tempat Lahir")
    print("4. Tanggal Lahir")
    print("5. Jenis Kelamin")
    print("6. Alamat")
    print("7. No Telepon")
    print("8. Email")
    print("9. kode jurusan")
    print("10. Semua data")
    
    pilihan = input("Pilih yang akan diubah (1-10): ")
    mahasiswa = data_mahasiswa[nim]
    
    if pilihan == "1":
        mahasiswa['Nama'] = input("Masukkan Nama baru: ")
    elif pilihan == "2":
        mahasiswa['NISN'] = input("Masukkan NISN baru: ")
    elif pilihan == "3":
        mahasiswa['Tempat Lahir'] = input("Masukkan tempat lahir baru: ")
    elif pilihan == "4":
        mahasiswa['Tanggal Lahir'] = input("Masukkan tanggal lahir baru: ")
    elif pilihan == "5":
        mahasiswa['Jenis Kelamin'] = input("Masukkan jenis kelamin baru (L/P): ")
    elif pilihan == "6":
        mahasiswa['Alamat'] = input("Masukkan alamat baru: ")
    elif pilihan == "7":
        mahasiswa['No Telepon'] = input("Masukkan nomor telepon baru: ")
    elif pilihan == "8":
        mahasiswa['Email'] = input("Masukkan email baru: ")
    elif pilihan == "9":
        jurusan = input(" TI (Teknologi Informasi)/ SI (Sistem Informasi)/ SIA (Sistem Informasi Akutansi)/ IK (Ilmu Komputer)/ MG (Manajemen)/ AK (Akutansi): ")
        if jurusan == "TI" or jurusan == "ti":
            mahasiswa['jurusan'] = "Teknologi Informasi"
            mahasiswa['kode Jurusan'] = "TI"
            mahasiswa['Biaya'] = 3000000
        elif jurusan == "SI" or jurusan == "si":
            mahasiswa['jurusan'] = "Sistem Informasi"
            mahasiswa['kode Jurusan'] = "SI"
            mahasiswa['Biaya'] = 2400000
        elif jurusan == "SIA" or jurusan == "sia":
            mahasiswa['jurusan'] = "Sistem Informasi Akutansi"
            mahasiswa['kode Jurusan'] = "SIA"
            mahasiswa['Biaya'] = 2000000
        elif jurusan == "IK" or jurusan == "ik":
            mahasiswa['jurusan'] = "Ilmu Komputer"
            mahasiswa['kode Jurusan'] = "IK"
            mahasiswa['Biaya'] = 2000000
        elif jurusan == "MG" or jurusan == "mg":
            mahasiswa['jurusan'] = "Manajemen"
            mahasiswa['kode Jurusan'] = "MG"
            mahasiswa['Biaya'] = 2000000
        elif jurusan == "AK" or jurusan == "ak":
            mahasiswa['jurusan'] = "Akutansi"
            mahasiswa['kode Jurusan'] = "AK"
            mahasiswa['Biaya'] = 2000000
        else:
            print("Kode jurusan tidak valid.")
            return
    elif pilihan == "10":
        mahasiswa['Nama'] = input("Masukkan nama baru: ")
        mahasiswa['NISN'] = input("Masukkan NISN baru: ")
        mahasiswa['Tempat Lahir'] = input("Masukkan tempat lahir baru: ")
        mahasiswa['Tanggal Lahir'] = input("Masukkan tanggal lahir baru: ")
        mahasiswa['Jenis Kelamin'] = input("Masukkan jenis kelamin baru (L/P): ")
        mahasiswa['Alamat'] = input("Masukkan alamat baru: ")
        mahasiswa['No Telepon'] = input("Masukkan nomor telepon baru: ")
        mahasiswa['Email'] = input("Masukkan email baru: ")
        jurusan = input(" TI (Teknologi Informasi)/ SI (Sistem Informasi)/ SIA (Sistem Informasi Akutansi)/ IK (Ilmu Komputer)/ MG (Manajemen)/ AK (Akutansi): ")
        if jurusan == "TI" or jurusan == "ti":
            mahasiswa['jurusan'] = "Teknologi Informasi"
            mahasiswa['kode Jurusan'] = "TI"
            mahasiswa['Biaya'] = 3000000
        elif jurusan == "SI" or jurusan == "si":
            mahasiswa['jurusan'] = "Sistem Informasi"
            mahasiswa['kode Jurusan'] = "SI"
            mahasiswa['Biaya'] = 2400000
        elif jurusan == "SIA" or jurusan == "sia":
            mahasiswa['jurusan'] = "Sistem Informasi Akutansi"
            mahasiswa['kode Jurusan'] = "SIA"
            mahasiswa['Biaya'] = 2000000
        elif jurusan == "IK" or jurusan == "ik":
            mahasiswa['jurusan'] = "Ilmu Komputer"
            mahasiswa['kode Jurusan'] = "IK"
            mahasiswa['Biaya'] = 2000000
        elif jurusan == "MG" or jurusan == "mg":
            mahasiswa['jurusan'] = "Manajemen"
            mahasiswa['kode Jurusan'] = "MG"
            mahasiswa['Biaya'] = 2000000
        elif jurusan == "AK" or jurusan == "ak":
            mahasiswa['jurusan'] = "Akutansi"
            mahasiswa['kode Jurusan'] = "AK"
            mahasiswa['Biaya'] = 2000000
        else:
            print("Kode jurusan tidak valid.")
            return
    else:
        print("Pilihan tidak valid.")
        return
    
    print("Data mahasiswa berhasil diubah.")

# Fungsi untuk menghapus data mahasiswa
def hapus_data_mahasiswa():
    nim = int(input("Masukkan NIM mahasiswa yang ingin dihapus: "))
    
    if nim not in data_mahasiswa:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        return
    
    del data_mahasiswa[nim]
    print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")


# Menu untuk mengelola data mahasiswa
def menu_mahasiswa():
    while True:
        print("\n==== Menu Mahasiswa ====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_data_mahasiswa()
        elif pilihan == "3":
            ubah_data_mahasiswa()
        elif pilihan == "4":
            hapus_data_mahasiswa()
        elif pilihan == "5":
            print("Keluar dari menu mahasiswa.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
            
# Menu utama program
def menu():
    while True:
        print("\nSELAMAT DATANG DI KAMPUS TRUNOJOYO MADURA")
        print("==== Menu ====")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
    
        pilih = input("Pilih opsi (1/2/3): ")
    
        if pilih == "1":
            registrasi()
        elif pilih == "2":
            login()
        elif pilih == "3":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih 1")
menu()
