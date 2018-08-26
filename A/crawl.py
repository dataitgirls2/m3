from urllib import parse
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
import time
import re

# url 만들고
base_url = 'https://m.search.naver.com/search.naver?display=15&nso=p%3A'
start = '20170305'
end = '20170405'
def make_url(keyword, start, end):
    period = 'from' + start + 'to' + end
    query = '&query=' + parse.quote(keyword)
    end = '&where=m_blog&start='
    final_url = base_url + period + query + end
    return final_url

basic_url = make_url('나노하나', start, end)

# page가 없을때까지 돌면서
index = 1
driver = webdriver.Chrome('C:\chromedriver.exe')
regex_href = r'.*https:\/\/m\.blog\.naver\.com\/(\w*\/\d*)'
blog_postings = []
flag = True
while(index < 15):
    url = basic_url + str(index)
    # index에 해당하는 html을 받아와
    driver.get(url)
    html = driver.page_source
    bs = BeautifulSoup(html, 'html5lib')
    links = bs.select('.bx a')
    for single_link in links:
    # #     #single_link가 https://m.blg.naver.com을 포함하면 그걸 가져오자
        href = re.findall(regex_href, str(single_link))
        if href != None and href !=[]:
            if href in blog_postings:
                flag = False
                break;
            else:
                blog_postings.append(href)
                # print(href)
    index += 15

# link를 돌면서 제목, 본문, 날짜 넣기
blog_base_url = 'https://m.blog.naver.com/'
titles = []
texts = []

regex_text = r'>((\w*\s?.?)*)<'
for posting_addr in blog_postings[:1]:
    posting_addr = str(posting_addr).strip('[]')
    posting_addr = posting_addr.strip('\'\'')
    url = blog_base_url + posting_addr

    driver.get(url)
    html = driver.page_source.encode('utf-8')
    bs = BeautifulSoup(html, 'html5lib', from_encoding='utf-8')
    title_divs = bs.select('.se_title > .se_textView > .se_textarea')
    text_divs = bs.select('.se_textView > .se_textarea > span')
    for title in title_divs:
        titles.append(title.text)

    text_for_blog = ''
    for text in text_divs:
        text = str(re.findall(regex_text, str(text)))
        text_final = re.sub(r'(<.*>)', '', text)
        text_final = re.sub(r'([\[\]\'])', '', text_final)
        text_final = text_final.strip('()')
        text_for_blog += text_final
    texts.append(text_for_blog)

print(len(titles))
print(len(texts))
