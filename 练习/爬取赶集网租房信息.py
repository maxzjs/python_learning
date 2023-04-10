# -*- coding:utf-8 -*- 
try:
    from bs4 import BeautifulSoup
    import requests,os
except Exception  :
    print("请安装 bs4库 和 requests库 再来运行")
    exit(0)
 
 
#获取当前价位的累计
def settle_add_num(soup_find_all,money):
    index=0
    for tag in soup_find_all:
        if tag.contents[0].isnumeric():
            money = money + int(tag.contents[0])
            index+=1
    return money
#获取当前平方的累计
def settle_add_m2(soup_find_all,m2):
    index = 0
    for tag in soup_find_all:
        m2 = m2 + int(tag['data-area'].replace('㎡', ''))
        index += 1
    return m2
 
#详细信息
def settle_moneysize_data(soup_find_all):
    url ="http://baoding.ganji.com{0}"
    with open(r'H:/zufang.txt','r+') as file:
        for tag in soup_find_all:
            print(tag.text.split()) #标题
            file.wirte(tag.text.split() + '\n')
            newurl=url.format(tag.a["href"])
            soup = BeautifulSoup(requests.get(newurl).text, "html.parser")
     
            for a in soup.find_all('div', class_='f-group'):#,id ="js-house-describe"
                if "地图" in a.text.split():
                    pass
                else:
                    print(a.text.split())

     
            print("-------------------------------------------------")
 
 
#下一页是否有
def is_next_page(soup_find_all,next):
    for tag in soup_find_all:
        for line in tag.strings:
           if line ==next:
               return  True
 
 
 
def mian():
    url = "http://baoding.ganji.com/fang1/xinshi/h3p3/"
    urlsize =1
    m2 = 0
    money = 0
    next=True
 
    while next:
        newurl =url.format(urlsize)
        urlsize+=1
        soup = BeautifulSoup(requests.get(newurl).text, "html.parser")
        settle_moneysize_data(soup.find_all('dd', class_='dd-item title'))
        money = settle_add_num(soup.find_all('span', class_='num'),money)#计算钱
        m2 =settle_add_m2(soup.find_all('dd', class_="dd-item size"),m2)#计算平方
        next =is_next_page(soup.find_all('ul',class_='pageLink clearfix'),str(urlsize))#判断是否还有
 
    print("当前房价为 ", int(money / m2), "一平")
 
    os.system('pause')
 
if __name__  =='__main__':
 
    mian()
else:
    print("请从bs4Demo启动 ，谢谢")
