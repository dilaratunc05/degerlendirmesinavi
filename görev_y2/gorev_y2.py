import cv2
import numpy as np

video = cv2.VideoCapture("#dosyayı yaz")

while True:
    ret, frame = video.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red1 =np.array([0,50,50]) # hue , saturation, value
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1= cv2.inRange(hsv,lower_red1,upper_red1)# pikseller arasındaki görüntüyü hsv adı altında algıladı 
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    masks = cv2.bitwise_or(mask1, mask2)

    result= cv2.bitwise_and(frame,frame,mask=mask)
    