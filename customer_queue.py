antrian = []

def tambah_transaksi(antrian, nama_pelanggan, jenis_transaksi):
    transaksi = (nama_pelanggan, jenis_transaksi)
    antrian.append(transaksi)
    print("Transaksi dari", nama_pelanggan, "dengan jenis", jenis_transaksi, "berhasil ditambahkan ke dalam antrean.")

def transaksi_berikutnya(antrian):
    if len(antrian) == 0:
        print("Antrean kosong, tidak ada transaksi yang dapat ditampilkan.")
    else:
        nama_pelanggan, jenis_transaksi = antrian[0]
        print("Transaksi berikutnya adalah dari", nama_pelanggan, "dengan jenis", jenis_transaksi)

def hapus_transaksi(antrian):
    if len(antrian) == 0:
        print("Antrean kosong, tidak ada transaksi yang dapat dihapus.")
    else:
        nama_pelanggan, jenis_transaksi = antrian[0]
        print("Transaksi dari", nama_pelanggan, "dengan jenis", jenis_transaksi, "berhasil dihapus dari antrean.")
        antrian.pop(0)

while True:
    print("\nAntrean saat ini:", antrian)
    print("Menu:")
    print("1. Tambah Transaksi")
    print("2. Transaksi Berikutnya")
    print("3. Hapus Transaksi")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        jenis_transaksi = input("Masukkan jenis transaksi (misalnya pembelian/tukar tambah/pengembalian): ")
        tambah_transaksi(antrian, nama_pelanggan, jenis_transaksi)
    elif pilihan == "2":
        transaksi_berikutnya(antrian)
        if len(antrian) > 0:
            antrian.pop(0)
    elif pilihan == "3":
        hapus_transaksi(antrian)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
