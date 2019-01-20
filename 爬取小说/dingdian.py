# 爬取顶点小说
# maxzjs
# 2019.1.13
# -*- coding:utf-8 -*-
import requests,sys
from lxml import etree
import threading
sys.setrecursionlimit(100000)


class Spider(object):
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.offset = 1

    def start_work(self, url):
        print("正在爬取第%d页。。。" % self.offset)
        self.offset += 1
        respone = requests.get(url=url, headers=self.headers)
        result = respone.content.decode()
        html = etree.HTML(result)

        txt_title = html.xpath('//td[@class="L"]/a/text()')[::2]
        txt_src = html.xpath('//td[@class="L"]/a/@href')[1::2]
        next_page ="".join(html.xpath('//a[@class="next"]/@href'))

        self.content_work(txt_src,txt_title)
        self.start_work(next_page)

    def content_work(self, txt_src, txt_title):
        for i,j in zip(txt_src,txt_title):
            req = requests.get(url=i,headers=self.headers)
            reqs = req.content.decode()
            req_html = etree.HTML(reqs)
            req_src = req_html.xpath('//td[@class="L"]/a/@href')[0]
            self.write_file(req_src, j)


    def write_file(self, last_src, txt_title):
        respone = requests.get(url=last_src, headers=self.headers)
        re_html = etree.HTML(respone.content.decode())
        re_title = re_html.xpath('//h1/text()')
        re_con = re_html.xpath('//dd[@id="contents"]/text()')
        re_next = re_html.xpath('//h3/a/@href')[2].encode().decode()
        re_next_http = "https://www.23us.so/" + re_next
        if re_next[-10] != "index.html":
            file_name = txt_title + ".txt"
            file_name = "".join(file_name.split("/"))
            print("正在爬取小说：%s %s" % (file_name, re_title))
            for i in re_con:
                re_cont = i.encode().decode().replace("\r\n","")
                re_conte = re_cont.replace("\r","")
                with open(file_name, "a", encoding='utf-8') as f:
                   f.write(re_conte)
            self.write_file(re_next_http,txt_title)

if __name__ == "__main__":

    spider = Spider()
    for i in range(0,73):
        t = threading.Thread(target=spider.start_work("https://www.23us.so/modules/article/articlelist.php?fullflag=1&page=" + str(i)))
        t.start()