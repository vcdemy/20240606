import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

app = QApplication(sys.argv)
window = uic.loadUi('test.ui')
window.show()
sys.exit(app.exec())
