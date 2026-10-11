import unittest
from keuangan_app.processing import Transaksi, AnalisisKeuangan

class TestKeuangan(unittest.TestCase):
    def setUp(self):
        self.analisis = AnalisisKeuangan()
        self.analisis.tambah_transaksi(Transaksi("Makanan", "Makan Siang", 25000))
        self.analisis.tambah_transaksi(Transaksi("Transport", "Bensin", 15000))

    def test_1_tambah_transaksi(self):
        self.assertEqual(len(self.analisis.daftar_transaksi), 2)

    def test_2_total_args(self):
        total = self.analisis.total_pengeluaran_args(100, 200, 300)
        self.assertEqual(total, 600)

    def test_3_kwargs_record(self):
        rec = self.analisis.buat_record_kwargs(id=1, status="Aktif")
        self.assertEqual(rec["status"], "Aktif")

    def test_4_filter_lambda(self):
        hasil = self.analisis.filter_berdasarkan_kategori("Makanan")
        self.assertEqual(len(hasil), 1)

    def test_5_urutkan(self):
        urut = self.analisis.urutkan_transaksi()
        self.assertEqual(urut[0].jumlah, 25000)

if __name__ == "__main__":
    unittest.main()