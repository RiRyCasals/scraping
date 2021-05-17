import sys
import os
from time import sleep
from collections import deque
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def download_imgs(img_urls, save_directory):
    for i, url in enumerate(img_urls):
        file_name = '{}.png'.format(i)
        save_img_path = os.path.join(save_directory, file_name)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(save_img_path, 'wb') as f:
                f.write(r.content)
        if (i + 1) % 50 == 0:
            print('{} / {} done'.format((i+1), len(img_urls)))
        if (i + 1) == len(img_urls):
            print('complete')


word = 'チェロ'
save_directory = './images/cello'

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

options = Options()
# options.add_argument('--headless')   # 挙動確認のためコメントアウト
driver = webdriver.Chrome('./chromedriver.exe',options=options)

driver.get('https://search.yahoo.co.jp/image/search?p={}'.format(word))

image_urls = deque()

while True:
    preview_html = driver.page_source
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1.0)
    current_html = driver.page_source
    if preview_html != current_html:
        preview_html = current_html
    else:
        try:
            button = driver.find_element_by_class_name('sw-Button')
            button.click()
        except:
            break


elements = driver.find_elements_by_tag_name('img')
for elem in elements:
    url = elem.get_attribute('src')
    if url not in image_urls:
        image_urls.append(url)

driver.close()
download_imgs(image_urls, save_directory)