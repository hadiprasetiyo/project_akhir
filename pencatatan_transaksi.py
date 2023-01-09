import os # Module sistem Clear
import pwinput # Module untuk mengubah password menjadi Bintang
import csv # Penyimpanan Eksternal

print("==================================================")
print("               PENCATATAN TRANSAKSI               ")
print("                    PERUSAHAAN                    ")
print("==================================================")
print("                 KELOMPOK 5 SMT 2                 ")
print("   Fadilah Jaga Pratama              2109116065   ")
print("   Hadi Prasetiyo                    2109116070   ")
print("   Jamal                             2109116073   ")
print("==================================================")

# LOGIN ADMIN
admin = {"usernameadmin" : ["admin"],
        "passwordadmin" : ["admin"],
    }

# LOGIN USER
user = {"username": ["jamal","fadil", "iyok"],
        "password": ["6073", "6065", "2002"],
    }

# LINKED LIST
class Node:
    def __init__(self,param1,param2, param3):
        # isi
        self.namaTransaksi = param1
        self.jumlahTransaksi = param2
        self.waktuTransaksi = param3

        # pengait
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head =None
        self.tail = None

    # =========== CREATE DI LINKED LIST ==============
    # Fungsi menambahkan data Gerbong di dalam Linked List
    def add(self,param1,param2,param3):
        a=Node(param1,param2,param3)
        if self.head == None:
            self.head = a
            self.tail = a
        else:
            self.tail.next = a
            a.prev = self.tail
            self.tail = a

    # =========== READ DI LINKED LIST ===============
    # Fungsi menampilkan data NAMA, JUMLAH dan WAKTU TRANSAKSI di dalam Linked List
    def show(self):
        a=self.head
        indeksTransaksi = 0
        while a != None:
            indeksTransaksi = indeksTransaksi + 1
            print("\n=========================================")
            print("Transaksi ", indeksTransaksi)
            print("\nNama Transaksi : ",a.namaTransaksi)
            print("Jumlah Transaksi : ",a.jumlahTransaksi)
            print("Waktu Transaksi : ",a.waktuTransaksi)
            print("===========================================")
            a=a.next

    # ============ UPDATE DI LINKED LIST =================
    # Fungsi mengubah data menggunakan nomor data
    def update(self, param1 ,param2, param3, index):
        a = self.head
        gerbongBaru = Node(param1,param2,param3)
        for i in range(index-1):
            a=a.next
        if a == self.head:
            b = a.next
            gerbongBaru.next = b
            b.prev = gerbongBaru
            self.head = gerbongBaru
            return
        elif a == self.tail:
            b = a.prev
            gerbongBaru.prev = b
            b.next = gerbongBaru
            self.tail = gerbongBaru
            return
        b = a.prev
        c = a.next
        b.next = gerbongBaru
        gerbongBaru.prev = b
        c.prev = gerbongBaru
        gerbongBaru.next = c
    
    # ============ DELETE DI LINKED LIST =================
    # PENERAPAN QUEUE
    # Fungsi QUEUE untuk menghapus Data AWAL
    def hapusQueue(self):
        self.head = self.head.next
        self.head.prev = None
    
    # Fungsi untuk menghapus Data Tengah
    def hapusTengah(self,index):
        a = self.head
        for i in range(index-1):
            a=a.next
        if a == self.head : #Jika User Ingin Hapus Transaksi Pertama
            transaksi.hapusQueue()
            return
        elif a == self.tail: #Jika User Ingin Hapus Transaksi Terakhir
            transaksi.hapusStack()
            return
        b = a.prev
        c = a.next
        b.next = c
        c.prev = b
    
    # PENERAPAN STACK
    # Fungsi STACK untuk menghapus Data AKHIR
    def hapusStack(self):
        self.tail = self.tail.prev
        self.tail.next = None
    
    # Mengambil data untuk dimasukkan kedalam CSV
    def ambilDataCSV(self):
        with open('transaksi.csv', mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                nTransaksi.append(row["nama"])
                self.add(row["nama"],row["jumlah"],row["waktu"])

    # Menulis data untuk dimasukkan kedalam CSV
    def tulisDataCSV(self):
        with open('transaksi.csv', mode="w", newline='') as csv_file:
            fieldnames = ['nama', 'jumlah', 'waktu']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            a = self.head
            while(a != None):
                writer.writerow({"nama":a.namaTransaksi,"jumlah":a.jumlahTransaksi,"waktu":a.waktuTransaksi})  # menulis ke csv
                a = a.next  # traversal

transaksi = LinkedList() # VARIABEL UNTUK MENERAPKAN LINKEDLIST
nTransaksi = [] # LIST BANTU UNTUK SORTING & SEARCHING

# ================ RUMUS SORTING ===============
def partition(l, kiri, kanan):
    pivot = l[kiri]
    urutan = kiri+1
    for j in range(kiri+1,kanan):
        if l[j] <= pivot:
            l[urutan],l[j]=l[j],l[urutan]
            urutan += 1
    l[urutan-1],l[kiri] = l[kiri],l[urutan-1]
    return urutan
# Metode Quicksort untuk Sorting
def quicksort(data, kiri, kanan):
    if kanan <= kiri:
        return
    q = partition(data, kiri, kanan)
    quicksort(data, kiri, q-1)
    quicksort(data, q, kanan)
    return data

# ================ PENGIMPLEMENTASIAN SORTING ===============
# Fungsi untuk Mengurutkan Data
def tampilkanTerurut():
    if transaksi.head == None: # Jika Data Transaksi Kosong
        input("\nData Transaksi Belum Ada. Silahkan Tambah Daftar Transaksi Terlebih Dahulu.\nTekan Enter Untuk Kembali. ")
        os.system("cls")
        return
    transaksi2 = LinkedList() # MENGGUNAKAN VARIABEL BARU UNTUK MENERAPKAN SORTING DI DALAM LINKEDLIST
    quicksort(nTransaksi,0,len(nTransaksi))
    for i in range(len(nTransaksi)) :
        a = transaksi.head
        while a.namaTransaksi != nTransaksi[i]:
            a = a.next
        param1 = a.namaTransaksi
        param2 = a.jumlahTransaksi
        param3 = a.waktuTransaksi
        b = Node(param1,param2,param3)
        if transaksi2.head == None :
            transaksi2.head = b
            transaksi2.tail = b

        else :
            transaksi2.tail.next = b
            b.prev = transaksi2.tail
            transaksi2.tail = b
    transaksi2.show()

# =============== RUMUS SEARCHING ===============
# Metode Binary Search untuk Searching
def binarysearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============== PENGIMPLEMENTASIAN SEARCHING =============
# Fungsi untuk Mencari Data
def caridata():
    if transaksi.head == None: # Jika Data Transaksi Kosong
        input("\nData Transaksi Belum Ada. Silahkan Tambah Daftar Transaksi Terlebih Dahulu.\nTekan Enter Untuk Kembali. ")
        os.system("cls")
        return
    target = str(input("Silakan Masukkan Nama Transaksi yang Ingin Dicari : "))
    arr = quicksort(nTransaksi,0,len(nTransaksi))
    index = binarysearch(arr, target)

    a = transaksi.head
    while a!=None:
        if a.namaTransaksi == arr[index]:
            print("\n=========================================")
            print("\nNama Transaksi : ",a.namaTransaksi)
            print("Jumlah Transaksi : ",a.jumlahTransaksi)
            print("Waktu Transaksi : ",a.waktuTransaksi)
            print("===========================================")
        a = a.next

# ========== CREATE ===========
# Fungsi Tambah Data untuk dipanggil pada Menu Utama
def tambahdata():
    nama = str(input('\nMasukkan Nama Transaksi : '))
    if len(nama.strip()) != 0:
        try :
            jumlah = int(input('Masukkan jumlah Transaksi : '))
            waktu = str(input('Masukkan waktu Transaksi : ')) #.replace(' ', ''))
            if waktu.isspace() :
                input('\nMasukkan data dengan Benar.\nTekan Enter Untuk Kembali. ')
                os.system('cls')
                return
            elif waktu == '':
                input('\nMasukkan data dengan Benar.\nTekan Enter Untuk Kembali. ')
                os.system('cls')
                return

            nTransaksi.append(nama)
            transaksi.add(nama, jumlah, waktu)

        except ValueError :
            input('\nMasukkan Nominal dengan Benar.\nTekan Enter Untuk Kembali. ')
            os.system('cls')
    else :
        input('\nMasukkan Nama dengan Benar.\nTekan Enter Untuk Kembali. ')
        os.system('cls')

# ========== READ =============
# Fungsi Tampilkan Data untuk dipanggil pada Menu Utama
def tampilkanData():
    if transaksi.head == None: # Jika Data Transaksi Kosong
        input("\nData Transaksi Belum Ada. Silahkan Tambah Daftar Transaksi Terlebih Dahulu.\nTekan Enter Untuk Kembali. ")
        os.system("cls")
        return
    print("\nDaftar Transaksi\n")
    transaksi.show()

# ========= UPDATE ===========
# Fungsi Ubah Data untuk dipanggil pada Menu Utama
def ubahdata():
    if transaksi.head == None: # Jika Data Transaksi Kosong
        input("\nData Transaksi Belum Ada. Silahkan Tambah Daftar Transaksi Terlebih Dahulu.\nTekan Enter Untuk Kembali. ")
        os.system("cls")
        return
    index = int(input("\nTransaksi ke berapa yang ingin diubah : "))
    nama = str(input('\nMasukkan nama Transaksi baru: '))
    jumlah = int(input('Masukkan jumlah Transaksi baru : '))
    waktu = str(input('Masukkan waktu Transaksi baru : '))
    transaksi.update(nama,jumlah,waktu,index)
    nTransaksi[(index)-1] = nama

# ========= DELETE ===========
# Fungsi Hapus Data untuk dipanggil pada Menu Utama
def hapusdata():
    if transaksi.head == None: # Jika Data Transaksi Kosong
        input("\nData Transaksi Belum Ada. Silahkan Tambah Daftar Transaksi Terlebih Dahulu.\nTekan Enter Untuk Kembali. ")
        os.system("cls")
        return
    if transaksi.head.next == None: # Jika Data Hanya ada 1 buah
        transaksi.head = None
        transaksi.tail = None
        return
    print("""
    ====================================
    ==== Ingin menghapus data ke : =====
    ====================================
    | 1. Pertama                       |
    | 2. Pertengahan                   |
    | 3. Akhir                         |
    ====================================
    """)
    # try :
    pilih = input("Masukkan Pilihan Anda : ")

    # PENERAPAN QUEUE
    if pilih == '1' :
        transaksi.hapusQueue()
        del nTransaksi[0]

    elif pilih == '2' :
        index = int(input("\nTransaksi ke berapa yang ingin dihapus : "))
        transaksi.hapusTengah(index)
        del nTransaksi[(index)-1]

    # PENERAPAN STACK
    elif pilih == '3' :
        transaksi.hapusStack()
        del nTransaksi[len(nTransaksi)-1]

    else: # SALAH INPUT PILIHAN
        print("Pilihan tidak tersedia!")
        input("Tekan ENTER untuk Kembali. ")
        os.system("cls")
        menuAdmin()

# MENU ADMIN
def menuAdmin():
    print("""
    =====================================
    ============ MENU ADMIN =============
    =====================================
    | 1. Tampilkan Daftar Transaksi     |
    | 2. Tambah Transaksi               |
    | 3. Ubah Transaksi                 |
    | 4. Hapus Transaksi                |
    | 5. KEMBALI KE MENU LOGIN          |
    =====================================
    """)
    pilih = input("Masukkan Pilihan Anda : ")

    if pilih == '1' : # READ
        tampilkanData()
        menuAdmin()

    elif pilih == '2' : # CREATE
        tambahdata()
        menuAdmin()

    elif pilih == '3': # UPDATE
        ubahdata()
        menuAdmin()

    elif pilih == '4' : # DELETE
        hapusdata()
        tampilkanData()
        menuAdmin()
    
    elif pilih == '5' : # kembali ke menu login
        os.system("cls")
        pilih_login()

    else: # SALAH INPUT PILIHAN
        print("Pilihan tidak tersedia!")
        input("Tekan ENTER untuk Kembali. ")
        os.system("cls")
        menuAdmin()

#MENU DIREKTUR
def menuDirektur():
    print("""
    =======================================================
    ==================== MENU DIREKTUR ====================
    =======================================================
    | 1. Tampilkan Daftar Transaksi Secara Default        |
    | 2. Tampilkan Daftar Transaksi secara Terurut        |
    | 3. Cari Transaksi                                   |
    | 4. KEMBALI KE MENU LOGIN                            |
    =======================================================
    """)
    pilih = input("Masukkan Pilihan Anda : ")
    # try :
    if pilih == '1' : # menampilkan data Default
        tampilkanData()
        menuDirektur()
    elif pilih == '2': # SORTING
        tampilkanTerurut()
        menuDirektur()
    elif pilih == '3': # SEARCHING
        caridata()
        menuDirektur()
    elif pilih == '4' : # kembali ke menu login
        os.system("cls")
        pilih_login()
    
    else: # SALAH INPUT PILIHAN
        print("Pilihan tidak tersedia!")
        input("Tekan ENTER untuk Kembali. ")
        os.system("cls")
        menuDirektur()

# MENU LOGIN
def pilih_login():
    print("""
    ===============================
    == SILAHKAN PILIH MENU LOGIN ==
    ===============================
    | 1. Admin                    |
    | 2. Direktur                 |
    | 3. EXIT                     |
    ===============================
    """)
    
    while True:
        try :
            pilih = input("Masukkan Pilihan : ")

            # LOGIN ADMIN
            if pilih == '1' :
                usernameadmin = input ("Masukkan Username Admin : ") # MASUKKAN USERNAME ADMIN, AKAN MENGULANG JIKA USERNAME ATAU PASSWORD SALAH
                passwordadmin = pwinput.pwinput("Masukkan Password Admin : ") # MASUKKAN PASSWORD ADMIN, AKAN MENGULANG JIKA USERNAME ATAU PASSWORD SALAH
                search = admin.get("usernameadmin").index(usernameadmin)
                if admin.get("usernameadmin")[search] == usernameadmin and admin.get("passwordadmin")[search] == passwordadmin :
                    print("Login Berhasil")
                    menuAdmin()

            # LOGIN DIREKTUR
            elif pilih == '2' :
                username = input ("Masukkan Username Direktur : ") # MASUKKAN USERNAME, AKAN MENGULANG JIKA USERNAME ATAU PASSWORD SALAH
                password = pwinput.pwinput("Masukkan Password Direktur : ") # MASUKKAN PASSWORD, AKAN MENGULANG JIKA USERNAME ATAU PASSWORD SALAH
                cariin = user.get("username").index(username)
                if user.get("username")[cariin] == username and user.get("password")[cariin] == password :
                    print("Login Berhasil")
                    menuDirektur()

            # KELUAR PROGRAM
            elif pilih == '3' :
                print("Terima Kasih")
                transaksi.tulisDataCSV()
                raise SystemExit

            else: # SALAH INPUT PILIHAN
                print("Pilihan tidak tersedia!")
                input("Tekan ENTER untuk Kembali. ")
                os.system("cls")
                pilih_login()
        
        # Error jika salah
        except ValueError :
            print("Maaf Data Tidak Tersedia")
            input("Tekan ENTER untuk Kembali. ")
            os.system("cls")
            pilih_login()
transaksi.ambilDataCSV()
pilih_login()