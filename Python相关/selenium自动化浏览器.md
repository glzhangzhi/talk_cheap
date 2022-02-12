[TOC]

# 安装
`pip install selenium`
还需要下载对应浏览器的驱动器
[Chrome](https://sites.google.com/chromium.org/driver/downloads) [IE](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

在创建driver对象时，将驱动器的位置给出，如

```python
driver = webdriver.Chrome(r"C:\Users\glzha\Download\chromedriver.exe")
```

# Hello World

先来一个简单例子，打开python官网，在搜索框里输入pycon并搜索
```python
from selenium import webdriver #导入基本模块
from selenium.webdriver.common.keys import Keys #导入模拟键盘操作模块
driver = webdriver.Chrome() #创建chrome浏览器
driver.get("http://www.python.org") #打开网址直到完全加载
assert "Python" in driver.title #确认打开网页的标题中含有python字样
elem = driver.find_element_by_name("q") #使用标签名q定位元素
elem.clear() #清除搜索框内的提示文字
elem.send_keys("pycon") #输入搜索关键词
elem.send_keys(Keys.RETURN) #按回车键
assert "No results found." not in driver.page_source #声明该字段不在页面源码中
driver.close() #关闭浏览器
```

# 导航至链接
最普通的链接方式为
```python
driver.get('http://www.ggogle.com')
driver.refresh() #刷新网页
```
浏览器会等待直至页面完全加载，但如果页面中使用了大量的AJAX元素，则不会完全加载，因为浏览器无法判断这些元素的加载情况，文档中说可以使用wait来等待页面元素的完全加载。

# 查找元素
```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```
但要注意，当使用文本匹配某个链接时，一定要精确匹配，除此之外，当使用Xpath进行匹配时，如果存在多个匹配项，只会返回第一个，如果找不到匹配项，会引发一个NoSuchElementException错误。
常用元素交互
```python
element.send_keys('some text') #在文本框中输入文本
element.send_keys(Keys.ARROW_DOWN) #模拟按下键盘的下箭头键
element.clear() #清除文本框中已存在的文字
```
# 输入文本和模拟按键

模块中selenium.webdriver.common.keys中保存了很多键盘按键

```python
from selenium.webdriver.common.keys import Keys

element.send_keys('some text')
element.send_keys('and some', Keys.ARROW_DOWN)

# 一些常用按键
# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT 箭头键
# Keys.ENTER 回车
# Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP 页首，页尾，下一页，上一页
# Keys.F1, Keys.F2, Keys.F12 功能键
# Keys.TAB Tab键
```

注意实现按键是通过某一个元素，而不是浏览器实例，一般推荐是页面最顶层的<html>标签中应用按键。

# 复选框/标签操作

```python
element = driver.find_element_by_xpath('//select[@name='name']') #找到复选项表单
all_options = element.find_element_by_tag_name('option') #返回所有选项List
for option in all_options:
    print('value is: %s' % option.get_attribute('value')) #循环打印所有选项值
    option.click() #并点击该选项
from selenium.webdriver.support.ui import Select #导入UI操作选择
select = Select(driver.find_element_by_name('name')) #创建复选项对象
select.select_by_index(index) #通过索引选择
select.select_by_visible_text("text") #通过文本选择
select.select_by_value(value) #通过值选择
select = Select(driver.find_element_by_id('id'))
select.deselect_all() #全部取消选择
select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options #返回所有已选选项
options = select.options #返回所有可选选项
driver.find_element_by_id("submit").click() #找到提交按钮并点击
element.submit() #直接提交
```

# cookie相关操作
```python
driver.get("http://www.example.com")
cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
driver.add_cookie(cookie) #向当前网页添加cookie
driver.get_cookies() #返回当前网页cookie
```

# 定位元素
## 单个元素
存在多个元素时会返回找到的第一个元素
```python
find_element_by_id #用于已知标签的id属性
find_element_by_name #用于已知标签的name属性
find_element_by_xpath #关于XPath的用法见我之前的博客
find_element_by_link_text #用标签文本来定位
find_element_by_partial_link_text #用部分标签文本来定位
find_element_by_tag_name #用Tag名字来定位，如body,h1,p等
find_element_by_class_name #用class属性定位
find_element_by_css_selector #感觉应该类似于XPath的语法体系，目前没有研究
```
## 多个元素
返回多个结果，形成一个List
```
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
```

# 获取标签的属性和内容
```python
elem = driver.find_element_by_xpath('.....')
attr = elem.get_attribute('attribute_name')
content = elem.text
```

# Wait指令

用于应对现在网页上应用越来越多的AJAX技术，可以使某个操作等待一定时间或是等待某个条件满足以后再执行

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    ) #等待十秒，默认每500毫秒检测一次条件，直到页面上出现id为XXX的元素
finally:
    driver.quit()
```
以下是一些常用的条件
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
也可以自己定义自己的等待条件
```python
class element_has_css_class(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False

# Wait until an element with id='myNewInput' has class 'myCSSClass'
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
```
另外就是单纯的等待一定时间
```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```

# 附录

今天看[huilan_same大神的博客文章](https://blog.csdn.net/huilan_same/article/details/52544521)，了解到其实这个等待一共分三种，强制等待，隐性等待和显性等待，使用sleep()就是强制等待，而上文的使用implicity_wait()就是隐性等待，指执行任何加载操作后，都会等待页面全部加载完毕再执行其他动作，这个指令是真对driver而言的，一个driver只用设置一次即可。而使用条件判断的就是显性等待。