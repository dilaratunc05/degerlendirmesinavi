# Kulüp Değerlendirme Sınavı - Yazılım ve Haberleşme Alanı
.
**PROJE 1 - GPS ile mesafe ve yön**
- `görev_y1`: Bu proje de GPS koordinatlarını kullanarak yön ve mesafe hesabı yapan bir yazılım geliştirildi.

-*Kazanımlar:*
- Haversine Formülü:Dünya düz olmadığı için iki mesafe arasındaki gerçek uzunluk bu formülle hesaplandı.Enlem ve boylamlar arasındaki farkı radyana çevrip trigonometrik adımlardan geçirdikten sonra dünyanın yarıçapı ile çarparak hassas ölçüm elde edildi.
- Temel Python OOP/fonksiyon yapısı
- Matematiksel Fonksiyonlar
- Hata Yönetimi


**PROJE 2 - Görüntü işleme: renkli hedef tespiti**
-`görev_y2`:Bu projede video dosyaları üzerinden renk tespiti,nesne takibi ve FPS takibi yapan bir yazılım geliştirildi.
-*Kazanımlar:*
-OpenCv ile kullanılan tüm yapılar , örneğin(cv2.getTickCount,cv2.imshow,cv2.drawCounters ve dahası)
-HSV renk filtrelemesinin neden ve nasıl kulllanıldığı:RGB renk uzayı ışık değişimlerinden çok etkilendiği için HSV kullanıldı(cv2.cvtColor ile dönüştürüldü).Aynı zamanda çift maskeleme ile kırmızının tüm tonları tespit edildi.
- Kontur ve sınır tespiti(cv2.findContours kullanıldı)
- Merkez ve Hata Hesaplama
- Gerçek zamanlı FPS takibi(cv2.getTickCount ve cv2.getTickFrequency kullanıldı)
- Renk parametreleri


**PROJE 3 - Kilitlenme mantığı ve QR okuma**
-`görev_y3`: Bu projede video dosyaları üzerinden hedefe kilitlenme ve kamera üzerinden QR okuma yazılımı geliştirildi.
-*Kazanımlar:*
- Kilitleme MAntığı 
- Program ile kamera arasında bağlantı kurma
- Sayaç sistemi
- QR okuma


**PROJE 4 -  Telemetri paketi ve UDP haberleşmesi**
struct yapısı ayrı değişkenleri ,birden fazlya veri grubunu tek bir ad altında paket haline getirmeyi sağlayan yapıdır coody.tech fehmi uyar. socketin bilgisayaların ağ üzerinden birbiriyle konuşmasını sağlayan bir yapı olduğunu öğrendim.UDP nin ağ üzerinde veri gönderirken kuralları temsil ettiğini öğrendim saniyede on paket atabildiğini ve sürekli taze veriyi fırlattığını öğrendim.IPv4 unBilgisayarların ağda birbirini bulmasını sağlar yani bizm kullandığımız 127.0.0.1 adresleme sistemlerinin genel adı ve bunu da AF_INET diyerek pythoma ben bunu kullancam demiş oluruz tabii paketin tam yerine teslimi için sadce bunlar değil bir port numarasıda vermemzi gerektiğini öğrendim



