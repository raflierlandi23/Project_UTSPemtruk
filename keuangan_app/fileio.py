NAMA_FILE = "data_keuangan.txt"
FILE_LAPORAN = "laporan_ringkasan.txt"

def inisialisasi_file():
    try:
        with open(NAMA_FILE, "x") as f:
            f.write("Kategori,Keterangan,Jumlah\n")
    except FileExistsError:
        pass

def tambah_data_file(kategori: str, keterangan: str, jumlah: float):
    with open(NAMA_FILE, "a") as f:
        f.write(f"{kategori},{keterangan},{jumlah}\n")

def baca_data_file() -> list:
    data = []
    try:
        with open(NAMA_FILE, "r") as f:
            for baris in f:
                data.append(baris.strip().split(","))
        return data
    except FileNotFoundError:
        print("[Info] Belum ada file data ditemukan.")
        return []

def tulis_laporan_file(teks_laporan: str):
    with open(FILE_LAPORAN, "w") as f:
        f.write(teks_laporan)
    print(f"[Sukses] Laporan disimpan ke {FILE_LAPORAN}")