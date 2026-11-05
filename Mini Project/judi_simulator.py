import random

#PERATURAN
UANG_AWAL = 100000
TARUHAN_MIN = 1000
PELUANG_MENANG = 40
KEUNTUNGAN_MENANG = 2
PINJAM_MIN = 100000
PINJAM_MAKS = 1000000
BUNGA_AWAL = 10            
KENAIKAN_BUNGA = 10        

#DATA PEMAIN
pemain = {
    "uang": UANG_AWAL,
    "tabungan": 0,
    "hutang": 0,
    "bunga": BUNGA_AWAL,
}


#FUNCTION 
def rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


def minta_angka(pesan, kecil, besar):
    while True:
        try:
            angka = int(input(pesan))
        except ValueError:
            print("[!] Harus berupa angka.")
            continue
        if kecil <= angka <= besar:
            return angka
        print(f"[!] Angka harus {rupiah(kecil)} sampai {rupiah(besar)}.")


def minta_pilihan(pesan, kecil, besar):
    while True:
        try:
            angka = int(input(pesan))
        except ValueError:
            print("[!] Harus berupa angka.")
            continue
        if kecil <= angka <= besar:
            return angka
        print(f"[!] Pilih nomor {kecil} sampai {besar}.")


def tampilkan_status(pemain):
    print("BALANCE".center(40))
    print("=" * 40)
    print(f"Uang     : {rupiah(pemain['uang'])}")
    print(f"Tabungan : {rupiah(pemain['tabungan'])}")
    print(f"Hutang   : {rupiah(pemain['hutang'])}")
    if pemain["hutang"] > 0:
        print(f"Bunga    : {pemain['bunga']}%")
    print("=" * 40)


# JUDI
def judi(pemain):
    print()
    print("=" * 40)
    print("JUDI".center(40))
    print("=" * 40)

    if pemain["uang"] < TARUHAN_MIN:
        print(f"[!] Uangmu kurang dari taruhan minimum ({rupiah(TARUHAN_MIN)}).")
        return

    print(f"Uangmu: {rupiah(pemain['uang'])}")
    print(f"Taruhan minimum: {rupiah(TARUHAN_MIN)}")
    taruhan = minta_angka("Taruhan: ", TARUHAN_MIN, pemain["uang"])

    undi = random.randint(1, 100)
    print("-" * 40)
    if undi <= PELUANG_MENANG:
        hadiah = taruhan * KEUNTUNGAN_MENANG
        pemain["uang"] += hadiah
        print(f"MENANG! +{rupiah(hadiah)}")
    else:
        pemain["uang"] -= taruhan
        print(f"KALAH! -{rupiah(taruhan)}")
    print(f"Uang sekarang: {rupiah(pemain['uang'])}")
    print("-" * 40)


#TABUNGAN
def menu_tabungan(pemain):
    while True:
        print("=" * 40)
        print("TABUNGAN".center(40))
        print("=" * 40)
        print(f"Uang     : {rupiah(pemain['uang'])}")
        print(f"Tabungan : {rupiah(pemain['tabungan'])}")
        print("-" * 40)
        print("[1] Deposit")
        print("[2] Tarik")
        print("[0] Kembali")
        print("-" * 40)
        pilihan = minta_pilihan("Pilih: ", 0, 2)

        if pilihan == 0:
            break
        elif pilihan == 1:
            if pemain["uang"] == 0:
                print("[!] Kamu tidak punya uang.")
            else:
                jumlah = minta_angka("Jumlah deposit: ", 1, pemain["uang"])
                pemain["uang"] -= jumlah
                pemain["tabungan"] += jumlah
                print(f"Berhasil menabung {rupiah(jumlah)}.")
        else:
            if pemain["tabungan"] == 0:
                print("[!] Tabungan kosong.")
            else:
                jumlah = minta_angka("Jumlah tarik: ", 1, pemain["tabungan"])
                pemain["tabungan"] -= jumlah
                pemain["uang"] += jumlah
                print(f"Berhasil menarik {rupiah(jumlah)}.")


#PINJAMAN
def pinjam(pemain):
    print()
    print("=" * 40)
    print("PINJAM UANG".center(40))
    print("=" * 40)

    if pemain["hutang"] == 0:
        pemain["bunga"] = BUNGA_AWAL
        print(f"Bunga: {pemain['bunga']}%")
        jumlah_diberi = minta_angka(
            f"Pinjam berapa? ({rupiah(PINJAM_MIN)} - {rupiah(PINJAM_MAKS)}): ",
            PINJAM_MIN, PINJAM_MAKS)
    else:
        print("[PERINGATAN] Kamu masih punya hutang!")
        print("Pinjaman hanya SETENGAH dari yang diminta,")
        print("dan bunga NAIK.")
        pemain["bunga"] += KENAIKAN_BUNGA
        print(f"Bunga sekarang: {pemain['bunga']}%")
        jumlah_diminta = minta_angka(
            f"Pinjam berapa? ({rupiah(PINJAM_MIN)} - {rupiah(PINJAM_MAKS)}): ",
            PINJAM_MIN, PINJAM_MAKS)
        jumlah_diberi = jumlah_diminta // 2
        print(f"Kamu hanya mendapat {rupiah(jumlah_diberi)}.")

    bunga_rupiah = jumlah_diberi * pemain["bunga"] // 100
    tambahan_hutang = jumlah_diberi + bunga_rupiah

    pemain["uang"] += jumlah_diberi
    pemain["hutang"] += tambahan_hutang

    print("-" * 40)
    print(f"Uang diterima : {rupiah(jumlah_diberi)}")
    print(f"Bunga         : {pemain['bunga']}%")
    print(f"Hutang tambah : {rupiah(tambahan_hutang)}")
    print(f"Total hutang  : {rupiah(pemain['hutang'])}")
    print("-" * 40)


def bayar_hutang(pemain):
    print()
    print("=" * 40)
    print("BAYAR HUTANG".center(40))
    print("=" * 40)

    if pemain["hutang"] == 0:
        print("Kamu tidak punya hutang.")
        return

    batas = min(pemain["uang"], pemain["hutang"])
    if batas == 0:
        print("[!] Uangmu habis, tidak bisa membayar.")
        return

    print(f"Hutang : {rupiah(pemain['hutang'])}")
    print(f"Uang   : {rupiah(pemain['uang'])}")
    jumlah = minta_angka("Bayar berapa: ", 1, batas)
    pemain["uang"] -= jumlah
    pemain["hutang"] -= jumlah
    print(f"Berhasil membayar {rupiah(jumlah)}.")

    if pemain["hutang"] == 0:
        pemain["bunga"] = BUNGA_AWAL
        print("HUTANG LUNAS! Bunga kembali normal.")
    else:
        print(f"Sisa hutang: {rupiah(pemain['hutang'])}")


def menu_pinjaman(pemain):
    while True:
        print()
        print("=" * 40)
        print("PINJAMAN".center(40))
        print("=" * 40)
        print(f"Hutang: {rupiah(pemain['hutang'])}")
        print("-" * 40)
        print("[1] Pinjam uang")
        print("[2] Bayar hutang")
        print("[0] Kembali")
        print("-" * 40)
        pilihan = minta_pilihan("Pilih: ", 0, 2)

        if pilihan == 0:
            break
        elif pilihan == 1:
            pinjam(pemain)
        else:
            bayar_hutang(pemain)


#MENU UTAMA
def main():
    print("=" * 40)
    print("SIMULASI JUDI".center(40))
    print("=" * 40)
    while True:
        tampilkan_status(pemain)
        print("[1] Judi")
        print("[2] Tabungan")
        print("[3] Pinjaman")
        print("[4] Keluar")
        print("-" * 40)
        pilihan = minta_pilihan("Pilih menu (1-4): ", 1, 4)

        if pilihan == 1:
            judi(pemain)
        elif pilihan == 2:
            menu_tabungan(pemain)
        elif pilihan == 3:
            menu_pinjaman(pemain)
        else:
            print("Terima kasih sudah bermain!")
            break

        if (pemain["uang"] < TARUHAN_MIN
                and pemain["tabungan"] == 0
                and pemain["hutang"] > 0):
            print()
            print("=" * 40)
            print("BANGKRUT! Game berakhir.")
            print(f"Hutang tersisa: {rupiah(pemain['hutang'])}")
            print("=" * 40)
            break


main()