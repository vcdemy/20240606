import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import skimage
from PIL import Image
import numpy as np
import cv2

# p1 = np.float32([[95,154],[383,42],[619,373],[300,524]])
p1 = []
p2 = np.float32([[200,50],[480,50],[480,500],[200,500]])
ori = None
before = None
after = None

def open_file():
    global ori, before, after
    file_name, _ = QFileDialog.getOpenFileName(window, 'Open Image File', '', 'Image Files (*.png *.jpg *.bmp)')
    if file_name:
        pixmap1 = QPixmap(file_name)
        ori = Image.open(file_name)
        before = ori.size
        temp = ori.copy()
        temp.thumbnail((300, 300))
        after = temp.size
        print(before, "==>", after)
        pixmap1 = pixmap1.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        label1.setPixmap(pixmap1)


def mousePress(event):
    print(f"{event.position().x()}, {event.position().y()}")
    global ori, p1
    img = np.array(ori)

    
    x = event.position().x()
    y = event.position().y()
    scale = before[0] / after[0]
    nx = (x - 150) * scale + before[0]/2
    ny = (y - 150) * scale + before[1]/2
    p1.append([nx, ny])
    print(p1)
    
    if len(p1)==4:
        m = cv2.getPerspectiveTransform(np.float32(p1),p2)
        output = cv2.warpPerspective(img, m, before)
        bytes_per_line = output.shape[1] * output.shape[2]
        q_image = QImage(output, output.shape[1], output.shape[0], bytes_per_line, QImage.Format.Format_RGB888)
        pixmap2 = QPixmap.fromImage(q_image)
        pixmap2 = pixmap2.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        label2.setPixmap(pixmap2)
        p1.clear()
        # cv2.imwrite('output.jpg', output)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('課間小專案')
window.setFixedSize(640, 360)
label1 = QLabel(window)
label2 = QLabel(window)
button = QPushButton('Open File', window)
label1.setFixedSize(300, 300)
label1.move(10, 10)
label2.setFixedSize(300, 300)
label2.move(325, 10)
button.setGeometry(10, 320, 150, 30)
label1.setStyleSheet('background-color: gray')
label2.setStyleSheet('background-color: gray')

button.clicked.connect(open_file)
button.setStyleSheet('border: 1px solid black')

label1.mousePressEvent  = mousePress

window.show()

sys.exit(app.exec())