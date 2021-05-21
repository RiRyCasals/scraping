import sys
import os
from time import sleep
from collections import deque
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def make_save_directory(save_directory_path):
    if not os.path.exists(save_directory_path):
        os.makedirs(save_directory_path)


def obtain_html(driver):
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

    return driver


def obtain_image_urls(driver):
    image_urls = deque()
    elements = driver.find_elements_by_tag_name('img')
    for elem in elements:
        url = elem.get_attribute('src')

        if url not in image_urls:
            image_urls.append(url)

    return image_urls


def save_image(request, save_image_path):
    with open(save_image_path, 'wb') as f:
        f.write(request.content)


def download_images_from_urls(img_urls, save_directory_path):
    print("start download")
    for i, url in enumerate(img_urls):
        request = requests.get(url, stream=True)
        if request.status_code != 200:
            continue

        save_image_path = os.path.join(save_directory_path,
                                        '{:3}.png'.format(i))
        save_image(request, save_image_path)

        if (i + 1) % 10 == 0: # 最終的に削除
            print('{} / {} done'.format((i+1), len(img_urls)))
            break # for verification

    print('complete')



options = Options()
# options.add_argument('--headless') # 最終的に解除
driver = webdriver.Chrome('./chromedriver.exe',options=options)

scraping_word = 'モルカー'
driver.get('https://search.yahoo.co.jp/image/search?p={}'.format(scraping_word))
driver = obtain_html(driver)

save_directory_path = os.path.join('./images', scraping_word)
make_save_directory(save_directory_path)

image_urls = obtain_image_urls(driver)

driver.close()

download_images_from_urls(image_urls, save_directory_path)
