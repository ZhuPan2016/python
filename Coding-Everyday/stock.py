'''听说国内险资在A股市场动作频频，一个个查询必然非常费时间，
于是使用爬虫从雪球网爬取了一部分险资调研的股票信息，
主要涉及股票名称代码、收盘价、涨跌幅
主要运用的知识无非是正则表达式、urllib.request库
文件操作.由于正则表达式不熟练，只能多次匹配，有待改正.'''
import urllib.request
import re
import xlwt
import time
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
import xlrd
data = xlrd.open_workbook('G:\\1.xls')
table = data.sheets()[0]
a = table.col_values(2)
def getHtml(url):
    response = urllib.request.Request(url, headers=headers)
    response1 = urllib.request.urlopen(response)
    html = response1.read().decode('utf-8')
    return html
def getStock(html):
    pattern_price = re.compile('<strong data-current="(.*?)"', re.S)
    pattern_name = re.compile('" class="stockName">(.*?)</strong>', re.S)
    pattern_quote = re.compile('<span class="quote-percentage">(.*?)</span>', re.S)
    pattern_sign = re.compile('<span>(.*?)</span><span class="quote-percentage">')
    price = re.findall(pattern_price, html)
    name = re.findall(pattern_name, html)
    quote = str(re.findall(pattern_quote, html))
    pattern_quote2 = re.compile('[0-9]+', re.S)
    sign = re.findall(pattern_sign, html)
    quote = re.findall(pattern_quote2, quote)
    if float(sign[0])>0:
        quote = str(int(quote[0])+0.01*int(quote[1]))+'%'
    else:
        quote = '-'+str(int(quote[0])+0.01*int(quote[1]))+'%'
    return (name, price, quote)
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet(str(time.strftime('%Y-%m-%d',time.localtime(time.time()))),cell_overwrite_ok=True)
count_head = -1
count = 0
head = ['AnBang', 'BaoNeng', 'HengDa']
for i in a:
    if i == '':
        sheet.write(count_head+1, 0, head[count])
        count = count + 1
    if i !='':
        b=count_head +1
        html = getHtml(str(i))
        (name, price, quote) = getStock(html)
        sheet.write(count_head+1,1,name)
        sheet.write(b,2,price)
        sheet.write(b,3,quote)
        count_head = count_head+1
date = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
name = 'G:'+'\\'+date+'.xls'
book.save(name)
