import socket
import struct
import arac
import gorev_y4
import time

sckt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
teslim_yeri= ("127.0.0.1",1000)
sckt.bind(teslim_yeri)

FORMAT = "!2B2I7fB"
veri_formati="!2B2I7f"

try:
    while True:
        veri_paketi,adres=sckt.recvfrom(1024)

        gelen_veri= veri_paketi[:-1]
        gelen_cksum = veri_paketi[-1]

        cksum_start= 0
        for b in gelen_veri:
            cksum_start ^= b

        if gelen_cksum != cksum_start:
                print("Cheksumlar uyuşmuyor.")
                continue

            
        cozulmus_veri=struct.unpack(veri_formati,gelen_veri)

        baslik1 = cozulmus_veri[0]
        baslik2 = cozulmus_veri[1]
        paket_no = cozulmus_veri[2]
        zaman = cozulmus_veri[3]
        enlem = cozulmus_veri[4]
        boylam = cozulmus_veri[5]
        irtifa = cozulmus_veri[6]
        hiz = cozulmus_veri[7]
        batarya = cozulmus_veri[8]
        x = cozulmus_veri[9]
        y = cozulmus_veri[10]

        if baslik1 == 0xAA and batarya== 0x55:
             print(f"paket {paket_no} alındı.Hız:{hiz},İrtifa:{irtifa},Batarya:{batarya}")
        else:
             print("Paket başlığı uyuşmadı")

except KeyboardInterrupt:
     print("yer istasyonu kapatıldı")
     sckt.close()
        



