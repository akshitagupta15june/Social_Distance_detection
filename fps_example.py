import cv2
import datetime
import imutils
cap=cv2.VideoCapture('thestreet.mp4')
fps_start_time=datetime.datetime.now()
fps=0
total_frames=0
while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=800)
    total_frames=total_frames+1

    fps_end_time=datetime.datetime.now()
    time_diff=fps_end_time-fps_start_time
    if time_diff.seconds==0:
        fps=0.0
    else:
        fps = (total_frames / time_diff.seconds)



    fps_text="FPS: {:.2f}".format(fps)
    cv2.putText(frame,fps_text,(5,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
    cv2.imshow("APPLICATION",frame)
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()



