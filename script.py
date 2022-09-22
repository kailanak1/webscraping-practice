from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = 'https://www.scrapethissite.com/pages/'
wd.get(URL)

try:
    # check if the site loads
    wait = WebDriverWait(wd,20)
    html_page = wd.page_source
    # parse the site
    page = Soup(html_page,'html.parser')


    # put the titles in an array
    titles = []
    elems = page.findAll('h3', class_='page-title')
    for elem in elems:
        href = elem.find('a').get_text()
        titles.append(href)
    print(titles)
finally:
    wd.quit()
