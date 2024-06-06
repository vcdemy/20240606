import cv2
import numpy as np
from PIL import Image

# p1 = np.float32([[95,154],[383,42],[619,373],[300,524]])
p1 = []
p2 = np.float32([[200,50],[480,50],[480,500],[200,500]])

def show_xy(event,x,y,flags,userdata):
    global p1

    if event==1:
        print(event,x,y,flags)
        p1.append([x, y])
    
    if len(p1)==4:
        m = cv2.getPerspectiveTransform(np.float32(p1),p2)
        output = cv2.warpPerspective(img, m, mag.size)
        cv2.imshow("Corning02", output[:,:,::-1])
        p1.clear()


mag = Image.open('magazine.jpg')
img = np.array(mag)

cv2.imshow('Corning01', img[:,:,::-1])
cv2.setMouseCallback('Corning01', show_xy)


cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()