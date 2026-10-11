class Transaksi:
    def __init__(self, kategori: str, keterangan: str, jumlah: float):
        self.kategori = kategori
        self.keterangan = keterangan
        self.jumlah = jumlah

class AnalisisKeuangan:
    def __init__(self):
        self.daftar_transaksi = []

    def tambah_transaksi(self, transaksi: Transaksi):
        self.daftar_transaksi.append(transaksi)

    def total_pengeluaran_args(self, *args: float) -> float:
        return sum(args)

    def buat_record_kwargs(self, **kwargs) -> dict:
        return kwargs

    def filter_berdasarkan_kategori(self, target_kategori: str) -> list:
        return list(filter(lambda t: t.kategori.lower() == target_kategori.lower(), self.daftar_transaksi))

    def urutkan_transaksi(self) -> list:
        return sorted(self.daftar_transaksi, key=lambda t: t.jumlah, reverse=True)