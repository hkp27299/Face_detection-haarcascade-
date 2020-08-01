import cv2

faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success,img = cap.read()
    cv2.imshow('WebCam',img)
    faces = faceCascade.detectMultiScale(img,1.1,4)
    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img," Face",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
        cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
