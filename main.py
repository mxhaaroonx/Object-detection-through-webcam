import cv2

first=None

vid=cv2.VideoCapture(1)

while True:
    check,frame=vid.read()
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) #to cancel the noise and improve accuracy
    if first is None:
        first=gray #to store the first frame
        continue
    delta_frame=cv2.absdiff(first,gray)# takes the absolute value of the difference
    
    tresh=cv2.threshold(delta_frame,28, 255, cv2.THRESH_BINARY)[1] #RETURNS A TUPLE So the acceessing 2nd value is enough
    tresh=cv2.dilate(tresh,None, iterations=2) 
    
    (cnts,_)= cv2.findContours(tresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#to find the contours of the white objects
    
    for c in cnts:
        if cv2.contourArea(c)<800:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0), 3)#creating a rectangle
    
    #cv2.imshow("Capture", gray)
    #cv2.imshow("delta", delta_frame)
    #cv2.imshow("tHREShhold", tresh)
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    print(delta_frame)
    if key==ord('q'):
        break;


video.release()
cv2.destroyAllWindows()