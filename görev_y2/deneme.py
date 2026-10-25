import cv2
import numpy as np

# 30 saniyelik boş bir avi video üretici kuruyoruz
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test_video.avi', fourcc, 20.0, (640, 480))

# İçine hareket eden kırmızı bir top çizen 100 tane kare (frame) ekleyelim
for i in range(100):
    frame = np.zeros((480, 640, 3), dtype=np.uint8) # Siyah arka plan
    # Hareket eden kırmızı bir daire çiziyoruz
    cv2.circle(frame, (100 + i * 3, 240), 30, (0, 0, 255), -1) 
    out.write(frame)

out.release()
print("Test videosu başarıyla oluşturuldu: test_video.avi")