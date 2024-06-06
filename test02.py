import test01
import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
ui = test01.Ui_Form()
ui.setupUi(window)
window.show()
sys.exit(app.exec())