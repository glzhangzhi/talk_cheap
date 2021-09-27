from lxml import etree
import requests
import os
from zhconv import convert

def GetHTMLContent(url): #return r
	headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
	r = requests.get(url, headers = headers)
	r.raise_for_status()
	r.encoding = 'UTF-8'
	return r


def get_the_url(name, url):
	r = GetHTMLContent(url)
	html = etree.HTML(r.text)
	Urls = html.xpath('/html/body/div[3]/div[1]/ul[3]/li/a/@href')
	new_Urls = []
	for url in Urls[1:]:
		new_Urls.append('https:' + url)
	cap = 1
	for url in new_Urls:
		r = GetHTMLContent(url)
		html = etree.HTML(r.text)
		contents = html.xpath('//*[@id="sticky-parent"]/div[2]/div[4]/text()')
		new_contents = []
		for i in contents:
			if i == '\r\n':
				continue
			else:
				new_contents.append(i.replace('\r\n\u3000\u3000', ''))
		alle = ''
		for i in new_contents[1:]:
			alle += i
		
			with open(name + '/' + str(cap) + '.txt', 'w') as f:
				try:
					f.write(alle)
				except:
					f.write('error')
		cap += 1
	return cap - 1

def f2j(cap, name):
	for idx in range(1, cap + 1):
		try:
			with open(name + '/' + str(idx) + '.txt', 'r') as f:
				content = f.read()
			j = convert(content, 'zh-cn')
			with open(name + '/' + 'j_' + str(idx) + '.txt', 'w') as f:
				f.write(j)
		except:
			with open(name + '/' + 'j_' + str(idx) + '.txt', 'w') as f:
				f.write('error')

def zhenghe(cap, name):
	whole = ''
	for i in range(1, cap + 1):
		with open(name + '/' + 'j_' + str(i) + '.txt', 'r') as f:
			whole = whole + str(i) + '\n' + f.read() + '\n\n'
	with open(name + '/' + name + '.txt', 'w') as f:
		f.write(whole)

def main():
	names = ['穿進肉文被操翻了怎麼辦']
	urls = ['https://czbooks.net/n/cpgg3m8']
	data = zip(names, urls)
	for name, url in data:
		try:
			os.mkdir(name)
			cap = get_the_url(name, url)
			f2j(cap, name)
			zhenghe(cap, name)
			print(f'{name}已下载完毕')
		except:
			print(f'正在下载{name}时出错，已跳过，开始下载下一部小说')
			continue

if __name__ == '__main__':
	main()