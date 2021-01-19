import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        # 判断标签tr是否为类型
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].text.strip(),tds[1].text.strip(),tds[2].text.strip(),tds[3].text.strip(),tds[4].text.strip()])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{5}^10}\t{2:{5}^10}\t{3:{5}^10}\t{4:^10}"
    print(tplt.format('排名','学校名称','省市','类型','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))

def main():
    uinfo = []
    url = "http://www.shanghairanking.cn/rankings/bcur/2020"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
main()












