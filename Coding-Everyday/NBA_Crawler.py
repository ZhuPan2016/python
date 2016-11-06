import urllib.request
import re
import numpy as np
url = 'http://nba.sports.sina.com.cn/match_result.php'
import pandas as pd


def getHtml(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('gb2312')
    return html
def getHead(html):
    pattern1 = re.compile('<tr bgcolor=#FFD200 align="center">(.*?)</tr>',re.S)
    head = re.findall(pattern1,html)
    headd = str(head[0])
    pattern2= re.compile('>(.*?)<',re.S)
    head2 = re.findall(pattern2, headd)
    head=[]
    head.append(head2[0])
    head.append(head2[2])
    head.append(head2[4])
    head.append(head2[6])
    head.append(head2[8])
    return head
def getData(html,n):
    pattern = re.compile('<tr bgcolor="#FFEFB6" (.*?)</tr>',re.S)
    data = re.findall(pattern,html)
    data = str(data[n])
    pattern2 = re.compile('>(.*?)<')
    dataa = re.findall(pattern2,data)
    data = []
    data.append(dataa[0])
    data.append(dataa[1])
    data.append(dataa[2])
    data.append(dataa[5])
    data.append(dataa[7])
    return data
html = getHtml(url)
head = getHead(html)
data = []
for i in range(10):
    dataa = getData(html,i)
    data.append(dataa)

frame = pd.DataFrame(data,columns=head)
print(frame)
