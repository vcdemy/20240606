from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
import plotly.express as px
import skimage
import sys


app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("Plotly in PyQt")
window.setGeometry(100, 100, 800, 600)

web_view = QWebEngineView(window)
web_view.resize(800, 600)
img = skimage.io.imread('therock.jpg')
fig = px.imshow(img)
web_view.setHtml(fig.to_html(include_plotlyjs='cdn'))

window.show()
sys.exit(app.exec())