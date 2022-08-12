from codecs import BOM_UTF16_BE
from re import sub
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QSlider, QMainWindow, QGridLayout, QMessageBox, QMenu, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        # 按钮
        btn1 = QPushButton('按钮1', self)
        btn1.setToolTip('<b>测试</b>按钮')
        # btn1.move(0, 50)
        btn2 = QPushButton('退出', self)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        # btn2.move(100, 50)
        
        # 其他小组件
        
        
        # 布局
        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(btn1, 0, 0, 2, 1)
        layout.addWidget(btn2, 1, 1, 1, 2)
        
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
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('智超工具箱')        
        self.show()

    # 右键菜单
    def contextMenuEvent(self, event) -> None:
        cmenu = QMenu(self)
        
        act_new = cmenu.addAction('新建')
        act_open = cmenu.addAction('打开')
        act_quit = cmenu.addAction('退出')
        
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == act_quit:
            qApp.quit()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '嗯？',
            "你要退我？？？", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())