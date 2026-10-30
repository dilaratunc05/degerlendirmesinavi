import time 
import socket
import struct
import gorev_y4

sckt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
teslim_yeri= ("127.0.0.1",1000)
sckt.bind(teslim_yeri)

FORMAT = "!2B2I7fB"

bozuk_sayac=0
kayip_sayac=0
son_paket_no=0


print("Yer istasyonuna bağlanıldı.")
try: 
    while True:
        veri_paketi, adres= sckt.recvfrom(1024)

        if len(veri_paketi) == 40:
            baslik1, baslik2, gelen_paket_no = struct.unpack("!2BI", veri_paketi[:6])

            if baslik1 == 0xAA and baslik2 == 0x55:
                if son_paket_no != 0 and gelen_paket_no > son_paket_no + 1:
                    fark = gelen_paket_no - son_paket_no - 1
                    kayip_sayac += fark
                    print(f"Arada {fark} paket kayboldu. Toplam kayıp: {kayip_sayac}")

                son_paket_no = gelen_paket_no
        try :
            cozulmus_veri=gorev_y4.decode(veri_paketi)
        except ValueError as hata:
            bozuk_sayac += 1
            print(f"Geçersiz paket: {hata}. Toplam hatalı: {bozuk_sayac}")
            continue

 
        paket_no = cozulmus_veri[2]
        zaman = cozulmus_veri[3]
        enlem = cozulmus_veri[4]
        boylam = cozulmus_veri[5]
        irtifa = cozulmus_veri[6]
        hiz = cozulmus_veri[7]
        batarya = cozulmus_veri[8]
        x = cozulmus_veri[9]
        y = cozulmus_veri[10]
        kilit= cozulmus_veri[11]

        print(f"Paket {paket_no} alındı. Hız: {hiz}, İrtifa: {irtifa}, Batarya: {batarya}") 


except KeyboardInterrupt:
     print("Yer istasyonu kapatıldı")
     sckt.close()
        



