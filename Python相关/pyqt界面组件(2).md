[TOC]

# 文本图像标签

用于显示文本或者图像，可以使用以下方法设置其内容：

setText()  # 传递字符串

setText()  # 传递富文本

setPixmap(QPixmap())  # 图像

setNum(int/double)  # 数字

```python
class Example(QWidget):

    def initUI(self):

        pix = QPixmap('nosexy.jpg')

        lbp = QLabel(self)
        lbp.setGeometry(0,0,300,200)
        lbp.setStyleSheet("border: 2px solid red")
        lbp.setPixmap(pix)

        lbq = QLabel(self)
        lbq.setGeometry(0,250,300,200)
        lbq.setPixmap(pix)
        lbq.setStyleSheet("border: 2px solid red")
        lbq.setScaledContents(True)  # 图像会自动拉伸填充该部件s   
        
        self.lb1 = QLabel('学点编程吧，我爱你~！',self)
        self.lb2 = QLabel('我内容很少哦...',self)
        self.lb3 = QLabel('我内容很少哦...',self)
        self.lb3.setWordWrap(True)  # 设置自动换行

        self.bt1 = QPushButton('输入内容1',self)
        self.bt2 = QPushButton('输入内容2',self)


        self.ra1 = QRadioButton('左边',self)
        self.ra2 = QRadioButton('中间',self)
        self.ra3 = QRadioButton('右边',self)

        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.ra1, 1)
        self.bg1.addButton(self.ra2, 2)
        self.bg1.addButton(self.ra3, 3)

        self.show()

        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)

    def rbclicked(self):
        if self.bg1.checkedId() == 1:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 竖直居中， 水平左对齐
        elif self.bg1.checkedId() == 2:
            self.lb1.setAlignment(Qt.AlignCenter)  # 水平居中
        elif self.bg1.checkedId() == 3:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignRight)  # 竖直居中，水平右对齐
    
    def showDialog(self):
        sender = self.sender()
            if sender == self.bt1:
                text, ok = QInputDialog.getText(self, '内容1', '请输入内容1：')
                if ok:
                    self.lb2.setText(text)
            elif sender == self.bt2:
                text, ok = QInputDialog.getText(self, '内容2', '请输入内容2：')
                if ok:
                    self.lb3.setText(str(text))
```

# 工具箱

```python
class Example(QToolBox):

    def initUI(self):
        self.resize(280,500)
        self.setWindowTitle('微信公众号：学点编程吧--QToolBox')
        self.setWindowFlags(Qt.Dialog)

        favorites =[
                        [
                            {'des':'百度搜索', 'pic':'image/se/baidu.ico'},
                            {'des':'搜狗搜索', 'pic':'image/se/sougo.ico'},
                            {'des':'必应搜索', 'pic':'image/se/bing.ico'},
                            {'des':'360搜索', 'pic':'image/se/360.ico'},
                            {'des':'谷歌搜索', 'pic':'image/se/google.ico'},
                            {'des':'雅虎搜索', 'pic':'image/se/yahoo.ico'}
                        ],
                        [
                            {'des':'腾讯视频', 'pic':'image/v/tengxun.ico'},
                            {'des':'搜狐视频', 'pic':'image/v/sohuvideo.ico'},
                            {'des':'优酷视频', 'pic':'image/v/youku.ico'},
                            {'des':'土豆视频', 'pic':'image/v/tudou.ico'},
                            {'des':'AcFun弹幕', 'pic':'image/v/acfun.ico'},
                            {'des':'哔哩哔哩', 'pic':'image/v/bilibili.ico'}
                        ]
        ]
        for item in favorites:
            groupbox = QGroupBox()  # 每一个大类作为一个选项卡
            vlayout = QVBoxLayout(groupbox)
            vlayout.setAlignment(Qt.AlignCenter) 
            for category in item:
                toolButton = QToolButton()
                toolButton.setText(category['des'])
                toolButton.setIcon(QIcon(category['pic']))
                toolButton.setIconSize(QSize(64, 64))
                toolButton.setAutoRaise(True)
                toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                vlayout.addWidget(toolButton)
                name = category['des']  
                toolButton.clicked.connect(run)
			if name == '雅虎搜索':
				self.addItem(groupbox,'搜索引擎')
			else:
				self.addItem(groupbox,'视频网站')
    def run(self):
        if self.sender().text() == '百度搜索':
            webbrowser.open('https://www.baidu.com')
        elif self.sender().text() == '搜狗搜索':
            webbrowser.open('https://www.sogou.com/')
        #...下面的代码和上面差不多，不再描述
```

# QListView

# QListWidget

# QTreeWidget

# QTableWidget

