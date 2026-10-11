class NegatifValueError(Exception):
    pass

def validasi_angka(prompt: str) -> float:
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < 0:
                raise NegatifValueError("Nilai tidak boleh negatif!")
            return nilai
        except ValueError:
            print("[Error] Masukkan angka yang valid.")
        except NegatifValueError as e:
            print(f"[Peringatan] {e}")

def validasi_string(prompt: str) -> str:
    while True:
        teks = input(prompt).strip()
        try:
            assert len(teks) > 0, "Field input tidak boleh kosong!"
            return teks
        except AssertionError as e:
            print(f"[Peringatan] {e}")