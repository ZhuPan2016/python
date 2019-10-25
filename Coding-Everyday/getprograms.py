import urllib.request
import re

user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}

def get_html(url):
    response = urllib.request.Request(url, headers=headers)
    response1 = urllib.request.urlopen(response)
    html = response1.read().decode('utf-8')
    return html

def get_title_and_code(html):
    videoTitle_pattern = re.compile('"videoTitle":"(.*?)"',re.S)
    videoSharedCode_pattern = re.compile('"videoSharedCode":"(.*?)"',re.S)
    videoTitles = re.findall(videoTitle_pattern,html)
    videoSharedCodes = re.findall(videoSharedCode_pattern,html)
    return videoTitles, videoSharedCodes

def get_title_and_code2(html):
    videoTitle_pattern = re.compile('"title":"(.*?)"',re.S)
    videoSharedCodeUrl_pattern = re.compile('"img":"(.*?)",',re.S)
    videoTitles = re.findall(videoTitle_pattern,html)
    videoSharedCodeUrls = re.findall(videoSharedCodeUrl_pattern,html)
    videoSharedCodes = []
    for codeUrl in videoSharedCodeUrls:
        videoSharedCodes.append((codeUrl.split('/')[-1])[:32])
    return videoTitles, videoSharedCodes
# "http://api.cntv.cn/lanmu/videolistByColumnId?id=TOPC1451557893544236&n=30&of=fdate&p=2&type=0&serviceId=tvcctv&cb=Callback"探索发现
# "videoTitle":"《探索发现》 20190615 考古晋国——崛起之谜（二）"
# "videoSharedCode":"581e99d564eb4627a08dd8e5ebed3f7d"
'''
#EXTINF:-1 group-title="探索发现",20190615 考古晋国——崛起之谜（二）
http://asp.cntv.lxdns.com/asp/hls/850/0303000a/3/default/de518d52f59745b1a8226406faa50678/850.m3u8
'''

def zhuaqu():
    f = open("./text1018.txt",'w')
    url = "http://tv.cctv.com/2017/05/25/VIDA9lyN9LEHc2BVPzBmYF2E170525.shtml"
    html = get_html(url)
    titles,codes = get_title_and_code2(html)
    for count,title in enumerate(titles):
        f.write('#EXTINF:-1 group-title="xxx",%s'%(title))
        f.write('\n')
        f.write("http://asp.cntv.lxdns.com/asp/hls/850/0303000a/3/default/%s/850.m3u8"%(codes[count]))
        f.write('\n')
if __name__ == "__main__":
    zhuaqu()


    
