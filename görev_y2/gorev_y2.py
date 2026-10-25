import cv2
import numpy as np

video = cv2.VideoCapture("kirmizitoplar.mp4")
frame_time=cv2.getTickCount()
freq=cv2.getTickFrequency()
while True:
    ret, frame = video.read()
    if not ret:
        print("HATA: Video karesi okunamadı! Dosya formatı desteklenmiyor olabilir.")
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
        cv2.circle(frame,( object_center_x, object_center_y),3,(255,0,0),-1)

        height,width ,_ =frame.shape
        frame_center_x=width//2
        frame_center_y= height//2

        error_x=frame_center_x-object_center_x
        error_y=frame_center_y-object_center_y

        show_error = f"Error x: {error_x}, ,Error y : {error_y}"
        cv2.putText(frame,show_error,(40,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("kırmızı nesne takibi",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()




    

