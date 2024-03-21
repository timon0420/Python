from platform import release
from cv2 import VideoCapture, cvtColor, putText
import numpy as np
import cv2

cam = VideoCapture(0)
while True:
    ret, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))
    hsv = cvtColor(frame, cv2.COLOR_BGR2HSV) #(HSV) określenie koloru oznacza odcień, nasycenie i jasność #Funkcja zmieniająca kolor obrazu z systemu BGR na system HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue) #Funkcja tworząca maskę która wyświetla tylko kolory z podanego przedziału
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows