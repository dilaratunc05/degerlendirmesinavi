# Kulüp Değerlendirme Sınavı - Yazılım ve Haberleşme Alanı
.
**PROJE 1 - GPS ile mesafe ve yön**
- `görev_y1`: Bu proje de GPS koordinatlarını kullanarak yön ve mesafe hesabı yapan bir yazılım geliştirildi.

*Kazanımlar:*
- Haversine Formülü:Dünya düz olmadığı için iki mesafe arasındaki gerçek uzunluk bu formülle hesaplandı.Enlem ve boylamlar arasındaki farkı radyana çevrip trigonometrik adımlardan geçirdikten sonra dünyanın yarıçapı ile çarparak hassas ölçüm elde edildi.
- Temel Python OOP/fonksiyon yapısı
- Matematiksel Fonksiyonlar
- Hata Yönetimi


**PROJE 2 - Görüntü işleme: renkli hedef tespiti**
- `görev_y2`:Bu projede video dosyaları üzerinden renk tespiti,nesne takibi ve FPS takibi yapan bir yazılım geliştirildi.

*Kazanımlar:*
- OpenCv ile kullanılan tüm yapılar , örneğin(cv2.getTickCount,cv2.imshow,cv2.drawCounters ve dahası)
- HSV renk filtrelemesinin neden ve nasıl kulllanıldığı:RGB renk uzayı ışık değişimlerinden çok etkilendiği için HSV kullanıldı(cv2.cvtColor ile dönüştürüldü).Aynı zamanda çift maskeleme ile kırmızının tüm tonları tespit edildi.
- Kontur ve sınır tespiti(cv2.findContours kullanıldı)
- Merkez ve Hata Hesaplama
- Gerçek zamanlı FPS takibi(cv2.getTickCount ve cv2.getTickFrequency kullanıldı)
- Renk parametreleri


**PROJE 3 - Kilitlenme mantığı ve QR okuma**
- `görev_y3`: Bu projede video dosyaları üzerinden hedefe kilitlenme ve kamera üzerinden QR okuma yazılımı geliştirildi.

*Kazanımlar:*
- Kilitleme MAntığı 
- Program ile kamera arasında bağlantı kurma
- Sayaç sistemi
- QR okuma


**PROJE 4 -  Telemetri paketi ve UDP haberleşmesi**
- `görev_y4`: Bu projede hava aracının uçuş esnasında topladığı telemetri verilerini UDP üzerinden yer istasyonuna aktarmasını sağlayan bir yazılım geliştirildi.

*Kazanımlar:*
- Struct: Birden fazla veri grubunu tek bir ad altında paket haline getirir.S
- Encode ve Decode : Encode 
- Socket Programlama: Bilgisayarların ağ üzerinden birbiriyle konuşmasını sağlayan yapı
- UDP ve TCP ile farkı: UDP ağ üzerinde veri gönderirken belli başlı görevleri temsil eder ve bağlantı kurmadan da paket gönderir.TCP ile farkı ise bağlantı kurmadan paketleri fırlatıyor olmasıdır TCP de bağlanttı şarttır.UDP doğrudan veri pakertlerini gönderdiği için daha hızlıdır TCP ise daha fazla işlem gücü ve zaman gerektirir.
- IPv4 ve Adresleme : IPv4 bilgisayarın ağda birbirini bulmasını sağlayan adresleme sistemidir. Socket.AF_INET parametresi ile kullandığımız adresi pythona bildiririz ve paketin tam yerine teslimi için bir de port numarası belirleriz.
- XOR Checksum(^): Verinin yolda bozulup bozulmadığını anlamak amacıyla paketin sonuna XOR tabanlı doğrulama baytı eklenir
- Paket Yapısı : Aktarılcak tüm telemetrileri bir format dizilimi altında yazarız(!2B2I7fB)



