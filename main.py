import random

kelmimeler = ["globalaihub", "turkishaihub", "omer cengiz", "elif yigit", "kutay akalin", "aysuda ceylan"]


def ana_menu():
    print("*********ANA MENÜ**********")
    print("Bunu biliyor muydunuz?: Avrupa'da 17. yy'da adam asma oyunu ölüm hükmü almış kişilere oynatılırdı. Sonuca göre hükümlünün canı bağışlanırdı.")
    print("Her yanlış tahminde idama daha da yaklaşırsınız. Bunu aşağıdaki şekli tekip ederek görebilirsiniz. ."
"""
---0
 _/|\_
 _/ \_
""")
    secim = int(input("oyunu başlatmak için 1'e basınız: "))
    if secim == 1:
        oyun()
    else:
        print("geçersiz seçenek!")


def oyun():
    print("OYUN BAŞLADI!..\nROBOTUMUZ RASTGELE BİR KELİME ÜRETİYOR...")

    kelime = random.choice(kelmimeler)
    print("(İPUCU) BULMAK İSTEDİĞİMİZ KELİME--->  {}".format(kelime))
    uzunluk = len(kelime)
    sifreli_liste = list(kelime)
    sayac = 0
    for i in sifreli_liste:  # listeyi şifreliyor
        if i != ' ':
            sifreli_liste[sayac] = '_'
        else:
            uzunluk -= 1
        sayac += 1

    def listeden_kurtar():
        for j in sifreli_liste:  # ekranda güzel görüntü. liste görünümünden kurtarmak
            print(j, end="")
        print()

    listeden_kurtar()

    harfler = list(kelime)

    yildiz_sayisi = 6
    sayac3 = 0

    while yildiz_sayisi > 0:
        try:
            sayi = int(input("kelime tahmini için 1'e, harf tahmini için 2'ye basınız: "))
        except (UnboundLocalError, ValueError):
            print(" >>>>>>>>>>>HATA! 1 veya 2 değerlerinden birini girmediniz.<<<<<<<<<<<<<")
        if sayi == 1:
            kelime_tahmin = input("tahmininizi giriniz: ")
            if kelime_tahmin == kelime:
                print(">>>>>>>>>tebrikler!.. kelimeyi doğru tahmin ettiniz.")
                break
            else:
                print("yanlış tahmin!")
        elif sayi == 2:
            sayac4 = 0
            sayac2 = 0
            tahmin = input("harf tahmininizi giriniz: ")
            for k in harfler:
                if tahmin == k:
                    sifreli_liste[sayac2] = tahmin
                    sayac3 += 1
                    sayac4 += 1


                if not tahmin in harfler:
                    yildiz_sayisi -= 1
                    print("kalan can:" + yildiz_sayisi * "*")
                    if yildiz_sayisi == 6:
                        print(50 * "-")
                    elif yildiz_sayisi == 5:
                        print(50 * "-" + "---0")
                    elif yildiz_sayisi == 4:
                        print(50 * "-" + "---0")
                        print(50 * " " + "   |")
                    elif yildiz_sayisi == 3:
                        print(50 * "-" + "---0")
                        print(50 * " " + " _/|")
                    elif yildiz_sayisi == 2:
                        print(50 * "-" + "---0")
                        print(50 * " " + " _/|\_")
                    elif yildiz_sayisi == 1:
                        print(50 * "-" + "---0")
                        print(50 * " " + " _/|\_")
                        print(50 * " " + " _/")
                    elif yildiz_sayisi == 0:
                        print(50 * "-" + "---0")
                        print(50 * " " + " _/|\_ ")
                        print(50 * " " + " _/ \_")

                    if yildiz_sayisi == 0:
                        print("kaybettiniz! idama mahkumsunuz.")
                    break
                sayac2 = sayac2 + 1
            print(str(sayac4) + "'tane {} bulundu".format(tahmin))
            if sayac3 == uzunluk:
                print("kazandınız! artık idam edilmeyeceksiniz. ")
                break
            listeden_kurtar()
        else:
            print("geçersiz giriş yaptınız!")


ana_menu()


