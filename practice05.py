import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, QThread
import skimage
from ultralytics import YOLO

model = YOLO()
file_name = None

thread_a = QThread()
thread_b = QThread()


def open_file():
    global file_name, thread_a, thread_b
    file_name, _ = QFileDialog.getOpenFileName(window, 'Open Image File', '', 'Image Files (*.png *.jpg *.bmp)')
    if file_name:
        thread_a.run = pic1       # 設定該執行緒執行 a()
        thread_a.start()          # 啟動執行緒
        thread_b.run = pic2       # 設定該執行緒執行 b()
        thread_b.start()


def pic1():
    global file_name
    pixmap1 = QPixmap(file_name)
    pixmap1 = pixmap1.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label1.setPixmap(pixmap1)

def pic2():
    global file_name
    results = model(file_name)
    results[0].save('temp.jpg')
    pixmap2 = QPixmap('temp.jpg')
    pixmap2 = pixmap2.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label2.setPixmap(pixmap2)

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

window.show()

sys.exit(app.exec())