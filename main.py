import pymem
from time import sleep

def health():
    pm = pymem.Pymem("ac_client.exe") # oyunun adı, kısaca assault cube'un process'ini tanımlıyoruz.
    adress = 0x008F065C # can değerinin adresi, bunu cheat engine ile bulabilirsiniz.
    while True:
        sleep(0.1) # her 0.1 saniyede bir can değerini güncelliyoruz, yoksa bilgisayrı yavaşlatabilir.
        pm.write_int(adress, 9999) # can değerini 9999 yapıyoruz, döngüye aldık ki sürekli 9999 olsun

def ammo():
    pm = pymem.Pymem("ac_client.exe") # başlıca aynı process tanımı, sadece adres silah mermisinin adresi.
    adress = 0x008F06B0
    while True:
        sleep(0.1) 
        pm.write_int(adress, 999) 




if __name__ == "__main__":
    print("can ya da mermi seç (a/m): ")
    secenek = input().lower()
    if secenek == "a":
        health()
    elif secenek == "m":
        ammo()
    else:
        print("geçersiz seçenek")