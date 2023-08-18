
def hesap_makinesi():

    islem = int(input("İslem secin, 1: Toplama 2: Çıkarma 3: Çarpma 4: Bölme"))
    sayi1 = int(input("İlk sayi girin:"))
    sayi2 = int(input("İkinci sayi girin:"))


    if islem == 1:
        toplam = sayi1 + sayi2
        print ("Cevap," ,toplam)

    elif islem == 2:
        cikartma = sayi1 - sayi2
        print ("Cevap",cikartma)

    elif islem == 3:
        carpma = sayi1 * sayi2
        print ("Cevap",carpma)

    elif islem ==4:
        print("şuan ayarlanmadı ")
    
    
    else:
        print("Hatali giris")
    
    a = str(input("Birdaha çalıştırmak ister misiniz, y (yes/evet), kalan seçenekler işlemi sonlandıracaktır"))

    if a == "y":
        hesap_makinesi()

    else:
        print("İyi gunler")
    






    

hesap_makinesi()













