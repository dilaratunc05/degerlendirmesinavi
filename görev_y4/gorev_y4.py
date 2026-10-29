import struct

FORMAT= "!2B2I7fB" #2 tane 1 baytlık sayı (başlık), 2 tane int (paket numarası ve zaman),7 tane float(enlem,boylam,irtifa,hız,batarya,x ve y),1 baytlık sayı (kilit durumu)


def packet(paket_no,zaman,enlem,boylam,irtifa,hiz,batarya,x,y,kilit_durumu):
    baslik1= 0xAA
    baslik2=0x55

    data=struct.pack(FORMAT,baslik1,baslik2,paket_no,zaman,enlem,boylam,irtifa,hiz,batarya,x,y,kilit_durumu)

    cksum= 0
    for b in data:
        cksum ^= b
    total_packet= data + struct.pack("!B", cksum)

    return total_packet

    
