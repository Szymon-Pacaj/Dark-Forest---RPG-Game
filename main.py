import random
import sys


def ScreenPodstawowy():
    print("=============================\n         DARK FOREST         \n=============================")
    print(gracz['name'])
    print(f"HP = {gracz['hp']}/{gracz['max_HP']}")
    print(f"Obrażenia = {gracz['obrazenia_zakres']}")
    print(f"LVL = {gracz['lvl']}       XP = {gracz['xp']}/{gracz['max_XP']}")
    print(f"Złoto = {gracz['gold']}")
    if goldx2 > 0:
        print(f"Podwajane złoto: {goldx2}")
    if xpx2 > 0:
        print(f"Podwajane xp: {xpx2}")
    if xpx0 > 0:
        print(f"Blokada rozwoju (LVL i XP): {xpx0}")
    print("\n1. Idź do lasu.\n2. Idź do kopalni.\n3. Ekwipunek\n4. Sklep\n5. Kowal")




def walka(PotworHP, PotworObrazeniaMin, PotworObrazeniaMax, XPMin, XPMax, GoldMin, GoldMax, grupa):
    global xpx2, xpx0, goldx2
    potwor['hp'] = PotworHP
    potwor['xp_min'] = XPMin
    potwor['xp_max'] = XPMax
    potwor['gold_min'] = GoldMin
    potwor['gold_max'] = GoldMax
    potwor["obrazenia_min"] = PotworObrazeniaMin
    potwor["obrazenia_max"] = PotworObrazeniaMax
    if zbroja == 1:
        potwor['obrazenia_min'] -= 1
        potwor['obrazenia_max'] -= 1
    elif zbroja == 2:
        potwor['obrazenia_min'] -= 3
        potwor['obrazenia_max'] -= 3
    elif zbroja == 3:
        potwor['obrazenia_min'] -= 5
        potwor['obrazenia_max'] -= 5
    elif zbroja == 4:
        potwor['obrazenia_min'] -= 10
        potwor['obrazenia_max'] -= 10
    print(f"{gracz['name']}: {gracz['hp']}hp\npotwór: {potwor['hp']}hp")
    while gracz['hp'] > 0 and potwor['hp'] > 0:
        print(f"1. Walcz!\n2. Wycofaj się!\n3. Użyj mikstury leczenia({ekwipunek['leczenie']})")
        wpisywanie(1, 3, 2)
        if wybor2 == 1:
            potwor['hp'] -= random.randint(gracz["obrazenia_min"], gracz["obrazenia_max"])
            obrazenia = random.randint(potwor["obrazenia_min"], potwor["obrazenia_max"])
            if obrazenia < 0:
                obrazenia = 0
            gracz['hp'] -= obrazenia
            if gracz['hp'] < 0:
                gracz['hp'] = 0
            if potwor['hp'] < 0:
                potwor['hp'] = 0
            print(f"{gracz['name']}: {gracz['hp']}hp\npotwór: {potwor['hp']}hp")
        elif wybor2 == 2:
            break
        elif wybor2 == 3:
            if ekwipunek["leczenie"] > 0:
                gracz['hp'] = gracz['max_HP']
                print(f"{gracz['name']}: {gracz['hp']}hp\npotwór: {potwor['hp']}hp")
                ekwipunek["leczenie"] -= 1
            else:
                print("Nie masz mikstur!")
    else:
        if gracz["hp"] <= 0:
            print(f"\n\n\nNiestety, UMARŁEŚ!\nLVL: {gracz['lvl']}")
            sys.exit()
        else:
            xp_zdobyte = random.randint(potwor['xp_min'], potwor['xp_max'])
            gold_zdobyty  = random.randint(potwor['gold_min'], potwor['gold_max'])
            if xpx2 > 0:
                xp_zdobyte = 2 * xp_zdobyte
                gracz['xp'] += xp_zdobyte
                xpx2 -= 1
            elif xpx0 > 0:
                xp_zdobyte = 0
                xpx0 -= 1
            else:
                gracz['xp'] += xp_zdobyte
            if goldx2 > 0:
                gold_zdobyty = 2 * gold_zdobyty
                gracz['gold'] += gold_zdobyty
                goldx2 -= 1
            else:
                gracz['gold'] += gold_zdobyty
            print(f"Zdobywasz {gold_zdobyty} złota i {xp_zdobyte} XP")
            if grupa == 1:
                drop["drewno"] = random.randint(-1, 2)
                drop["skora"] = random.randint(-1, 2)
                if drop["drewno"] > 0:
                    print(f"Zdobywasz {drop['drewno']} drewna!")
                    materialy["drewno"] += drop["drewno"]
                if drop["skora"] > 0:
                    print(f"Zdobywasz {drop['skora']} skóry!")
                    materialy["skora"] += drop["skora"]
            if grupa == 2:
                drop["drewno"] = random.randint(0, 2)
                drop["skora"] = random.randint(0, 2)
                drop["zelazo"] = random.randint(0, 2)
                drop["stal"] = random.randint(0, 1)
                if drop["drewno"] > 0:
                    print(f"Zdobywasz {drop['drewno']} drewna!")
                    materialy["drewno"] += drop["drewno"]
                if drop["skora"] > 0:
                    print(f"Zdobywasz {drop['skora']} skóry!")
                    materialy["skora"] += drop["skora"]
                if drop["zelazo"] > 0:
                    print(f"Zdobywasz {drop['zelazo']} żelaza!")
                    materialy["zelazo"] += drop["zelazo"]
                if drop["stal"] > 0:
                    print(f"Zdobywasz {drop['stal']} stali!")
                    materialy["stal"] += drop["stal"]
            if grupa == 3:
                drop["zelazo"] = random.randint(1, 3)
                if drop["zelazo"] == 1:
                    print("Zdobywasz 3 żelaza!")
                    materialy["zelazo"] += 3
                elif drop["zelazo"] == 2:
                    print("Zdobywasz 5 żelaza!")
                    materialy["zelazo"] += 5
                drop["stal"] = random.randint(1, 10)
                if drop["stal"] <= 3:
                    print("Zdobywasz 1 stali!")
                    materialy["stal"] += 1
                elif drop["stal"] == 4 or drop["stal"] == 5:
                    print("Zdobywasz 3 stali!")
                    materialy["stal"] += 3
                elif drop["stal"] == 6 or drop["stal"] == 7:
                    print("Zdobywasz 5 stali!")
                    materialy["stal"] += 5
                drop["mithril"] = random.randint(1, 10)
                if drop["mithril"] == 1 or drop["mithril"] == 2:
                    print("Zdobywasz 1 mithril!")
                    materialy["mithril"] += 1
                elif drop["mithril"] == 3:
                    print("Zdobywasz 2 mithrilu!")
                    materialy["mithril"] += 2
            while gracz['xp'] >= gracz["max_XP"]:
                if gracz['lvl'] == 5:
                    gracz["max_XP"] = 200
                elif gracz['lvl'] == 10:
                    gracz["max_XP"] = 300
                elif gracz['lvl'] == 15:
                    gracz["max_XP"] = 500
                if gracz['xp'] >= gracz["max_XP"]:
                    gracz['xp'] -= gracz['max_XP']
                    gracz['lvl'] += 1
                    print(f"Zdobywasz {gracz['lvl']} LVL!")
            if gracz['lvl'] > 20:
                gracz['lvl']  = 20
                gracz["xp"] = 0


def otwarcie_skrzyni():
    skrzynia['gold'] = random.randint(100, 500)
    skrzynia['skora'] = random.randint(0, 10)
    skrzynia['drewno'] = random.randint(0, 10)
    skrzynia['zelazo'] = random.randint(0, 7)
    skrzynia['stal'] = random.randint(0, 5)
    skrzynia['mithril'] = random.randint(0, 2)
    skrzynia['leczenie'] = random.randint(0, 2)
    skrzynia['sila'] = random.randint(0, 1)
    skrzynia['wzmocnienie'] = random.randint(0, 1)
    print(f"Zdobywasz {skrzynia['gold']} złota!")
    gracz["gold"] += skrzynia['gold']
    if skrzynia['skora'] > 0:
        print(f"Zdobywasz {skrzynia['skora']} skóry!")
        materialy["skora"] += skrzynia['skora']
    if skrzynia['drewno'] > 0:
        print(f"Zdobywasz {skrzynia['drewno']} drewna!")
        materialy["drewno"] += skrzynia['drewno']
    if skrzynia['zelazo'] > 0:
        print(f"Zdobywasz {skrzynia['zelazo']} żelaza!")
        materialy["zelazo"] += skrzynia['zelazo']
    if skrzynia['stal'] > 0:
        print(f"Zdobywasz {skrzynia['stal']} stali!")
        materialy["stal"] += skrzynia['stal']
    if skrzynia['mithril'] > 0:
        print(f"Zdobywasz {skrzynia['mithril']} mithrilu!")
        materialy["mithril"] += skrzynia['mithril']
    if skrzynia['leczenie'] > 0:
        print(f"Zdobywasz {skrzynia['leczenie']} mikstur leczenia!")
        ekwipunek["leczenie"] += skrzynia['leczenie']
    if skrzynia['sila'] > 0:
        print(f"Zdobywasz miksturę siły!")
        ekwipunek["sila"] += skrzynia['sila']
    if skrzynia['wzmocnienie'] > 0:
        print(f"Zdobywasz miksturę wzmocnienia!")
        ekwipunek["wzmocnienie"] += skrzynia['wzmocnienie']
    if random.randint(1, 4) == 1:
        print(f"Zdobywasz miksturę podwajającą zdobywane złoto!")
        ekwipunek["goldx2"] += 1
    if random.randint(1, 4) == 1:
        print(f"Zdobywasz miksturę podwajającą zdobywane XP!")
        ekwipunek["xpx2"] += 1
    if random.randint(1, 4) == 1:
        print(f"Zdobywasz miksturę zatrzymującą postęp (LVL i XP)!")
        ekwipunek["xpx0"] += 1


def wpisywanie(min, max, nr):
    global wybor, wybor2, wybor3, wybor4
    if nr == 1:
        while True:
            try:
                wybor = int(input("Wybierz jedną z opcji: "))
                print()
                if min <= wybor <= max:
                    break
                print("Błąd! Wybierz jedną z dostępnych opcji!")
            except ValueError:
                print("Błąd! Wybierz jedną z dostępnych opcji!")
    elif nr == 2:
        while True:
            try:
                wybor2 = int(input("Wybierz jedną z opcji: "))
                print()
                if min <= wybor2 <= max:
                    break
                print("Błąd! Wybierz jedną z dostępnych opcji!")
            except ValueError:
                print("Błąd! Wybierz jedną z dostępnych opcji!")
    elif nr == 3:
        while True:
            try:
                wybor3 = int(input("Wybierz jedną z opcji: "))
                print()
                if min <= wybor3 <= max:
                    break
                print("Błąd! Wybierz jedną z dostępnych opcji!")
            except ValueError:
                print("Błąd! Wybierz jedną z dostępnych opcji!")
    elif nr == 4:
        while True:
            try:
                wybor4 = int(input("Wybierz jedną z opcji: "))
                print()
                if min <= wybor4 <= max:
                    break
                print("Błąd! Wybierz jedną z dostępnych opcji!")
            except ValueError:
                print("Błąd! Wybierz jedną z dostępnych opcji!")




            
gracz = {
    "name" : "Vacat vacat",
    "hp" : 100,
    "lvl" : 1,
    "xp" : 0,
    "gold" : 500,
    "max_XP" : 100,
    "max_HP" : 100,
    "obrazenia_zakres" : "10-15",
    "obrazenia_min" : 10,
    "obrazenia_max" : 15
}


ekwipunek = {
    "leczenie" : 5,
    "sila" : 0,
    "wzmocnienie" : 0,
    "goldx2" : 0,
    "xpx2" : 0,
    "xpx0" : 0,
    "klucze" : 0,
    "skrzynie" : 0
}


materialy = {
    "drewno" : 0,
    "skora" : 0,
    "zelazo" : 0,
    "stal" : 0,
    "mithril" : 0
}


potwor = {
    "klasa" : random.randint(1, 26),
    "hp" : 1,
    "obrazenia_min" : 1,
    "obrazenia_max" : 1,
    "xp_min" : 1,
    "xp_max" : 1,
    "gold_min": 1,
    "gold_max": 1
}


sklep = {
    "leczenie" : 250,
    "sila" : 1000,
    "wzmocnienie" : 1000,
    "los" : 500,
    "goldx2" : 1000,
    "xpx2" : 1000,
    "xpx0" : 1000,
    "ilosc" : 0
}


skrzynia = {
    "gold" : 0,
    "drewno" : 0,
    "skora" : 0,
    "zelazo" : 0,
    "stal" : 0,
    "mithril" : 0,
    "leczenie" : 0,
    "sila" : 0,
    "wzmocnienie" : 0,
    "los" : 0,
    "goldx2" : 0,
    "xpx2" : 0,
    "xpx0" : 0
}


drop = {
    "drewno" : 0,
    "skora" : 0,
    "zelazo" : 0,
    "stal" : 0,
    "mithril" : 0
}





xpx0 = 0
xpx2 = 0
goldx2 = 0

miecz = 0
kilof = 0
kilof_uzycia = 0
zbroja = 0
kopalnia = 0


gracz["name"] = input("Jak się nazywasz? ")
print(f"Witaj {gracz ['name']}!\n\n")




while True:
    if gracz['lvl'] == 20:
        print(f"{gracz['name']}, przyszła pora na walkę z BOSEM!!!")
    ScreenPodstawowy()
    wpisywanie(1, 5, 1)
    if wybor == 1:
        if gracz["lvl"] <= 5:
            potwor['klasa'] = random.randint(1, 26)
            if potwor['klasa'] == 1:
                print("LEGENDARNY potwór!!!")
                walka(200, 8, 12, 100, 250, 200, 500, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                ekwipunek['leczenie'] += 1
                print("Zdobywasz miksturę leczenia!")
            elif potwor['klasa'] == 2:
                print("LEGENDARNY potwór!!!")
                walka(150, 10, 15, 100, 250, 200, 500, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                if random.randint(1, 2) == 1:
                    ekwipunek['leczenie'] += 1
                    print("Zdobywasz miksturę leczenia!")
            elif 5 >= potwor['klasa'] >= 3:
                print("RZADKI potwór!!!")
                walka(100, 5, 7, 30, 100, 50, 250, 2)
            elif 8 >= potwor['klasa'] >= 6:
                print("RZADKI potwór!!!")
                walka(75, 5, 7, 30, 100, 50, 200, 2)
            elif 11 >= potwor['klasa'] >= 9:
                print("RZADKI potwór!!!")
                walka(50, 5, 10, 30, 100, 50, 200, 2)
            elif 16 >= potwor['klasa'] >= 12:
                print("KLASYCZNY potwór!!!")
                walka(50, 1, 3, 10, 30, 5, 25, 1)
            elif 21 >= potwor['klasa'] >= 17:
                print("KLASYCZNY potwór!!!")
                walka(25, 1, 4, 10, 30, 5, 25, 1)
            elif 26 >= potwor['klasa'] >= 22:
                print("KLASYCZNY potwór!!!")
                walka(15, 1, 5, 10, 30, 5, 25, 1)
        elif 10 >= gracz["lvl"] >= 6:
            potwor['klasa'] = random.randint(1, 26)
            if potwor['klasa'] == 1:
                print("LEGENDARNY potwór!!!")
                walka(300, 8, 12, 150, 300, 300, 500, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                ekwipunek['leczenie'] += 1
                print("Zdobywasz miksturę leczenia!")
            elif potwor['klasa'] == 2:
                print("LEGENDARNY potwór!!!")
                walka(200, 10, 15, 150, 300, 300, 500, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                if random.randint(1, 2) == 1:
                    ekwipunek['leczenie'] += 1
                    print("Zdobywasz miksturę leczenia!")
            elif 5 >= potwor['klasa'] >= 3:
                print("RZADKI potwór!!!")
                walka(150, 6, 8, 50, 150, 75, 300, 2)
            elif 8 >= potwor['klasa'] >= 6:
                print("RZADKI potwór!!!")
                walka(100, 6, 7, 50, 150, 50, 200, 2)
            elif 11 >= potwor['klasa'] >= 9:
                print("RZADKI potwór!!!")
                walka(75, 7, 10, 50, 150, 50, 200, 2)
            elif 16 >= potwor['klasa'] >= 12:
                print("KLASYCZNY potwór!!!")
                walka(75, 1, 5, 25, 50, 10, 50, 1)
            elif 21 >= potwor['klasa'] >= 17:
                print("KLASYCZNY potwór!!!")
                walka(50, 3, 5, 25, 50, 10, 50, 1)
            elif 26 >= potwor['klasa'] >= 22:
                print("KLASYCZNY potwór!!!")
                walka(25, 3, 7, 25, 50, 10, 50, 1)
        elif 15 >= gracz["lvl"] >= 11:
            potwor['klasa'] = random.randint(1, 26)
            if potwor['klasa'] == 1:
                print("LEGENDARNY potwór!!!")
                walka(400, 10, 13, 250, 500, 500, 750, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                ekwipunek['leczenie'] += 1
                print("Zdobywasz miksturę leczenia!")
            elif potwor['klasa'] == 2:
                print("LEGENDARNY potwór!!!")
                walka(300, 12, 15, 250, 500, 500, 750, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                if random.randint(1, 2) == 1:
                    ekwipunek['leczenie'] += 1
                    print("Zdobywasz miksturę leczenia!")
            elif 5 >= potwor['klasa'] >= 3:
                print("RZADKI potwór!!!")
                walka(200, 6, 10, 100, 250, 100, 300, 2)
            elif 8 >= potwor['klasa'] >= 6:
                print("RZADKI potwór!!!")
                walka(150, 7, 10, 100, 250, 100, 300, 2)
            elif 11 >= potwor['klasa'] >= 9:
                print("RZADKI potwór!!!")
                walka(100, 10, 12, 100, 250, 200, 300, 2)
            elif 16 >= potwor['klasa'] >= 12:
                print("KLASYCZNY potwór!!!")
                walka(100, 1, 5, 50, 100, 25, 100, 1)
            elif 21 >= potwor['klasa'] >= 17:
                print("KLASYCZNY potwór!!!")
                walka(75, 3, 5, 50, 100, 25, 100, 1)
            elif 26 >= potwor['klasa'] >= 22:
                print("KLASYCZNY potwór!!!")
                walka(50, 3, 7, 50, 100, 25, 100, 1)
        elif 19 >= gracz["lvl"] >= 16:
            potwor['klasa'] = random.randint(1, 26)
            if potwor['klasa'] == 1:
                print("LEGENDARNY potwór!!!")
                walka(500, 10, 15, 500, 750, 750, 1000, 3)
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['sila'] += 1
                    print("Zdobywasz miksturę siły!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                if random.randint(1, 2) == 1:
                    ekwipunek['wzmocnienie'] += 1
                    print("Zdobywasz miksturę wzmocnienia!")
                ekwipunek['leczenie'] += 2
                print("Zdobywasz miksturę leczenia!")
                print("Zdobywasz miksturę leczenia!")
            elif potwor['klasa'] == 2:
                print("LEGENDARNY potwór!!!")
                walka(400, 12, 15, 500, 750, 750, 1000, 3)
                ekwipunek['sila'] += 1
                print("Zdobywasz miksturę siły!")
                ekwipunek['wzmocnienie'] += 1
                print("Zdobywasz miksturę wzmocnienia!")
                ekwipunek['leczenie'] += 1
                print("Zdobywasz miksturę leczenia!")
            elif 5 >= potwor['klasa'] >= 3:
                print("RZADKI potwór!!!")
                walka(250, 8, 12, 150, 250, 200, 500, 2)
            elif 8 >= potwor['klasa'] >= 6:
                print("RZADKI potwór!!!")
                walka(200, 8, 10, 150, 250, 200, 500, 2)
            elif 11 >= potwor['klasa'] >= 9:
                print("RZADKI potwór!!!")
                walka(150, 10, 12, 150, 250, 200, 500, 2)
            elif 16 >= potwor['klasa'] >= 12:
                print("KLASYCZNY potwór!!!")
                walka(150, 3, 7, 100, 200, 50, 250, 1)
            elif 21 >= potwor['klasa'] >= 17:
                print("KLASYCZNY potwór!!!")
                walka(100, 4, 7, 100, 200, 50, 250, 1)
            elif 26 >= potwor['klasa'] >= 22:
                print("KLASYCZNY potwór!!!")
                walka(75, 3, 7, 100, 200, 50, 250, 1)
        elif gracz['lvl'] >= 20:
            print("WALKA Z BOSEM!!!")
            walka(10000, 5, 25, 0, 0, 0, 0, 0)
            print(f"GRATULACJE!!! {gracz['name']} przeszedłeś grę!")
            sys.exit()
    if wybor == 2:
        while kilof_uzycia > 0:
            print("1. Kop!\n2. Wyjdź z kopalni")
            wpisywanie(1, 2, 2)
            if wybor2 == 1:
                kilof_uzycia -= 1
                if kilof_uzycia == 0:
                    kilof = 0
                    print("Twój kilof się zniszczył!")
                kopalnia = random.randint(1, 50)
                if kopalnia <= 20:
                    print("Tym razem nic nie wykopałeś!")
                if 21 <= kopalnia <= 36:
                    print("Zdobywasz żelazo!")
                    materialy["zelazo"] += 1
                if 37 <= kopalnia <= 46:
                    print("Zdobywasz stal!")
                    materialy["stal"] += 1
                if 47 <= kopalnia <= 49:
                    print("Zdobywasz mithril!")
                    materialy["mithril"] += 1
                if kopalnia == 50:
                    print("Znajdujesz skrzynię!!!")
                    while True:
                        print("1. Otwórz skrzynię (wymagany klucz)\n2. Weź skrzynię ze sobą (1000 złota)\n3. Zostaw skrzynię")
                        wpisywanie(1, 3, 3)
                        if wybor3 == 1:
                            if ekwipunek["klucze"] > 0:
                                ekwipunek["klucze"] -= 1
                                otwarcie_skrzyni()
                                break
                            else:
                                print("Nie masz klucza!")
                        if wybor3 == 2:
                            if gracz["gold"] >= 1000:
                                gracz["gold"] -= 1000
                                ekwipunek["skrzynie"] += 1
                                break
                            else:
                                print("Nie masz wystarczająco złota!")
                        if wybor3 == 3:
                            break
            else:
                break
        else:
            print("Nie masz kilofa!")
    if wybor == 3:
        print("1. WyświetL mikstury\n2. Wyświetl narzędzia i zbroje\n3. Wyświetl materiały\n4. Wyjdź z ekwipunku")
        wpisywanie(1, 4, 2)
        if wybor2 == 1:
            print(f"Masz {ekwipunek['leczenie']} mikstur leczenia,\n{ekwipunek['sila']} mikstur siły,\n{ekwipunek['wzmocnienie']} mikstur wzmocnienia.\n{ekwipunek['goldx2']} mikstur podwajających zdobywane złoto.\n{ekwipunek['xpx2']} podwajających zdobywane XP.\n{ekwipunek['xpx0']} mikstur zatrzymujących postęp(LVL i XP).\n")
            print("1. Wyjdź z ekwipunku\n2. Użyj mikstury siły\n3. Użyj mikstury wzmocnienia\n4. Użyj mikstury podwajającej zdowywane złoto\n5. Użyj mikstury podwajającej zdobywane XP\n6. Użyj mikstury zatrzymującej postęp(LVL i XP)")
            wpisywanie(1, 6, 3)
            if wybor3 == 2:
                if ekwipunek['sila'] > 0:
                    gracz['obrazenia_min'] += 5
                    gracz['obrazenia_max'] += 5
                    gracz['obrazenia_zakres'] = f"{gracz['obrazenia_min']}-{gracz['obrazenia_max']}"
                    ekwipunek['sila'] -= 1
                else:
                    print("Nie masz mikstur!")
            if wybor3 == 3:
                if ekwipunek['wzmocnienie'] > 0:
                    gracz["max_HP"] += 50
                    ekwipunek['wzmocnienie'] -= 1
                else:
                    print("Nie masz mikstur!")
            if wybor3 == 4:
                if goldx2 <= 0:
                    if ekwipunek['goldx2'] > 0:
                        goldx2 = 10
                        ekwipunek['goldx2'] -= 1
                    else:
                        print("Nie masz mikstur!")
                else:
                    print("Mikstura jest aktywna!")
            if wybor3 == 5:
                if xpx2 <= 0 and xpx0 <= 0:
                    if ekwipunek['xpx2'] > 0:
                        xpx2 = 10
                        ekwipunek['xpx2'] -= 1
                    else:
                        print("Nie masz mikstur!")
                else:
                    print("Jedna z mikstur wpływających na xp jest aktywna!")
            if wybor3 == 6:
                if xpx2 <= 0 and xpx0 <= 0:
                    if ekwipunek['xpx0'] > 0:
                        xpx0 = 10
                        ekwipunek['xpx0'] -= 1
                    else:
                        print("Nie masz mikstur!")
                else:
                    print("Jedna z mikstur wpływających na xp jest aktywna!")
        if wybor2 == 2:
            if miecz == 0:
                print("Nie masz jeszcze żadnego miecza.")
            elif miecz == 1:
                print("Masz drewniany miecz!")
            elif miecz == 2:
                print("Masz żelazny miecz!")
            elif miecz == 3:
                print("Masz stalowy miecz!")
            elif miecz == 4:
                print("Masz mithrilowy miecz!")
            if kilof == 0:
                print("Nie masz obecnie żadnego kilofu.")
            elif kilof == 1:
                print("Masz drewniany kilof!")
            elif kilof == 2:
                print("Masz żelazny kilof!")
            elif kilof == 3:
                print("Masz stalowy kilof!")
            elif kilof == 4:
                print("Masz mithrilowy kilof!")
            if kilof != 0:
                print(f"Pozostało {kilof_uzycia} użyć kilofa!")
            if zbroja == 0:
                print("Nie masz jeszcze żadnej zbroi.")
            elif zbroja == 1:
                print("Masz skórzaną zbroję!")
            elif zbroja == 2:
                print("Masz żelazną zbroję!")
            elif zbroja == 3:
                print("Masz stalową zbroję!")
            elif zbroja == 4:
                print("Masz mithrilową zbroję!")
            if ekwipunek["klucze"] > 0:
                print(f"Masz {ekwipunek['klucze']} kluczy!")
            else:
                print("Nie masz obecnie żadnych kluczy.")
            if ekwipunek["skrzynie"] > 0:
                print(f"Masz {ekwipunek['skrzynie']} skrzyń przy sobie!")
                print("1. Otwórz skrzynię (wymagany klucz)\n2. Wyjdź z ekwipunku")
                wpisywanie(1, 2, 3)
                if wybor3 == 1:
                    if ekwipunek['klucze'] >= 1:
                        ekwipunek['klucze'] -= 1
                        ekwipunek["skrzynie"] -= 1
                        otwarcie_skrzyni()
                    else:
                        print("Nie masz obecnie żadnego klucza!\n")
            else:
                print("Nie masz obecnie przy sobie żadnej skrzyni.\n")
        if wybor2 == 3:
            print(f"Masz {materialy['skora']} skóry,\n{materialy['drewno']} drewna,\n{materialy['zelazo']} żelaza,\n{materialy['stal']} stali\ni {materialy['mithril']} mithrilu!")
    if wybor == 4:
        print("1. Kupuj mikstury\n2. Kupuj materiały\n3. Sprzedawaj materiały\n4. Kupuj los na loterii\n5. Wyjdź ze sklepu")
        wpisywanie(1, 5, 2)
        if wybor2 == 1:
            print(f"1. Kup miksturę leczenia ({sklep['leczenie']} złota)\n2. Kup miksturę siły ({sklep['sila']} złota)\n3. Kup miksturę wzmocnienia ({sklep['wzmocnienie']} złota)\n4. Kup miksturę podwajającą zdobywane złoto ({sklep['goldx2']} złota)\n5. Kup miksturę podwajającą zdobywane XP ({sklep['xpx2']} złota)\n6. Kup miksturę zatrzymującą postęp (LVL i XP) ({sklep['xpx0']} złota)\n7. Wyjdź ze sklepu")
            wpisywanie(1, 7, 3)
            if wybor3 == 1:
                if gracz["gold"] >= sklep["leczenie"]:
                    ekwipunek["leczenie"] += 1
                    gracz["gold"] -= sklep["leczenie"]
                    sklep["leczenie"] += 250
                else:
                    print("Masz za mało złota!")
            if wybor3 == 2:
                if gracz["gold"] >= sklep["sila"]:
                    ekwipunek["sila"] += 1
                    gracz["gold"] -= sklep["sila"]
                    sklep["sila"] += 1000
                else:
                    print("Masz za mało złota!")
            if wybor3 == 3:
                if gracz["gold"] >= sklep["wzmocnienie"]:
                    ekwipunek["wzmocnienie"] += 1
                    gracz["gold"] -= sklep["wzmocnienie"]
                    sklep["wzmocnienie"] += 1000
                else:
                    print("Masz za mało złota!")
            if wybor3 == 4:
                if gracz["gold"] >= sklep["goldx2"]:
                    ekwipunek["goldx2"] += 1
                    gracz["gold"] -= sklep["goldx2"]
                    sklep["goldx2"] = 2500
                else:
                    print("Masz za mało złota!")
            if wybor3 == 5:
                if gracz["gold"] >= sklep["xpx2"]:
                    ekwipunek["xpx2"] += 1
                    gracz["gold"] -= sklep["xpx2"]
                    sklep["xpx2"] = 2500
                else:
                    print("Masz za mało złota!")
            if wybor3 == 6:
                if gracz["gold"] >= sklep["xpx0"]:
                    ekwipunek["xpx0"] += 1
                    gracz["gold"] -= sklep["xpx0"]
                    sklep["xpx0"] = 2500
                else:
                    print("Masz za mało złota!")
        if wybor2 == 2:
            print("Kup: \n1. Skórę (50 złota/szt.)\n2. Drewno (50 złota/szt.)\n3. Żelazo (100 złota/szt.)\n4. Stal (200 złota/szt.)\n5. Mithril (1000 złota/szt.)\n6. Wyjdx ze sklepu")
            wpisywanie(1, 6, 3)
            while True:
                try:
                    sklep["ilosc"] = int(input("Ile sztuk chcesz kupić: "))
                    if sklep["ilosc"] > 0:
                        break
                    else:
                        print("Błąd! Wybierz jedną z dostępnych opcji!")
                except ValueError:
                    print("Błąd! Wybierz jedną z dostępnych opcji!")
            print()
            if wybor3 == 1:
                if gracz["gold"] >= 50 * sklep["ilosc"]:
                    gracz["gold"] -= 50 * sklep["ilosc"]
                    materialy["skora"] += sklep["ilosc"]
                    print(f"Zakupiłeś {sklep['ilosc']} skóry!")
                else:
                    print("Nie masz wystarczająco złota!")
            elif wybor3 == 2:
                if gracz["gold"] >= 50 * sklep["ilosc"]:
                    gracz["gold"] -= 50 * sklep["ilosc"]
                    materialy["drewno"] += sklep["ilosc"]
                    print(f"Zakupiłeś {sklep['ilosc']} drewna!")
                else:
                    print("Nie masz wystarczająco złota!")
            elif wybor3 == 3:
                if gracz["gold"] >= 100 * sklep["ilosc"]:
                    gracz["gold"] -= 100 * sklep["ilosc"]
                    materialy["zelazo"] += sklep["ilosc"]
                    print(f"Zakupiłeś {sklep['ilosc']} żelaza!")
                else:
                    print("Nie masz wystarczająco złota!")
            elif wybor3 == 4:
                if gracz["gold"] >= 200 * sklep["ilosc"]:
                    gracz["gold"] -= 200 * sklep["ilosc"]
                    materialy["stal"] += sklep["ilosc"]
                    print(f"Zakupiłeś {sklep['ilosc']} stali!")
                else:
                    print("Nie masz wystarczająco złota!")
            elif wybor3 == 5:
                if gracz["gold"] >= 1000 * sklep["ilosc"]:
                    gracz["gold"] -= 1000 * sklep["ilosc"]
                    materialy["mithril"] += sklep["ilosc"]
                    print(f"Zakupiłeś {sklep['ilosc']} mithrilu!")
                else:
                    print("Nie masz wystarczająco złota!")
        if wybor2 == 3:
            print("Sprzedaj: \n1. Skórę (30 złota/szt.)\n2. Drewno (30 złota/szt.)\n3. Żelazo (75 złota/szt.)\n4. Stal (150 złota/szt.)\n5. Mithril (750 złota/szt.)\n6.Wyjdź ze sklepu")
            wpisywanie(1, 6, 3)
            print()
            while True:
                try:
                    sklep["ilosc"] = int(input("Ile sztuk chcesz sprzedać: "))
                    if sklep["ilosc"] > 0:
                        break
                    else:
                        print("Błąd! Wybierz jedną z dostępnych opcji!")
                except ValueError:
                    print("Błąd! Wybierz jedną z dostępnych opcji!")
            print()
            if wybor3 == 1:
                if materialy["skora"] >= sklep["ilosc"]:
                    materialy["skora"] -= sklep["ilosc"]
                    gracz["gold"] += 30 * sklep["ilosc"]
                    print(f"Sprzedałeś {sklep['ilosc']} skóry za {30 * sklep['ilosc']} złota!")
                else:
                    print("Masz za mało materiałów!")
            elif wybor3 == 2:
                if materialy["drewno"] >= sklep["ilosc"]:
                    materialy["drewno"] -= sklep["ilosc"]
                    gracz["gold"] += 30 * sklep["ilosc"]
                    print(f"Sprzedałeś {sklep['ilosc']} drewna za {30 * sklep['ilosc']} złota!")
                else:
                    print("Masz za mało materiałów!")
            elif wybor3 == 3:
                if materialy["zelazo"] >= sklep["ilosc"]:
                    materialy["zelazo"] -= sklep["ilosc"]
                    gracz["gold"] += 75 * sklep["ilosc"]
                    print(f"Sprzedałeś {sklep['ilosc']} żelaza za {75 * sklep['ilosc']} złota!")
                else:
                    print("Masz za mało materiałów!")
            elif wybor3 == 4:
                if materialy["stal"] >= sklep["ilosc"]:
                    materialy["stal"] -= sklep["ilosc"]
                    gracz["gold"] += 150 * sklep["ilosc"]
                    print(f"Sprzedałeś {sklep['ilosc']} stali za {150 * sklep['ilosc']} złota!")
                else:
                    print("Masz za mało materiałów!")
            elif wybor3 == 5:
                if materialy["mithril"] >= sklep["ilosc"]:
                    materialy["mithril"] -= sklep["ilosc"]
                    gracz["gold"] += 750 * sklep["ilosc"]
                    print(f"Sprzedałeś {sklep['ilosc']} mithrilu za {750 * sklep['ilosc']} złota!")
                else:
                    print("Masz za mało materiałów!")
        if wybor2 == 4:
            print(f"Kupując los, masz szansę na:\n- miksturę leczenia(15%)\n- miksturę siły(15%)\n- miksturę wzmocnienia(15%)\n- miksturę podwajającą zdobywane złoto(5%)\n- miksturę podwajającą zdobywane XP(5%)\n- miksturę blokującą postępy (LVL i XP)(5%)\n- pusty los(40%)\n\n1. Kup los ({sklep['los']} złota)\n2. Wyjdź ze sklepu")
            wpisywanie(1, 2, 3)
            if wybor3 == 1:
                if gracz["gold"] >= sklep["los"]:
                    gracz["gold"] -= sklep["los"]
                    sklep["los"] += 500
                    los = random.randint(1, 20)
                    if los <= 3:
                        ekwipunek["leczenie"] += 1
                        print("Zdobywasz miksturę leczenia!")
                    elif 4 <= los <= 6:
                        ekwipunek["sila"] += 1
                        print("Zdobywasz miksturę siły!")
                    elif 7 <= los <= 9:
                        ekwipunek["wzmocnienie"] += 1
                        print("Zdobywasz miksturę wzmocnienia!")
                    elif los == 10:
                        ekwipunek["goldx2"] += 1
                        print("Zdobywasz miksturę podwajającą zdobywane złoto!")
                    elif los == 11:
                        ekwipunek["xpx2"] += 1
                        print("Zdobywasz miksturę podwajającą zdobywane XP!")
                    elif los == 12:
                        ekwipunek["xpx0"] += 1
                        print("Zdobywasz miksturę blokującą postępy (LVL i XP)!")
                    else:
                        print("Niestety, trafiasz pusty los")
                else:
                    print("Masz za mało złota!")
    if wybor == 5:
        print("Co cię do mnie sprowadza?\n1. Chcę zdobyć narzędzia\n2. Chcę zdobyć zbroje\n3. Wyjdź od kowala")
        wpisywanie(1, 3, 2)
        if wybor2 == 1:
            print("Które z narzędzi cię interesują\n1. Miecze\n2. Kilofy\n3. Klucze\n4. Wyjdź od kowala")
            wpisywanie(1, 4, 3)
            if wybor3 == 1:
                print("Mogę zrobić dla ciebie\n1. Drewniany miecz (obrażenia: +1) Koszt: 10 drewna\n2. Żelazny miecz (obrażenia: +3) Koszt: 10 żelaza i 5 drewna\n3. Stalowy miecz (obrażenia: +5) Koszt: 10 stali i 10 żelaza\n4. Mithrilowy miecz (obrażenia: +10) Koszt: 5 mithrilu, 10 stali i 20 żelaza\n5. Wyjdź od kowala")
                wpisywanie(1, 5, 4)
                if wybor4 == 1:
                    if miecz < 1:
                        if materialy["drewno"] >= 10:
                            gracz['obrazenia_min'] += 1
                            gracz['obrazenia_max'] += 1
                            gracz['obrazenia_zakres'] = f"{gracz['obrazenia_min']}-{gracz['obrazenia_max']}"
                            materialy["drewno"] -= 10
                            miecz = 1
                        else:
                            print("Nie masz wystarczająco surowców")
                    elif miecz == 1:
                        print("Posiadasz już ten miecz!")
                    else:
                        print("Posiadasz już lepszy miecz!")
                elif wybor4 == 2:
                    if miecz < 2:
                        if materialy["zelazo"] >= 10 and materialy["drewno"] >= 5:
                            if miecz == 1:
                                gracz['obrazenia_min'] -= 1
                                gracz['obrazenia_max'] -= 1
                            gracz['obrazenia_min'] += 3
                            gracz['obrazenia_max'] += 3
                            gracz['obrazenia_zakres'] = f"{gracz['obrazenia_min']}-{gracz['obrazenia_max']}"
                            materialy["zelazo"] -= 10
                            materialy["drewno"] -= 5
                            miecz = 2
                        else:
                            print("Nie masz wystarczająco surowców")
                    elif miecz == 2:
                        print("Posiadasz już ten miecz!")
                    else:
                        print("Posiadasz już lepszy miecz!")
                elif wybor4 == 3:
                    if miecz < 3:
                        if materialy["stal"] >= 10 and materialy["zelazo"] >= 10:
                            if miecz == 1:
                                gracz['obrazenia_min'] -= 1
                                gracz['obrazenia_max'] -= 1
                            if miecz == 2:
                                gracz['obrazenia_min'] -= 3
                                gracz['obrazenia_max'] -= 3
                            gracz['obrazenia_min'] += 5
                            gracz['obrazenia_max'] += 5
                            gracz['obrazenia_zakres'] = f"{gracz['obrazenia_min']}-{gracz['obrazenia_max']}"
                            materialy["stal"] -= 10
                            materialy["zelazo"] -= 10
                            miecz = 3
                        else:
                            print("Nie masz wystarczająco surowców")
                    elif miecz == 3:
                        print("Posiadasz już ten miecz!")
                    else:
                        print("Posiadasz już lepszy miecz!")
                elif wybor4 == 4:
                    if miecz < 4:
                        if materialy["mithril"] >= 5 and materialy["stal"] >= 10 and materialy["zelazo"] >= 20:
                            if miecz == 1:
                                gracz['obrazenia_min'] -= 1
                                gracz['obrazenia_max'] -= 1
                            if miecz == 2:
                                gracz['obrazenia_min'] -= 3
                                gracz['obrazenia_max'] -= 3
                            if miecz == 3:
                                gracz['obrazenia_min'] -= 5
                                gracz['obrazenia_max'] -= 5
                            gracz['obrazenia_min'] += 10
                            gracz['obrazenia_max'] += 10
                            gracz['obrazenia_zakres'] = f"{gracz['obrazenia_min']}-{gracz['obrazenia_max']}"
                            materialy["mithril"] -= 5
                            materialy["stal"] -= 10
                            materialy["zelazo"] -= 20
                            miecz = 4
                        else:
                            print("Nie masz wystarczająco surowców")
                    elif miecz == 4:
                        print("Posiadasz już ten miecz!")
                    else:
                        print("Posiadasz już lepszy miecz!")
            if wybor3 == 2:
                print("Mogę zrobić dla Ciebie\n1. Drewniany kilof (10 użyć) Koszt: 10 drewna\n2. Żelazny kilof (25 użyć) Koszt: 15 żelaza\n3. Stalowy kilof (50 użyć) Koszt: 15 stali\n4. Mithrilowy kilof (100 użyć) Koszt: 3 mithrilu, 20 stali i 20 żelaza\n5. Wyjdź od kowala")
                wpisywanie(1, 5, 4)
                if wybor4 == 1:
                    if kilof == 0:
                        if materialy["drewno"] >= 10:
                            kilof_uzycia += 10
                            kilof = 1
                            materialy["drewno"] -= 10
                        else:
                            print("Nie masz wystarczająco surowców")
                    else:
                        print("Masz już kilof!")
                if wybor4 == 2:
                    if kilof == 0:
                        if materialy["zelazo"] >= 15:
                            kilof_uzycia += 25
                            kilof = 2
                            materialy["zelazo"] -= 15
                        else:
                            print("Nie masz wystarczająco surowców")
                    else:
                        print("Masz już kilof!")
                if wybor4 == 3:
                    if kilof == 0:
                        if materialy["stal"] >= 15:
                            kilof_uzycia += 50
                            kilof = 3
                            materialy["stal"] -= 15
                        else:
                            print("Nie masz wystarczająco surowców")
                    else:
                        print("Masz już kilof!")
                if wybor4 == 4:
                    if kilof == 0:
                        if materialy["mithril"] >= 3 and materialy["stal"] >= 20 and materialy["zelazo"] >= 20:
                            kilof_uzycia += 100
                            kilof = 4
                            materialy["mithril"] -= 3
                            materialy["stal"] -= 20
                            materialy["zelazo"] -= 20
                        else:
                            print("Nie masz wystarczająco surowców")
                    else:
                        print("Masz już kilof!")
            if wybor3 == 3:
                print("1. Wyprodukuj klucz do skrzyni (20 żelaza, 20 stali, 1 mithril\n2. Wyjdź od kowala")
                wpisywanie(1, 2, 4)
                if wybor4 == 1:
                    if materialy["mithril"] >= 1 and materialy["stal"] >= 20 and materialy["zelazo"] >= 20:
                        ekwipunek["klucze"] += 1
                        materialy["mithril"] -= 1
                        materialy["stal"] -= 20
                        materialy["zelazo"] -= 20
                    else:
                        print("Nie masz wystarczająco surowców")
        if wybor2 == 2:
            print("Mogę zaoferować ci \n1. Skórzaną zbroję (obrażenia potworów: -1) Koszt: 15 skóry\n2. Żelazną zbroję (obrażenia potworów: -3) Koszt: 20 żelaza\n3. Stalową zbroję (obrażenia potworów: -5) Koszt: 15 stali\n4. Mithrilową zbroję (obrażenia potworów: -10) Koszt: 5 mithrilu, 10 stali i 10 żelaza\n5. Wyjdź od kowala")
            wpisywanie(1, 5, 3)
            if wybor3 == 1:
                if zbroja < 1:
                    if materialy["skora"] >= 15:
                        materialy["skora"] -= 15
                        zbroja = 1
                    else:
                        print("Nie masz wystarczająco surowców")
                elif zbroja == 1:
                    print("Posiadasz już tą zbroję!")
                else:
                    print("Posiadasz już lepszą zbroję!")
            if wybor3 == 2:
                if zbroja < 2:
                    if materialy["zelazo"] >= 20:
                        materialy["zelazo"] -= 20
                        zbroja = 2
                    else:
                        print("Nie masz wystarczająco surowców")
                elif zbroja == 2:
                    print("Posiadasz już tą zbroję!")
                else:
                    print("Posiadasz już lepszą zbroję!")
            if wybor3 == 3:
                if zbroja < 3:
                    if materialy["stal"] >= 15:
                        materialy["stal"] -= 15
                        zbroja = 3
                    else:
                        print("Nie masz wystarczająco surowców")
                elif zbroja == 3:
                    print("Posiadasz już tą zbroję!")
                else:
                    print("Posiadasz już lepszą zbroję!")
            if wybor3 == 4:
                if zbroja < 4:
                    if materialy["mithril"] >= 5 and materialy["stal"] >= 10 and materialy["zelazo"] >= 10:
                        materialy["mithril"] -= 5
                        materialy["stal"] -= 10
                        materialy["zelazo"] -= 10
                        zbroja = 4
                    else:
                        print("Nie masz wystarczająco surowców")
                elif zbroja == 4:
                    print("Posiadasz już tą zbroję!")
                else:
                    print("Posiadasz już lepszą zbroję!")
                    