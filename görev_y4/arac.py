import socket
import time
import gorev_y4 
import random

sckt= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hedef = ("127.0.0.1", 1000)
paket_no=0
zaman=0

try:
    while True:
        paket_no += 1
        zaman += 100
        enlem=63.47
        boylam=75.65
        irtifa=150
        hiz=38.3
        batarya=97.0
        x=5.3
        y=4.7
        kilit = 1

        data_packet=gorev_y4.encode(paket_no, zaman, enlem, boylam, irtifa, hiz, batarya, x, y,kilit)

        r= random.random()
        if r <0.02:
            print("Paket kayboldu")
            continue
        elif r <0.07:
            data_packet=data_packet[:-1] + bytes([data_packet[-1]^ 0xFF])
            print(f"Paket yolda bozuldu")


        sckt.sendto(data_packet,hedef)
        print(f"Paket {paket_no} gönderildi")

        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"Bilgiler şuan gönderilmiyor.")
    sckt.close()



