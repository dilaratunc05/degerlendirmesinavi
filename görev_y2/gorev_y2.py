import cv2
import numpy as np

video = cv2.VideoCapture("#dosyayı yaz")

while True:
    ret, frame = video.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red1 =np.array([0,50,50]) # hue , saturation, values
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1= cv2.inRange(hsv,lower_red1,upper_red1)# pikseller arasındaki görüntüyü hsv adı altında algıladı 
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    masks = mask2 + mask1

    result= cv2.bitwise_and(frame,frame,mask=masks)
    cv2.imshow("kırmızı tespit edildi",result)

    contours = cv2.findContours(masks , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),2) #-1 tüm hepsiniçizer , 2 kalınlığı ayarlar

    contours=sorted(contours,key =cv2.contourArea,reverse=True)#reverse büyükten küçüğe gitmesini sağladı

    if len(contours)>0:
        biggest_contours = contours[0]

        x,y,w,h=cv2.boundingRect(biggest_contours)
        cv2.rectangle(frame,(x,y),(x+w, y +h),(0,255,0),2)

        object_center_x= x+w //2
        object_center_y= y+h//2
        cv2.circle(frame,( object_center_x, object_center_y),3,(255,0,0))#-1 neden ekleriz

        height,width ,_ =frame.shape
        frame_center_x=width//2
        frame_center_y= height//2

        error_x=frame_center_x-object_center_x
        error_y=frame_center_y-object_center_y
        
     
    

