import time
import re
import numpy as np
import pandas as pd
from selenium import webdriver

# 用chrome
# browser = webdriver.Chrome()
browser = None


goal_url = 'https://search.bilibili.com/all?keyword=%E8%AF%B4%E5%94%B1%E6%96%B0%E6%97%B6%E4%BB%A3%20%E7%BA%AF%E4%BA%AB&page='

db = []

def get_one_html(url):
    browser.get(url)
    time.sleep(4)

    try:
        all_songs_information = browser.find_element_by_css_selector('#all-list > div.flow-loader > div.mixin-list > ul').get_attribute('innerHTML')
    except:
        all_songs_information = browser.find_element_by_css_selector('#all-list > div.flow-loader > ul').get_attribute('innerHTML')
    # #all-list > div.flow-loader > ul
    # #all-list > div.flow-loader > ul
    return all_songs_information


def get_all_pages():
    for i in range(1,7):
        url = goal_url+str(i)
        html = get_one_html(url)
        with open('page_informations/{}.txt'.format(str(i)),"w+") as f:
            f.write(html)

    pass


# 用正则表达式匹配需要的文本信息
def parse_one_page(html):
    # re.S	使 . 匹配包括换行在内的所有字符
    # pa = '<li.*?纯享】：(.*?)\n.*?</div>.*?<span.*?观看.*?icon-playtime.*?i.*?\n\s+(.*?)\n.*?</s.*?'
    # pa = '<li.*?纯享】：(.*?)\n.*?</div>.*?<span.*?观看.*?icon-playtime.*?i.*?\n\s+(.*?)\n.*?</s.*?<span.*?弹幕.*?icon-subtitle.*?i.*?\n\s+(.*?)\n.*?</s.*?<span.*?上传时间.*?icon-data.*?i.*?\n\s+(.*?)\n.*?</s.*?'
    pa = '<li.*?纯享】：(.*?)《(.*?)》\n.*?</div>.*?<span.*?观看.*?icon-playtime.*?i.*?\n\s+(.*?)\n.*?</s.*?<span.*?弹幕.*?icon-subtitle.*?i.*?\n\s+(.*?)\n.*?</s.*?<span.*?上传时间.*?icon-date.*?i.*?\n\s+(.*?)\n.*?</s.*?'
    pattern = re.compile(pa,re.S)
    items = re.findall(pattern, html)
    for item in items:
        item = list(item)
        db.append(item)
        print(item)


def deal_all_pages():
    for i in range(1,7):
        with open('page_informations/{}.txt'.format(str(i)),'r') as f:
            informations = f.read()
            parse_one_page(informations)

    new_db = np.array(db)
    song_informations = pd.DataFrame(new_db,columns=['singers','song','playtime','subtitle','date'])
    # 保存歌曲信息
    song_informations.to_csv('song_informations.csv',index=0)

if __name__ == '__main__':
    # 获取所有页面上的歌曲相关的信息

    # get_all_pages()

    deal_all_pages()