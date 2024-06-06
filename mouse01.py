from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(800, 600)

def mousePress(event):
    print(event)
    print(f"{event.position().x()}, {event.position().y()}")
    print(f"{Form.x()}, {Form.y()}")

Form.mousePressEvent  = mousePress    # 新增按下滑鼠事件，事件發生時執行 mousePress 函式

Form.show()
sys.exit(app.exec())