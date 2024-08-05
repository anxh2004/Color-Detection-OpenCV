import cv2
from utils import get_limit

from PIL import Image

cap = cv2.VideoCapture(0)

yellow =[0,255,255]   # yellow in bgr colorspace
while True:
    ret,frame = cap.read()

    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit,upperLimit = get_limit(color=yellow)

    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit)

    mask_ = Image.fromarray(mask)   # converting from numpy to pillow  # using pillow to get bounding box

    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()


cv2.destroyAllWindows()