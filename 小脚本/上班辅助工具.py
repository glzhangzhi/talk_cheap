'''
这是一个用来辅助上班的工具

预计功能：

1. 一键上下班打卡
2. 显示下班倒计时（可自定义上班时长，显示多余时长）
3. 显示本

'''

from time import sleep
import time
import sys
import datetime
from selenium import webdriver
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout

def clockin():
    driver = webdriver.Chrome(r'C:\Users\glzha\Desktop\Git\小脚本\chromedriver.exe')
    driver.get('http://timeterminal/')
    name = driver.find_element_by_id("Ident1")
    name.send_keys('Zhang')
    sleep(1)
    password = driver.find_element_by_id("Ident2")
    password.send_keys('7500478')
    sleep(1)
    coming = driver.find_element_by_id('C1')
    coming.click()
    print('已打卡登录')

def clockout():
    driver = webdriver.Chrome(r'C:\Users\glzha\Desktop\Git\小脚本\chromedriver.exe')
    driver.get('http://timeterminal/')
    name = driver.find_element_by_id("Ident1")
    name.send_keys('Zhang')
    sleep(1)
    password = driver.find_element_by_id("Ident2")
    password.send_keys('7500478')
    sleep(1)
    going = driver.find_element_by_id('C2')
    going.click()
    print('已打卡下班')

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)

        self.sp = QSpinBox(self)
        self.sp.setRange(1, 8)
        self.sp.setSingleStep(1)
        self.sp.setValue(8)
        self.sp.valueChanged.connect(self.changeLbText)
        
        self.bt1 = QPushButton('上班', self)
        # self.bt1.clicked.connect(clockin())
        
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.sp)
        hbox1.addWidget(self.bt1)
        hbox1.addStretch(1)

        self.lb1 = QLabel(self)
        self.lb1.setText(f"预计下班时间：{(datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%H:%M')}")
        self.lb2 = QLabel(self)
        self.lb2.setText(f'剩余：{540} min')

        self.bt2 = QPushButton('下班', self)
        # self.bt2.clicked.connect(clockout())

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.lb1)
        vbox.addWidget(self.lb2)
        vbox.addWidget(self.bt2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.show()

    def changeLbText(self, value):
        if value == 8:
            value = 9
        else:
            value = 4  
        self.lb2.setText(f'剩余：{value * 60} min')
        self.lb1.setText(f"预计下班时间：{(datetime.datetime.now() + datetime.timedelta(hours=value)).strftime('%H:%M')}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())