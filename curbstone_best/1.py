# PyQt5.QtCore  # 线程，事件
# PyQt5.QtGui  # 事件，Painting
# PyQt5.QtWidgets  # 小部件

import sys
from pathlib import Path

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QIcon, QKeySequence, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QComboBox, QFileDialog,
                             QFileSystemModel, QGraphicsView, QGridLayout,
                             QHBoxLayout, QLabel, QLCDNumber, QListView,
                             QMainWindow, QMenu, QMenuBar, QPushButton,
                             QSpinBox, QStatusBar, QStyle, QToolBar,
                             QToolButton, QTreeView, QVBoxLayout, QWidget)


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # 可以在这里设置一些窗口都用得到的变量
        self.init_ui()

    def test(self):
        print(123)

    def get_dir_path(self):
        '''获取目录路径

        Returns:
            Path Object: pathlib Path object
        '''
        self.dir_path = QFileDialog.getExistingDirectory(self, '', './')
        print(self.dir_path)
        self.tv.update()

    def init_ui(self):
        # 工具栏
        toolbar = QToolBar()
        action_select_project_path = QAction(self)
        action_select_project_path.setIcon(QApplication.style().standardIcon(22))
        action_select_project_path.setToolTip("Open Project Path")
        action_select_project_path.triggered.connect(self.get_dir_path)
        toolbar.addAction(action_select_project_path)
        self.addToolBar(toolbar)

        # 中心部件
        grid1 = QGridLayout()
        
        # 显示文件夹结构
        dirmodel = QFileSystemModel()
        try:
            print(self.dir_path)
        except AttributeError:
            self.dir_path = QDir.rootPath()
            print('请首先打开项目文件夹')
        dirmodel.setRootPath(self.dir_path)
        dirmodel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
        self.tv = QTreeView()
        self.tv.setModel(dirmodel)
        self.tv.setRootIndex(dirmodel.index(self.dir_path))

        # 显示文件列表
        filemodel = QFileSystemModel()
        filemodel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)
        lv = QListView()
        lv.setModel(filemodel)
        lv.setRootIndex(filemodel.index(self.dir_path))

        gv = QGraphicsView()
        grid1.addWidget(self.tv, 0, 0, 15, 5)
        grid1.addWidget(lv, 15, 0, 5, 5)
        grid1.addWidget(gv, 0, 5, 15, 20)

        grid2 = QGridLayout()

        cbn = QComboBox()
        grid2.addWidget(cbn, 0, 0, 1, 2)

        pbn1 = QPushButton('pre frame')
        pbn1.setShortcut(QKeySequence('p'))
        pbn1.clicked.connect(self.test)
        grid2.addWidget(pbn1, 0, 2)

        pbn2 = QPushButton('next frame')
        pbn2.setShortcut(QKeySequence('n'))
        pbn2.clicked.connect(self.test)
        grid2.addWidget(pbn2, 0, 3)

        pbn3 = QPushButton('pre 10 frame')
        pbn3.setShortcut(QKeySequence('ctrl+p'))
        pbn3.clicked.connect(self.test)
        grid2.addWidget(pbn3, 1, 2)

        pbn4 = QPushButton('next 10 frame')
        pbn4.setShortcut(QKeySequence('ctrl+n'))
        pbn4.clicked.connect(self.test)
        grid2.addWidget(pbn4, 1, 3)

        grid1.addLayout(grid2, 15, 5, 5, 20)

        center_widget = QWidget()
        center_widget.setLayout(grid1)
        self.setCentralWidget(center_widget)

        # 状态栏
        statubar = QStatusBar()
        statubar.showMessage('please open a project')
        self.setStatusBar(statubar)

class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        hlay = QHBoxLayout(self)
        self.treeview = QTreeView()
        self.listview = QListView()
        hlay.addWidget(self.treeview)
        hlay.addWidget(self.listview)

        # path = QDir.rootPath()
        path = QFileDialog.getExistingDirectory(self, '', './')

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.filemodel = QFileSystemModel()
        self.filemodel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.filemodel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.filemodel.index(path))

        self.treeview.clicked.connect(self.on_clicked)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.filemodel.setRootPath(path))

# class DemoIcon(QWidget):
#     def __init__(self):
#         super(DemoIcon, self).__init__()
#         self.initUI()

#     def initUI(self):
#         layout = QGridLayout()
#         line_count = 16
#         index = 0

#         for key in dir(QStyle):
#             value = getattr(QStyle, key)
#             if isinstance(value, QStyle.StandardPixmap):
#                 if key != 'SP_CustomBase' and value < 71:
#                     print(key, value)
#                     btn = QToolButton()
#                     btn.setFixedSize(32, 32)
#                     btn.setIcon(QApplication.style().standardIcon(value))
#                     btn.setToolTip(f'{key}, {value}')
#                     layout.addWidget(btn, index//line_count,
#                                      index % line_count)
#                     index += 1
#         self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    # win = Widget()
    win.show()
    sys.exit(app.exec_())
