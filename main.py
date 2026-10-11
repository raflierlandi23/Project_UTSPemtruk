from keuangan_app.fileio import inisialisasi_file, tambah_data_file, baca_data_file, tulis_laporan_file
from keuangan_app.processing import Transaksi, AnalisisKeuangan
from keuangan_app.validasi import validasi_angka, validasi_string

def main():
    inisialisasi_file()
    sistem = AnalisisKeuangan()

    data_mentah = baca_data_file()
    for baris in data_mentah[1:]:
        if len(baris) == 3:
            sistem.tambah_transaksi(Transaksi(baris[0], baris[1], float(baris[2])))

    while True:
        print("\n==============================")
        print("  APLIKASI KEUANGAN PRIBADI   ")
        print("==============================")
        print("1. Tambah Transaksi")
        print("2. Lihat Daftar Transaksi")
        print("3. Buat Laporan ke File")
        print("4. Jalankan Unit Test")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            kategori = validasi_string("Masukkan Kategori: ")
            keterangan = validasi_string("Masukkan Keterangan: ")
            jumlah = validasi_angka("Masukkan Jumlah Nominal: Rp ")

            t = Transaksi(kategori=kategori, keterangan=keterangan, jumlah=jumlah)
            sistem.tambah_transaksi(t)
            tambah_data_file(kategori, keterangan, jumlah)
            print("[Sukses] Transaksi berhasil disimpan!")

        elif pilihan == "2":
            print("\n--- DAFTAR TRANSAKSI TERURUT ---")
            for t in sistem.urutkan_transaksi():
                print(f"• [{t.kategori}] {t.keterangan} : Rp {t.jumlah:,.0f}")

        elif pilihan == "3":
            total = sum([t.jumlah for t in sistem.daftar_transaksi])
            laporan = f"LAPORAN KEUANGAN\nTotal Pengeluaran: Rp {total:,.0f}\n"
            tulis_laporan_file(laporan)

        elif pilihan == "4":
            print("\n--- MENJALANKAN UNIT TEST ---")
            import unittest
            from keuangan_app.testing import TestKeuangan
            suite = unittest.TestLoader().loadTestsFromTestCase(TestKeuangan)
            unittest.TextTestRunner().run(suite)

        elif pilihan == "5":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("[Error] Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()