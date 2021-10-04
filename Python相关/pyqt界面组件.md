# 一个简单的窗口

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)  # 设置窗口尺寸
    w.move(300, 300)  # 移动窗口
    w.setWindowTitle('Simple')  # 设置窗口标题
    w.show()  # 显示窗口
    
    sys.exit(app.exec_())
```

# 使用对象实现窗口

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

        
if __name__ == '__main__'：
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

# 添加