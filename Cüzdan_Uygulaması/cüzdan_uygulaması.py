import json
import os

def dosya_kaydet(kullanici):
    if not os.path.exists("kullanicilar.json"):
        with open("kullanicilar.json", "w") as dosya:
            json.dump({}, dosya)
    
    with open("kullanicilar.json", "r+") as dosya:
        kullanicilar = json.load(dosya)
        kullanicilar[kullanici["email"]] = kullanici
        dosya.seek(0)
        json.dump(kullanicilar, dosya, indent=3)

def kullanici_dosyasindan_yukle(email):
    if not os.path.exists("kullanicilar.json"):
        return None
    
    with open("kullanicilar.json", "r") as dosya:
        kullanicilar = json.load(dosya)
    
    return kullanicilar.get(email)

def giris_yap():
    email = input("E-posta: ")
    sifre = input("Şifre: ")

    kullanici = kullanici_dosyasindan_yukle(email)
    if kullanici and kullanici["sifre"] == sifre:
        print(f"Giriş başarılı!\nBakiyeniz: {kullanici['bakiye']}")
        return kullanici
    else:
        print("Geçersiz kullanıcı bilgileri!")
        return None

def kayit_ol():
    email = input("E-posta: ")
    sifre = input("Şifre: ")
    
    if kullanici_dosyasindan_yukle(email):
        print("Bu kullanıcı zaten var!")
        return

    kullanici = {
        "email": email,
        "sifre": sifre,
        "bakiye": 0
    }
    dosya_kaydet(kullanici)
    print("Kayıt başarılı!")

def bakiye_guncelle(kullanici, tutar):
    kullanici["bakiye"] += tutar
    dosya_kaydet(kullanici)

def menu():
    while True:
        print(20 * "-" + "Cüzdan Uygulaması" + 20 * "-")
        print("1- Giriş Yap")
        print("2- Kayıt Ol")
        print("3- Çıkış")
        
        secim = input("Bir işlem seçin: ")
        
        if secim == "1":
            kullanici = giris_yap()
            if kullanici:
                while True:
                    print("1- Bakiyeyi Görüntüle")
                    print("2- Bakiye Ekle")
                    print("3- Bakiye Çek")
                    print("4- Çıkış Yap")
                    
                    islem = input("Bir işlem seçin: ")
                    
                    if islem == "1":
                        print(f"Bakiyeniz: {kullanici['bakiye']}")
                    elif islem == "2":
                        tutar = float(input("Eklemek istediğiniz tutar: "))
                        bakiye_guncelle(kullanici, tutar)
                        print(f"{tutar} eklenmiştir. Yeni bakiye: {kullanici['bakiye']}")
                    elif islem == "3":
                        tutar = float(input("Çekmek istediğiniz tutar: "))
                        if kullanici["bakiye"] >= tutar:
                            bakiye_guncelle(kullanici, -tutar)
                            print(f"{tutar} çekilmiştir. Yeni bakiye: {kullanici['bakiye']}")
                        else:
                            print("Yetersiz bakiye!")
                    elif islem == "4":
                        break
        elif secim == "2":
            kayit_ol()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim!")

menu()