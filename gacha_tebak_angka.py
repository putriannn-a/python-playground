import random
ANGKA_MAKS = 20        
BATAS_LUCK = 75
HARGA_GACHA = 80
HARGA_POTION = 30
LUCK_POTION = 20
HARGA_PET_TOKO = 200
LEBAR = 46              

player = {
    "poin": 100,
    "potion": 0,
    "pet": {"nama": "belum ada", "luck": 0},
    "armor": {"nama": "belum ada", "luck": 0, "bonus": 0},
}

pet_toko = {"nama": "hamster", "luck": 4}

hadiah_gacha = {
    ("pet", "common"): [
        {"nama": "kelinci", "luck": 3},
        {"nama": "kucing", "luck": 3},
    ],
    ("pet", "uncommon"): [
        {"nama": "rubah", "luck": 5},
        {"nama": "penguin", "luck": 5},
    ],
    ("pet", "rare"): [
        {"nama": "rusa", "luck": 8},
        {"nama": "serigala", "luck": 8},
        {"nama": "beruang", "luck": 8},
    ],
    ("pet", "epic"): [
        {"nama": "harimau", "luck": 12},
        {"nama": "naga", "luck": 12},
        {"nama": "singa", "luck": 12},
    ],
    ("pet", "legendary"): [
        {"nama": "phoenix", "luck": 20},
    ],
    ("armor", "common"): [
        {"nama": "wooden armor", "luck": 3, "bonus": 5},
    ],
    ("armor", "uncommon"): [
        {"nama": "bronze armor", "luck": 5, "bonus": 10},
    ],
    ("armor", "rare"): [
        {"nama": "crystal armor", "luck": 10, "bonus": 15},
    ],
    ("armor", "epic"): [
        {"nama": "shadow armor", "luck": 15, "bonus": 20},
    ],
    ("armor", "legendary"): [
        {"nama": "celestial armor", "luck": 20, "bonus": 25},
    ],
}


def garis(karakter="-"):
    print(karakter * LEBAR)

def judul(teks):
    print()
    garis("=")
    print(teks.center(LEBAR))
    garis("=")

def jeda():
    input("\n  Tekan Enter untuk lanjut...")


def tampilkan_aturan():
    judul("CARA BERMAIN")
    print("  1. Tebak SATU angka (1-" + str(ANGKA_MAKS) + ") tiap ronde.")
    print("  2. Poin yang didapat:")
    print("       PAS    (selisih 0)    = 100 poin")
    print("       DEKAT  (selisih 1-3)  =  50 poin")
    print("       JAUH   (selisih > 3)  =  10 poin")
    print("  3. LUCK = peluang tebakanmu otomatis jadi PAS.")
    print("     Luck dari pet + armor + lucky potion.")
    print("  4. ARMOR memberi bonus poin setiap ronde,")
    print("     bahkan saat tebakanmu jauh.")
    print("  5. Pakai poin di SHOP dan GACHA untuk")
    print("     mendapat luck lebih besar.")
    garis("=")
    jeda()

def minta_angka(pesan, kecil, besar):
    while True:
        try:
            angka = int(input(pesan))
        except ValueError:
            print("  SALAH: Harus berupa angka.")
            continue
        if kecil <= angka <= besar:
            return angka
        print(f"  SALAH: Angka harus {kecil} sampai {besar}.")

def tanya_potion():
    while True:
        jawab = input("  Pakai lucky potion? (y/n): ").strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  SALAH: Ketik y atau n saja.")

def hitung_luck(player, pakai_potion):
    luck = player["pet"]["luck"] + player["armor"]["luck"]
    if pakai_potion:
        luck += LUCK_POTION
    if luck > BATAS_LUCK:
        luck = BATAS_LUCK
    return luck

def tampilkan_status(player):
    luck = hitung_luck(player, False)
    judul("STATUS PEMAIN")
    print(f"  Poin   : {player['poin']}")
    print(f"  Potion : {player['potion']}")
    print(f"  Pet    : {player['pet']['nama']} (+{player['pet']['luck']} luck)")
    print(f"  Armor  : {player['armor']['nama']} "
          f"(+{player['armor']['luck']} luck, +{player['armor']['bonus']} bonus poin)")
    print(f"  LUCK   : {luck}%")
    garis("=")

def main_tebak_angka(player):
    judul("TEBAK ANGKA")

    pakai_potion = False
    if player["potion"] > 0:
        if tanya_potion():
            player["potion"] -= 1
            pakai_potion = True
            print(f"  Potion terpakai! (+{LUCK_POTION} luck ronde ini)")

    luck = hitung_luck(player, pakai_potion)
    print(f"  Luck kamu ronde ini: {luck}%")
    tebakan = minta_angka(f"  Tebakanmu (1-{ANGKA_MAKS}): ", 1, ANGKA_MAKS)

    rahasia = random.randint(1, ANGKA_MAKS)
    undi = random.randint(1, 100)
    luck_bekerja = False
    if undi <= luck:
        rahasia = tebakan
        luck_bekerja = True

    selisih = abs(tebakan - rahasia)

    if selisih == 0:
        poin_dasar = 100
        pesan = "TEPAT SEKALI!"
    elif selisih <= 3:
        poin_dasar = 50
        pesan = "HAMPIR KENA!"
    else:
        poin_dasar = 10
        pesan = "Jauh banget kawan, yuk coba lagi!"

    bonus = player["armor"]["bonus"]
    total = poin_dasar + bonus
    player["poin"] += total

    print()
    garis("-")
    print(f"  >> {pesan} <<")
    if luck_bekerja:
        print("  (Luck mu bekerja dan menyelamatkan tebakanmu!)")
    garis("-")
    print(f"  Tebakanmu     : {tebakan}")
    print(f"  Angka rahasia : {rahasia}")
    print(f"  Selisih       : {selisih}")
    garis("-")
    print(f"  Poin dasar    : {poin_dasar}")
    print(f"  Bonus armor   : +{bonus}")
    print(f"  TOTAL         : +{total}")
    print(f"  Poin sekarang : {player['poin']}")
    garis("-")
    jeda()


def buka_shop(player):
    while True:
        judul("SHOP")
        print(f"  Poin kamu: {player['poin']}")
        garis("-")
        print(f"  [1] Lucky Potion  - {HARGA_POTION} poin")
        print(f"      (+{LUCK_POTION} luck, berlaku 1 ronde)")
        print(f"  [2] Pet {pet_toko['nama']}  - {HARGA_PET_TOKO} poin")
        print(f"      (+{pet_toko['luck']} luck, permanen)")
        print("  [0] Kembali")
        garis("-")
        pilihan = minta_angka("  Pilih: ", 0, 2)

        if pilihan == 0:
            break
        elif pilihan == 1:
            if player["poin"] < HARGA_POTION:
                print("  [!] Poin tidak cukup.")
            else:
                player["poin"] -= HARGA_POTION
                player["potion"] += 1
                print("  Berhasil membeli 1 lucky potion!")
        else:
            if pet_toko["luck"] <= player["pet"]["luck"]:
                print("  [!] Petmu sekarang sudah sama atau lebih bagus.")
            elif player["poin"] < HARGA_PET_TOKO:
                print("  [!] Poin tidak cukup.")
            else:
                player["poin"] -= HARGA_PET_TOKO
                player["pet"] = {"nama": pet_toko["nama"], "luck": pet_toko["luck"]}
                print(f"  Berhasil membeli pet {pet_toko['nama']}!")
        jeda()


def tarik_gacha(player):
    judul("GACHA")
    if player["poin"] < HARGA_GACHA:
        print(f"  [!] Poin tidak cukup (butuh {HARGA_GACHA}).")
        jeda()
        return

    player["poin"] -= HARGA_GACHA

    roll = random.randint(1, 100)
    if roll <= 50:
        rarity = "common"
    elif roll <= 75:
        rarity = "uncommon"
    elif roll <= 90:
        rarity = "rare"
    elif roll <= 98:
        rarity = "epic"
    else:
        rarity = "legendary"

    tipe = random.choice(["pet", "armor"])
    hadiah = random.choice(hadiah_gacha[(tipe, rarity)])

    print(f"  Kamu menarik gacha... (-{HARGA_GACHA} poin)")
    garis("-")
    print(f"  Rarity : {rarity.upper()}")
    print(f"  Tipe   : {tipe}")
    print(f"  Hadiah : {hadiah['nama']} (+{hadiah['luck']} luck)")
    garis("-")

    if hadiah["luck"] > player[tipe]["luck"]:
        player[tipe] = dict(hadiah)
        print("  Item baru langsung dipakai!")
    else:
        print("  Tidak lebih bagus dari yang sedang kamu pakai.")
    print(f"  Poin sekarang: {player['poin']}")
    jeda()


def main():
    judul("Welcome To GuessNum!")
    print("  Pilih menu 4 untuk membaca cara bermain.")
    while True:
        tampilkan_status(player)
        print("  [1] Main tebak angka")
        print("  [2] Shop")
        print(f"  [3] Gacha ({HARGA_GACHA} poin)")
        print("  [4] Cara bermain")
        print("  [5] Keluar")
        garis("-")
        pilihan = minta_angka("  Pilih menu (1-5): ", 1, 5)

        if pilihan == 1:
            main_tebak_angka(player)
        elif pilihan == 2:
            buka_shop(player)
        elif pilihan == 3:
            tarik_gacha(player)
        elif pilihan == 4:
            tampilkan_aturan()
        else:
            print("\n  Terima kasih sudah bermain!")
            break


main()