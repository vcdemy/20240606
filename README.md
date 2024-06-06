# 20240606


## PySide6 安裝

```bash
pip install PySide6
```

## Qt Designer 使用

`designer.exe` 會在 PySide6 的套件的跟目錄。

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
ui = test01.Ui_Form()
ui.setupUi(window)
window.show()
sys.exit(app.exec())
```








