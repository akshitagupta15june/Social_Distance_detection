import cv2
import numpy as np
import imutils
modelpath="MobileNetSSD_deploy.caffemodel"
protopath="MobileNetSSD_deploy.prototxt"
detector=cv2.dnn.readNetFromCaffe(prototxt=protopath,caffeModel=modelpath)
CLASSES=["background", "aeroplane", "bicycle", "bird", "boat",
"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
"sofa", "train", "tvmonitor"]

image=cv2.imread('people.jpg')
image=imutils.resize(image,width=800)
(H,W)=image.shape[:2]
blob=cv2.dnn.blobFromImage(image,0.007843,(H,W),127.5)
detector.setInput(blob)
person_detections=detector.forward()
for i in np.arange(0,person_detections.shape[2]):
    confidence=person_detections[0,0,i,2]
    if confidence>0.5:
        idx=int(person_detections[0,0,i,1])
        if CLASSES[idx]!="person":
            continue
        person_box=person_detections[0,0,i,3:7]*np.array([W,H,W,H])
        (startX,startY,endX,endY)=person_box.astype("int")
        cv2.rectangle(image,(startX,startY),(endX,endY),(0,255,0),2)
cv2.imshow("results",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
