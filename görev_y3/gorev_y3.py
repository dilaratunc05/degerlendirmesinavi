import cv2
import numpy as np
import time

video = cv2.VideoCapture("kirmizitoplarr.mp4")
frame_time=cv2.getTickCount()
freq=cv2.getTickFrequency()
qr_detector = cv2.QRCodeDetector()

start_time=None
is_locked= False
lost_time= None

while True:
    ret, frame = video.read()
    if not ret:
        print("video okunamadı.Dosya formatı desteklenmiyor olabilir.")
        break
    frame= cv2.resize(frame,(900,500))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red1 =np.array([0,50,50]) 
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1= cv2.inRange(hsv,lower_red1,upper_red1)
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    masks = mask2 + mask1

    result= cv2.bitwise_and(frame,frame,mask=masks)
    cv2.imshow("kırmızı tespit edildi",result)

    contours,_ = cv2.findContours(masks , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),2) 

    contours=sorted(contours,key =cv2.contourArea,reverse=True)

    time_now= cv2.getTickCount()
    diff_time= (time_now-frame_time)/freq 
    frame_time= time_now
    FPS = 1 / diff_time if diff_time >0 else 0
    show_fps=f"FPS:{FPS}"
    cv2.putText(frame,show_fps,(40,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    if len(contours)>0:
        biggest_contours = contours[0]

        x,y,w,h=cv2.boundingRect(biggest_contours)
        cv2.rectangle(frame,(x,y),(x+w, y +h),(0,255,0),2)

        object_center_x= x+w //2
        object_center_y= y+h//2
        cv2.circle(frame,( object_center_x, object_center_y),5,(255,0,0),-1)

        height,width ,_ =frame.shape
        frame_center_x=width//2
        frame_center_y= height//2
        
        error_x=frame_center_x-object_center_x
        error_y=frame_center_y-object_center_y
        
        show_error = f"Error x: {error_x}, ,Error y : {error_y}"
        cv2.putText(frame,show_error,(40,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

        #3.PROJE BURDAN İTİBAREN BAŞLIYOR

        height ,width ,_ =frame.shape

        box_w=int(width*0.25)
        bow_h=int(height*0.25)

        boxw_alt= (width- box_w)//2
        boxh_alt= (height- bow_h)//2
        boxw_ust= box_w + boxw_alt
        boxh_ust=bow_h + boxh_alt

        cv2.rectangle(frame,(boxw_alt,boxh_alt),(boxw_ust,boxh_ust),(255,0,0),2)

        if boxw_alt <= object_center_x <= boxw_ust and boxh_alt <= object_center_y <= boxh_ust:

            if start_time is None:
                 start_time=time.time()

            lost_time = None
            
            gecen_time= time.time()- start_time
            print(f"kutunun içinde geçen süre:{gecen_time} saniye")

            if gecen_time>= 4.0:
                is_locked = True
        else:
            if lost_time is None :
                lost_time = time.time()
            if time.time()- lost_time >= 0.2:
                start_time=None
                is_locked=False
            
                
    
        if is_locked:
            cv2.putText(frame,"KİLİTLENDİ",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),3)

    data, points, _ = qr_detector.detectAndDecode(frame)

    if data :
        print(f"Okunan QR kod:{data}.")
        cv2.putText(frame,data,(50,150), cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),3)
    
    cv2.imshow("kırmızı nesne takibi",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


