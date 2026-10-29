import socket
import time
import gorev_y4
import packet 

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

        data_packet=packet(paket_no, zaman, enlem, boylam, irtifa, hiz, batarya, x, y,kilit)

        sckt.sendto(data_packet,hedef)
        print(f"Paket {paket_no} gönderildi")

        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"Bilgiler şuan gönderilmiyor.")
    sckt.close()



