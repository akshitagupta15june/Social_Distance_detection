import cv2
import imutils
#image=cv2.imread('social.jpeg')
cap=cv2.VideoCapture("thestreet.mp4")
while True:
    ret,frame=cap.read()
    frame=imutils.resize(frame,width=800)
    text="This is my custom text"
    cv2.putText(frame,text,(5,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
    cv2.rectangle(frame,(50,50),(100,100),(0,0,255),2)
    #cv2.imwrite("output",frame)
    cv2.imshow("application", frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()