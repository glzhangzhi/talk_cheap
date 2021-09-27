
# 主要功能
```python
import time #主要用到time库，这个python自带的库
t0 = time.time() #获取当前时间戳
t1 = time.localtime(time.time()) #获取当前时间
t2 = time.asctime(time.localtime(time.time())) #直接获取可读格式的时间
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#自定义时间格式输出
#年-月-日 时-分-秒
time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 星期简称 月份简称 日 时:分:秒 年
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")) 将某个日期转化为时间戳
cal = calendar.month(2016, 1) 获取某月月历
```

# 时间格式符
代码 | 含义
---- | -----
%a | 本地简化星期名称
%A | 本地完整星期名称
%b  | 本地简化的月份名称
%B  | 本地完整的月份名称
%c  | 本地相应的日期表示和时间表示
%d |  月内中的一天（0-31）
%H |  24小时制小时数（0-23）
%I |  12小时制小时数（01-12）
%j  | 年内的一天（001-366）
%m  | 月份（01-12）
%M  | 分钟数（00=59）
%p  | 本地A.M.或P.M.的等价符
%S  | 秒（00-59）
%U  | 一年中的星期数（00-53）星期天为星期的开始
%w |  星期（0-6），星期天为星期的开始
%W |  一年中的星期数（00-53）星期一为星期的开始
%x  | 本地相应的日期表示
%X |  本地相应的时间表示
%y  | 两位数的年份表示（00-99）
%Y |  四位数的年份表示（000-9999）
%Z  | 当前时区的名称
%% |  %号本身

# 其他time库中的函数

```python
time.altzome #返回格林威治西部的夏令时地区的偏移秒数
time.asctime([tupletime]) #将时间元组转换为一个可读形式
time.clock() #用以浮点数计算的秒数返回当前的CPU时间
time.ctime([secs]) #作用相当于asctime(localtime(secs))，未给参数相当于asctime()
time.gmtime([secs]) #接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t
time.localtime([secs])
#接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）
time.mktime(tupletime) #接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）
time.sleep(secs) #推迟调用线程的运行，secs指秒数
time.strftime(fmt, tupletime) #接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定
time.strptime(str, fmt) #根据fmt的格式把一个时间字符串解析为时间元组
time.time() #返回当前时间的时间戳（1970纪元后经过的浮点秒数
time.tzset() #根据环境变量TZ重新初始化时间相关设置
time.timezome #当地时区（未启动夏令时）距离格林威治的偏移秒数
time.tzname #包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的
```

# 日历相关函数

```python
calendar.calendar(year, w=2, l=1, c=6) #返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数
calendar.firstweekday() #返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一
calendar.isleep(year) #是闰年返回 True，否则为 False
calendar.leapdays(y1, y2) #返回在Y1，Y2两年之间的闰年总数
calendar.month(year,month,w=2,l=1) #返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数
calendar.monthcalendar(year,month) #返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始
calendar.monthrange(year,month) #返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12
calendar.prcal(year,w=2,l=1,c=6) #相当于 print calendar.calendar(year,w,l,c)
calendar.prmonth(year,month,w=2,l=1) #相当于 print calendar.calendar（year，w，l，c） 
calendar.setfirstweekday(weekday) #设置每周的起始日期码。0（星期一）到6（星期日）
calendar.timegm(tupletime) #和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）
calendar.weekday(year,month,day) #返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
```

# 时间日期的比较
各种方法对比下来，比较简单且符合我需求的就是将时间的字符串形式转化为时间戳，然后比较两个时间戳的大小，因为时间戳是表示1970年1月1号到该时间的秒数，所以任何日期之间的相对大小都可以确定

```python
time1 = '2017-04-17'
time2 = '2017-04-19'
s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
e_time = time.mktime(time.strptime(time2,'%Y-%m-%d'))
print( 's_time is:',s_time )
print( 'e_time is:',e_time )
result = int(s_time) - int(e_time)
%Y年 #%m月%d日%H时%M分%S秒
```
但是在实际过程中发现一个小问题，就是如果按照我的需求，只对比小时和分钟这两个数值，传入的值是07：24这样，那么它会默认缺省的年份为1900年，但是`time.mktime`只能接收1970年以后的时间元组数据，就会报参数超出范围的错误，所以现在解决办法有两个，第一，把获取的本地时间的年月日信息传给日出时间，组成当地完整的时间元组，第二，把时间形成字符串，直接比较字符串大小。

时间戳中各个参数为
```
tm_year 年
tm_mon 月
tm_mday 日
tm_hour 小时
tm_min 分钟
tm_sec 秒
tm_wday 星期
tm_yday 一年中第几天
tm_isdst 是否是夏令时
```
本来打算直接读取这些属性然后赋值给另一个时间元组就好，结果这些属性都是只读的，所以如果采用第一个办法的话，还要再绕一圈，把这些时间元组的属性读出来，形成字符串，组成新的时间元组，再转化成时间戳
```python
r = GetTheHTML()
t1 = GetRiseTime(r)[0].text #得到日出时间，格式为HH:MM
t2 = time.localtime() #得到本地时间的时间元组
t3 = time.mktime(t2) #将时间元组转化为时间戳，方便比较
Y = t2.tm_year
M = t2.tm_mon
D = t2.tm_mday #将日出时间构造成本地时间的年月日
t1 = time.mktime(time.strptime(str(Y) + '-' + str(M) + '-' + str(D) + ' ' + t1,'%Y-%m-%d %H:%M')) 
#将构造好的日出时间元组的字符串转化为时间元组，再转化为时间戳
t1 > t3
```
最后代码如上,如此可以做到将日出时间和现在当地时间进行比较