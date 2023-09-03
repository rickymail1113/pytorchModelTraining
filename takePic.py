import os
import cv2
from time import strftime
labels = ['nophone', 'phone']
# labels = ['nomask', 'mask']
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    cv2.imshow('Tack Pic', image)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('0'):
        systime = strftime('%Y%m%d%H%M%S')
        imagename = os.path.join('data/images', labels[0]+'_'+systime+'.jpg')
        cv2.imwrite(imagename, image)
    elif key == ord('1'):
        systime = strftime('%Y%m%d%H%M%S')
        imagename = os.path.join('data/images', labels[1]+'_'+systime+'.jpg')
        cv2.imwrite(imagename, image)

cap.release()
cv2.destroyAllWindows()
