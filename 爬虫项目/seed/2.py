import requests
from lxml import etree
from time import sleep
# from openpyxl import load_workbook 

def GetHTMLContent(url): 
	headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
	cookies = {'existmag':'all'}
	r = requests.get(url, headers = headers, cookies = cookies)
	r.raise_for_status()
	r.encoding = 'UTF-8'
	return r

def main():
	url = 'https://www.javbus.com/star/okq/'
	# url = 'https://www.javbus.com/star/2jv/'	
	number = 4  #这里遇到的问题是，到某些页数，即使能直接访问，也提示找不到网页
	for i in range(number):
		url2 = url + str(i+1)
		r = GetHTMLContent(url2)
		html = etree.HTML(r.text)
		m = len(html.xpath('//div[@id="waterfall"]/div[@id="waterfall"]/div'))
		for j in range(m):
			name = html.xpath('//*[@id="waterfall"]/div[' + str(j+1) + ']/a/div[2]/span/text()')[0]
			index = html.xpath('//*[@id="waterfall"]/div[' + str(j+1) + ']/a/div[2]/span/date[1]')[0].text
			date = html.xpath('//*[@id="waterfall"]/div[' + str(j+1) + ']/a/div[2]/span/date[2]')[0].text
			urls = html.xpath('//*[@id="waterfall"]/div[' + str(j+1) + ']/a/@href')[0]
			# print(index, date, urls)
main()
