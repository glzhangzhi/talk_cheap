'''
https://maicss.gitbook.io/pyqt-chinese-tutoral/pyqt5/kong-jian-2
'''

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import (QBasicTimer, QCoreApplication, QMimeData, QObject,
                          Qt, pyqtSignal)
from PyQt5.QtGui import QDrag, QImage, QPixmap, QPainter, QColor, QFont
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
                             QFileDialog, QGridLayout, QInputDialog, QLabel,
                             QLCDNumber, QLineEdit, QMainWindow, QMenu,
                             QMessageBox, QProgressBar, QPushButton, QSlider,
                             QWidget, qApp)


# 自定义一个信号
class Communicate(QObject):
    closeApp = pyqtSignal()
    
# 自定义一个可拖拽按钮
class DragButton(QPushButton):
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class DragButton2(QPushButton):
    
    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos - self.rect().topLeft())
        dragAction = drag.exec_(Qt.MoveAction)

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        # 自定义信号
        self.c = Communicate()
        self.c.closeApp.connect(self.close)  # 将信号的出发链接到关闭行为
        
        # 按钮
        btn1 = QPushButton('按钮1', self)
        btn1.setToolTip('<b>测试</b>按钮')
        btn1.clicked.connect(self.buttonClicked)
        # btn1.move(0, 50)
        
        btn2 = QPushButton('退出', self)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        # btn2.move(100, 50)
        
        btn3 = QPushButton('对话框', self)
        btn3.clicked.connect(self.showDialog)
        
        # 切换按钮
        btn4 = QPushButton('切换红', self)
        btn4.setCheckable(True)  # 感觉如果不做什么修改的话，这个状态切换不如checkbox直观
        btn4.clicked[bool].connect(self.setColor)
        btn5 = QPushButton('切换绿', self)
        btn5.setCheckable(True)
        btn5.clicked[bool].connect(self.setColor)
        # self.btn6 = QPushButton('拖我', self)
        # self.btn6.move(0, 400)
        
        # LCD数字显示
        lcd = QLCDNumber(self)
        
        # 滑动条
        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged.connect(lcd.display)
        sld.valueChanged.connect(self.changeValue)

        # 文字
        # self.label = QLabel(self)
        
        # 单选框
        cb = QCheckBox('显示标题', self)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        # 进度条
        self.pbar = QProgressBar()
        self.btn6 = QPushButton('开始', self)
        self.btn6.clicked[bool].connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        
        # 单行文本输入框
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.textChanged[str].connect(self.onChanged)
        
        # 显示图片
        pixmal = QPixmap('map.jpg')
        pixmal = pixmal.scaled(200, 200, Qt.KeepAspectRatio)
        lbl = QLabel(self)
        lbl.setPixmap(pixmal)
        
        # 下拉框
        combo = QComboBox(self)
        combo.addItem('a')
        combo.addItem('b')
        combo.addItem('c')
        combo.addItem('d')
        combo.activated[str].connect(self.onActivated)
        
        # 可接受拖动文本按钮
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        button = DragButton('Button', self)
        
        # 布局
        layout = QGridLayout()
        layout.setSpacing(10)  # 间隔
        layout.addWidget(btn1, 0, 0)
        layout.addWidget(btn3, 0, 1)
        layout.addWidget(btn2, 0, 2)
        # layout.addWidget(self.label, 0, 2)
        layout.addWidget(lcd, 1, 0)
        layout.addWidget(sld, 1, 1, 1, 2)  # 后两个参数设置该组件所占行数和列数
        layout.addWidget(cb, 2, 0)
        layout.addWidget(btn4, 2, 1)
        layout.addWidget(btn5, 2, 2)
        layout.addWidget(self.pbar, 3, 0, 1, 2)
        layout.addWidget(self.btn6, 3, 2)
        layout.addWidget(lbl, 4, 0, 2, 3)
        layout.addWidget(qle, 6, 0, 1, 2)
        layout.addWidget(self.lbl, 6, 2)
        layout.addWidget(combo, 7, 0)
        layout.addWidget(edit, 7, 1)
        layout.addWidget(button, 7, 2)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # 状态栏
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('预备备')
        
        # 菜单栏
        act1 = QAction('退出', self)
        act1.setShortcut('ctrl+Q')
        act1.triggered.connect(QCoreApplication.instance().quit)
        
        menubar = self.menuBar()
        menu1 = menubar.addMenu('菜单1')
        menu1.addAction(act1)
        menu2 = menubar.addMenu('菜单2')
        sub_menu1 = menu2.addMenu('子菜单1')
        sub_menu1.addAction(act1)
        
        # 工具栏
        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(act1)

        # 窗口
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('智超工具箱')        
        self.show()

    
    def contextMenuEvent(self, event) -> None:
        '''右键菜单事件'''
        cmenu = QMenu(self)
        
        act_new = cmenu.addAction('新建')
        act_open = QAction('打开')
        act_open.triggered.connect(self.openFileDialog)
        cmenu.addAction(act_open)
        act_quit = cmenu.addAction('退出')
        
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == act_quit:
            qApp.quit()

    def closeEvent(self, event):
        '''关闭窗口事件'''
        reply = QMessageBox.question(self, '嗯？',
            "你要退我？？？", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

    
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        '''按下键盘事件'''
        if a0.key() == Qt.Key_Escape:
            self.close()
        elif a0.key() == Qt.Key_Q:
            self.c.closeApp.emit()  # 触发自定义信号
    
    # 移动鼠标事件
    # TODO 目前这个只能显示当鼠标按下或者释放时的位置，或者一直按下
    # def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
    #     self.label.setText(f'x:{a0.x()} y:{a0.y()}')

    def buttonClicked(self):
        '''自定义按下鼠标响应函数'''
        sender = self.sender()
        self.statusbar.showMessage(sender.text())
    
    def showDialog(self):
        '''自定义显示对话框响应函数'''
        text, ok = QInputDialog.getText(self, '输入框', '随便搞点什么')
        if ok:
            self.statusbar.showMessage(text)
    
    def openFileDialog(self):
        '''打开选择文件对话框'''
        fname = QFileDialog.getOpenFileName(self, '打开文件', '.')
        if fname[0]:
            self.statusbar.showMessage(fname[0])
     
    def changeTitle(self, state):
        '''根据单选框更改标题状态'''
        # state: 0 未勾选 1 部分勾选 2 勾选
        self.statusbar.showMessage(str(state))
        if state == Qt.Checked:
            self.setWindowTitle('勾上啦')
        else:
            self.setWindowTitle('没勾上')
    
    def setColor(self, pressed):
        '''根据切换按钮的来源响应功能'''
        source = self.sender()
        self.statusbar.showMessage(f'{pressed=} {source.text()}')
        
    def changeValue(self, value):
        '''接收滑动条改变数值并显示在状态栏上'''
        self.statusbar.showMessage(str(value))
    
    def doAction(self):
        """根据计时器不同的状态来更改按钮的文本"""
        print(self.timer.isActive(), self.step)
        if self.timer.isActive():
            self.timer.stop()
            self.btn6.setText('Start')
        else:
            self.step = 0
            self.timer.start(100, self)
            self.btn6.setText('Stop')
    
    def timerEvent(self, a0) -> None:
        """进度条更新"""
        if self.step >= 100:
            self.timer.stop()
            self.btn6.setText('restart')
            return
        self.step += 1
        self.pbar.setValue(self.step)
    
    def onChanged(self, text):
        """使用输入框的文本动态更细label文本"""
        self.lbl.setText(text)
        self.lbl.adjustSize()  # lbl会根据内容的多少，动态调节整体窗口的大小
    
    def onActivated(self, text):
        self.statusbar.showMessage(text)
        
    # def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
    #     a0.accept()
    
    # def dropEvent(self, a0: QtGui.QDropEvent) -> None:
    #     position = a0.pos()
    #     self.btn6.move(position)
    #     a0.setDropAction(Qt.MoveAction)
    #     a0.accept()

    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
