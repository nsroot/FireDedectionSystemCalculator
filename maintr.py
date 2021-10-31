#This document is written in Turkish.
import math
def yasamalani():
    apartmantsayisi = int(input("plase input apartment sayisi"))
    apartmantboyutu = int(input("please input room size"))
    odasayisi = int(input("please input liveroom apartmab basina sayisi"))
    katsayisi = int(input("please input katsayisi"))
    koridorsayisi = int(input("please input koridor sayisi"))
    koridoruzunluk = int(input("koridor uzunluk tipi dedektor sayisi icin : "))
    eksiodasayisi = int(input("eksi oda sayisi"))
    tavanarasi = input("Tavan arasi olacakmi \n Evet yada Hayir: ")
    mutfakalani = input("Mutfak Icin Isi Dedektoru Olacak mi ? \n Evet yada Hayir:  ")
    asansor = int(input("asansor sayisi"))
    merdivensayisi = int(input("Merdiven Sayisi: "))
    if odasayisi == 2:
        roomdedectorecnt = 2
    elif odasayisi == 1:
        roomdedectorecnt = 1
    if koridorsayisi in range(0,4):
        koridor1 = int(input("koridor 1 uzunluk"))
        koridor2 = int(input("koridor 1 uzunluk"))
        koridor3 = int(input("koridor 1 uzunluk"))
        koridor4 = int(input("koridor 1 uzunluk"))
        koridor1d = math.ceil(koridor1 / koridoruzunluk)
        koridor2d = math.ceil(koridor2 / koridoruzunluk)
        koridor3d = math.ceil(koridor3 / koridoruzunluk)
        koridor4d = math.ceil(koridor4 / koridoruzunluk)
        koridoruzunluk = math.ceil(koridor1d+koridor2d+koridor3d+koridor4d)
        butonsayisi = 2
        flashorsayisi = 2
    if mutfakalani in ("Evet","Hayir","E","H"):
        combinededector = katsayisi*((roomdedectorecnt*apartmantsayisi))
    if tavanarasi in ("Evet","Hayir","E","H"):
        roomdedectorecnt = roomdedectorecnt*2
    dedectorcnt = katsayisi*((koridoruzunluk+(roomdedectorecnt*apartmantsayisi))-eksiodasayisi)
    flashorcnt = katsayisi*flashorsayisi
    butoncnt = katsayisi*butonsayisi
    module = asansor

    print("Dedektor Sayisi: ", dedectorcnt)
    print("Flashor Sayisi: ",flashorcnt)
    print("Buton Sayisi: ",butoncnt)
    print("I/0 Modulu: ",module)
    if mutfakalani in ("Evet", "Hayir", "E", "H"):
        print("Combine Smoke and heat Dedector: ",combinededector)
def otopark():
    #30 Metre Kare Onerilen.
    type = input("Lutfen Otopark Tipini Seciniz.\n Araba baasina \n Metre Kare basina \n Girdiler M ve A\n Bilgiyi Giriniz: ")
    merdivesayisi = int(input("Merdiven Sayisi"))
    mvekesitmi = input("Merdivenler Kapilar ile yanyana mi ? \n Evet yada Hayir \n E veya H")
    if mvekesitmi in ("E","e"):
        flashorcnt = merdivesayisi
        butoncnt = merdivesayisi
        exitlamp = merdivesayisi+2
    if type in ("A","a"):
        parkalanisayisi = int(input("Park Alani Sayisini Giriniz: "))
    if type in ("M","m"):
        parkalanimetrekaresix = int(input("Enlem Uzunlugu: "))
        parkalanimetrekaresiy = int(input("Boylam Uzunlugu: "))
        dedectortype = int(input("Dedector Metrekare Tipi: "))
        dedectorcnt = (parkalanimetrekaresix*parkalanimetrekaresiy)/dedectortype

    print("Dedektor Sayisi: ", dedectorcnt)
    print("Flashor Sayisi: ", flashorcnt)
    print("Buton Sayisi: ", butoncnt)
    print("Exit Lambasi Yonlu : ",exitlamp)
def metrekare():
    metrekare = int(input("kulanilabilir Metre kareyi giriniz"))
    kapi = int(input("Kapi sayisini Giriniz."))
    type = int(input("Dedektor tipi metre karesi"))
    dedectorcnt = metrekare/type
    flashorcnt = kapi + 4
    butoncnt = flashorcnt
    exitlamp = flashorcnt
    print("Dedektor Sayisi: ", dedectorcnt)
    print("Flashor Sayisi: ", flashorcnt)
    print("Buton Sayisi: ", butoncnt)
    print("Exit Lambasi Yonlu : ", exitlamp)

projeyisec = int(input("Lutfen hesaplama istediklerinizi seciniz"
                       "\n1.Yasam Alani Icin Hesaplama"
                       "\n2.Otopark Hesaplama"
                       "\n3.Zemin Kat Metre Kare Hesaplama"
                       "\n4.Her ikisini Hesaplama"
                       "\nSiralamaya Gore Seciniz: "))
if projeyisec == 1:
    yasamalani()
if projeyisec == 2:
    otopark()
if projeyisec == 3:
    metrekare()


