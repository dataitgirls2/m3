from crawl import *
from settings import END_DATE, START_DATE, KEYWORD, XLSX_PATH

start = START_DATE
end = END_DATE
keyword = KEYWORD
driver = webdriver.Chrome(WEB_DRIVER_PATH)

dates = []
titles = []
texts = []

# 키워드, 검색 시작/종료 날짜의 포스팅 url을 가져오기
blog_posting_urls = get_blog_posting_urls(keyword, start, end, driver)

# blog_postings의 date, text, title 가져오기
for posting_addr in blog_posting_urls:
    date = get_element(DATE, posting_addr, driver)
    dates.append(date)

    text = get_element(TEXT, posting_addr, driver)
    texts.append(text)

    title = get_element(TITLE, posting_addr, driver)
    titles.append(title)

# XLSX_PATH에 저장하기
save_xlsx(XLSX_PATH, KEYWORD, KEYWORD, dates, titles, texts)
