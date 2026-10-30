import struct
import socket

FORMAT= "!2B2I7fB" #2 tane 1 baytlık sayı (başlık), 2 tane int (paket numarası ve zaman),7 tane float(enlem,boylam,irtifa,hız,batarya,x ve y),1 baytlık sayı (kilit durumu)
sckt= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def encode(paket_no,zaman,enlem,boylam,irtifa,hiz,batarya,x,y,kilit):
    baslik1= 0xAA
    baslik2=0x55

    data=struct.pack(FORMAT,baslik1,baslik2,paket_no,zaman,enlem,boylam,irtifa,hiz,batarya,x,y,kilit)

    cksum= 0
    for b in data:
        cksum ^= b
    total_packet= data + struct.pack("!B", cksum)

    return total_packet

def decode(veri_paketi):
    
    if len(veri_paketi) != 40:
        raise ValueError("Paket hatalı")
    
    gelen_veri= veri_paketi[:-1]
    gelen_cksum = veri_paketi[-1]
    
    cksum_start= 0
    for b in gelen_veri:
        cksum_start ^= b
    
    if gelen_cksum != cksum_start:
        print(f"Cheksumlar uyuşmuyor.")
        raise ValueError("Cheksum hatalı")

    cozulmus_veri=struct.unpack(FORMAT,gelen_veri)

    baslik1 = cozulmus_veri[0]
    baslik2 = cozulmus_veri[1]

    if baslik1 != 0xAA and baslik2 != 0x55:
        raise ValueError("Paket başlığı hatalı")
    
    return cozulmus_veri



    
