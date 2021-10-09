from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--上下文菜单')
        
        # 退出功能
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        # 保存功能
        saveAct = QAction(QIcon('save.png'),'保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        
        # 另存为功能
        saveasAct = QAction(QIcon('saveas.png'),'另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')

        # 新建功能
        newAct = QAction(QIcon('new.png'),'新建(&N)',self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        # 保存方式菜单
        saveMenu = QMenu('保存方式(&S)', self)
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('工具栏')  # 添加工具栏
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())