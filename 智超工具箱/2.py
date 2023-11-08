import random
import sys
from time import sleep

import clipboard
from PySide6 import QtGui
from PySide6.QtCore import QBasicTimer, QCoreApplication, QMimeData, QObject, Qt, Signal
from PySide6.QtGui import QAction, QColor, QDrag, QFont, QImage, QPainter, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFileDialog,
    QGridLayout,
    QInputDialog,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSlider,
    QWidget,
)


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # btn1 = QPushButton('开始去除换行', self)
        # # btn1.setCheckable(True)
        # # btn1.clicked[bool].connect(self.remove_liner)
        # layout = QGridLayout()
        # layout.setSpacing(10)  # 间隔
        # layout.addWidget(btn1, 0, 0)
        
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('智超工具箱')        
        self.show()
    
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        '''按下键盘事件
        # modifiers()   判断修饰键
        # Qt.NoModifier   没有修饰键
        # Qt.ShiftModifier    Shift键被按下
        # Qt.ControlModifier    Ctrl键被按下
        # Qt.AltModifier      Alt键被按下
        '''
        if a0.key() == Qt.Key_C and a0.modifiers() == Qt.ControlModifier:
            n_s = clipboard.paste()
            if n_s != s:
                s = n_s.replace('\r\n', ' ')
                clipboard.copy(s)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())