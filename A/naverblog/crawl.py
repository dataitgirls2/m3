from bs4 import BeautifulSoup
from urllib import request, parse
from selenium import webdriver
import time
import re
from settings import WEB_DRIVER_PATH
import xlwt

DATE = 0
TITLE = 1
TEXT = 2

def make_basic_url(keyword, start, end):
    print('make_basic_url')
    base_url = 'https://m.search.naver.com/search.naver?display=15&nso=p%3A'
    period = 'from' + start + 'to' + end
    query = '&query=' + parse.quote(keyword)
    end = '&where=m_blog&start='
    final_url = base_url + period + query + end
    return final_url

def get_blog_posting_urls(keyword, start, end, driver):
    print('get_blog_posting_urls')
    basic_url = make_basic_url(keyword, start, end)
    blog_postings = []
    index = 1
    flag = True
    regex_href = r'.*https:\/\/m\.blog\.naver\.com\/(\w*\/\d*)'
    while(flag):
        # index에 해당하는 url
        url = basic_url + str(index)

        driver.get(url)
        html = driver.page_source
        bs = BeautifulSoup(html, 'html5lib')
        links = bs.select('.bx a')
        for single_link in links:
        # single_link가 https://m.blg.naver.com을 포함하면 그걸 가져오자
            href = re.findall(regex_href, str(single_link))
            if href != None and href !=[]:
                if href in blog_postings:
                    flag = False
                    break;
                else:
                    blog_postings.append(href)
        index += 15
    return blog_postings

def get_element(type, posting_addr, driver):
    print('get_element')
    url = 'https://m.blog.naver.com/' + posting_addr[0]
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    bs = BeautifulSoup(html, 'html5lib', from_encoding='utf-8')

    switcher = {
        0: get_date,
        1: get_title,
        2: get_text
    }
    return switcher.get(type)(bs)

def get_date(bs):
    print('get_date')
    date_divs = bs.select('.se_date')
    date = re.findall(r'(20[\d\s\.\:]*)', str(date_divs))
    return date[0]

def get_text(bs):
    print('get_text')
    # 네이버는 에디터에 따라 css selctor가 달라진다
    text_divs1 = bs.select('.se_textView > .se_textarea > span,p')
    text_divs2 = bs.select('.post_ct span')

    if len(text_divs1) > len(text_divs2):
        final_text_div = text_divs1
    else:
        final_text_div = text_divs2

    text_for_blog = ''
    for text in final_text_div:
        text = re.sub(r'(\<.+?\>)', '', str(text))
        if text not in text_for_blog:
            text_for_blog += text
    return text_for_blog

def get_title(bs):
    print('get_title')
    title_divs = bs.select('.se_title > .se_textView > .se_textarea')
    if title_divs == []:
        title_divs = bs.select('.tit_h3')
    for title in title_divs:
        final_title = re.sub(r'(\s\s[\s]+)', '', str(title.text))
        return final_title

def save_xlsx(path, sheet_name, keyword, list1, list2, list3):
    print('save_xlsx')
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheet_name)
    index = 0
    for val1, val2, val3 in zip(list1, list2, list3):
        ws.write(index, 0, keyword)
        ws.write(index, 1, val1)
        ws.write(index, 2, val2)
        ws.write(index, 3, val3)
        index += 1
    wb.save(path)
