import cv2
import numpy as np
from PIL import Image

mag = Image.open('magazine.jpg')
p1 = np.float32([[95,154],[383,42],[619,373],[300,524]])
p2 = np.float32([[200,50],[480,50],[480,500],[200,500]])
m = cv2.getPerspectiveTransform(p1,p2)

img = np.array(mag)
output = cv2.warpPerspective(img, m, mag.size)

cv2.imshow('Corning01', img[:,:,::-1])
cv2.imshow('Corning02', output[:,:,::-1])

cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()