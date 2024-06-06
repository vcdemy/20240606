# 20240606


## PySide6 安裝

```bash
pip install PySide6
```

## Qt Designer 使用

`designer.exe` 會在 PySide6 的套件的根目錄。

```python
import PySide6

print(PySide6.__file__)
```

## Qt Designer 畫完的 UI 怎麼使用

1. 將設計好的介面存檔 (.ui)
2. 使用 pyside6-uic 將 .ui 檔轉換成 .py 檔
```bash
pyside6-uic practice.ui -o practice.py
```
3. 在自己的檔案中使用

```python
import practice # practice.py
import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
ui = practice.Ui_Form()
ui.setupUi(window)
window.show()
sys.exit(app.exec())
```







* OpenCV UI
* OpenCV mouseevent
* gradio進一步說明
* PyQT mouseevent
* PyQT layout 進一步使用
* PyQT 畫面大小的調整
* PyQT MessageBox
* PyQT QThread
* PyQT pyinstaller
* PyQT WebEngine
    * 使用來顯示 plotly 的東西
* Qt Designer 的使用

## Applications

* teachable machine 的使用
* keras application 的使用
* YOLO 配合 QThread 的使用
