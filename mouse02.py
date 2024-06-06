from PyQt6 import QtWidgets
import sys
from PyQt6.QtGui import QCursor

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(800, 600)

def mousePress(event):
    print('press')

def mouseMove(self):
    mx = QCursor.pos().x() - Form.x()
    my= QCursor.pos().y() - Form.y()
    print(f'{mx}, {my}') 

Form.mouseMoveEvent  = mouseMove    # 新增按下滑鼠事件，事件發生時執行 mousePress 函式

Form.show()
sys.exit(app.exec())