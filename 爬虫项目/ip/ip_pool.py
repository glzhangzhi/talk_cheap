# -*- coding: utf-8 -*-

import multiprocessing
from os import listdir
from pickle import dump, load
from random import choice
from re import compile
from sqlite3 import connect
from time import sleep

from lxml import etree
from requests import get

lock = multiprocessing.Lock()


def GetHTMLContent(url, use_proxy=True):  # return
    '''
    通过requests库获取网页，随机选择浏览器头，可选代理ip

    返回网页相应

    '''
    USER_AGENT_LIST = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
    headers = {'User-agent': choice(USER_AGENT_LIST)}
    if use_proxy:
        con = connect('./test.db')
        cur = con.cursor()
        rows = cur.execute("select type,ip from user").fetchall()
        cur.close()
        con.close()
        row = choice(rows)
        proxies = {row[0]:row[1]}
        r = get(url, headers=headers, proxies=proxies)
    else:
        r = get(url, headers=headers)
    r.encoding = 'UTF-8'
    return r


def ip_from_proxylist():
    print('正在从proxylist中获取代理地址')
    url = 'http://proxylist.fatezero.org/proxy.list'
    r = GetHTMLContent(url,False)
    lines = r.text.split('\n')
    con = connect('./test.db')
    cur = con.cursor()
    count = 0
    for line in lines:
        try:
            host = compile(r'"host": "(\d*.\d*.\d*.\d*)"').findall(line)[0]
            ty = compile(r'"type": "(https?)"').findall(line)[0].lower()
            cur.execute('insert into user values(?, ?, ?, ?);', (ty, host, True, 1.0))
            count += 1
        except:
            pass
    con.commit()
    cur.close()
    con.close()
    print(f'爬取完成，共获取{count}个代理地址')


def ip_from_ip3366():
    print('正在从ip3366中获取代理地址')
    con = connect('./test.db')
    cur = con.cursor()
    count = 0
    for i in range(1, 8):
        url = 'http://www.ip3366.net/free/?stype=1&page=' + str(i)
        r = GetHTMLContent(url, False)
        sleep(0.1)
        html = etree.HTML(r.text)
        ip = html.xpath('//*[@id="list"]/table/tbody/tr/td[1]')
        ty = html.xpath('//*[@id="list"]/table/tbody/tr/td[4]')
        for i in range(len(ip)):
            cur.execute('insert into user values(?, ?, ?, ?);', (ty[i].text.lower(), ip[i].text, True, 1.0))
            count += 1
    con.commit()
    cur.close()
    con.close()
    print(f'爬取完成，共获取{count}个代理地址')

def initsql():
    conn = connect('./test.db')
    cursor = conn.cursor()
    cursor.execute('''create table user (type varchar(5),
										 ip varchar(20),
										 connect boolean,
										 time real,
										 ftime int
	)''')
    cursor.close()
    conn.commit()
    conn.close()


def clear():
    print('正在清理连接不成功的代理')
    con = connect('./test.db')
    cur = con.cursor()
    cur.execute("select * from user where connect=False")
    rows = cur.fetchall()
    count = len(rows)
    cur.execute("delete from user where connect=False")
    con.commit()
    print(f'清理完成，共清除{count}个代理地址')



def test():
    url = 'https://www.baidu.com'
    con = connect('./test.db')
    cur = con.cursor()
    cur.execute("select type, ip from user")
    rows = cur.fetchall()
    cur.execute("select type from user")
    ty = cur.fetchall()
    cur.execute("select ip from user")
    ip = cur.fetchall()
    cur.close()
    con.close()
    pool = multiprocessing.Pool(processes=3)
    pool.map(testip, rows)


def testip(row):
    global lock
    url = 'https://www.baidu.com'
    headers = {
        'User-agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
    proxies = {row[0]: row[1]}
    try:
        r = get(url, headers=headers, proxies=proxies, timeout=0.5)
        time = r.elapsed.total_seconds()
        lock.acquire()
        con = connect('./test.db')
        cur = con.cursor()
        cur.execute(
            "update user set connect=True where type=? and ip=?", (row[0], row[1]))
        cur.execute("update user set time=? where type=? and ip=?",
                    (time, row[0], row[1]))
        con.commit()
        cur.close()
        con.close()
        print('连接成功')
        lock.release()
    except:
        lock.acquire()
        con = connect('./test.db')
        cur = con.cursor()
        cur.execute(
            "update user set connect=False where type=? and ip=?", (row[0], row[1]))
        con.commit()
        cur.close()
        con.close()
        print('连接失败')
        lock.release()


def show():
    con = connect('./test.db')
    cur = con.cursor()
    cur.execute("select * from user")
    rows = cur.fetchall()
    cur.close()
    con.close()
    n = len(rows)
    return n
    # print(f'目前库内共有可用的ip{n}条')


def run():
    print('功能列表:\n')
    a = 0
    while a != 99:
        a = int(input('''
    代理池程序
    1. 从proxylist中获取代理地址
    2. 从ip3366中获取代理地址
    3. 测试现有代理池连通性
    4. 清除不可用的代理
    5. 显示目前代理库容量
    
    99.退出
        '''))
        if a == 1:
            ip_from_proxylist()
        elif a == 2:
            ip_from_ip3366()
        elif a == 3:
            test()
        elif a == 4:
            clear()
        elif a == 5:
            n = show()
            print(f'目前库内共有可用的ip{n}条')
        elif a == 99:
            break


if __name__ == '__main__':
    run()
