from threading import Thread
from selenium.webdriver import Chrome
from time import sleep
import os
from datetime import datetime

"""
try:
    
    # Выбор категории поиска
    main_category = browser.find_elements_by_xpath('//*[@class="maincategories"]//*[@class="maincategories-list clr"]//a')
    id_category = [i.get_attribute('data-id') for i in main_category]
    browser.find_element_by_xpath('//*[@data-id=' + id_category[0] + ']').click()
    sleep(1)

    # Выбор подкатегории для поиска
    a = [i for i in browser.find_elements_by_xpath('//*[@data-category-id=' + id_category[0] + ']')]
    browser.find_element_by_xpath('//*[@data-id=' + a[0].get_attribute('data-id') + ']').click()
    sleep(10)

    
    sleep(2)
    browser.find_element_by_id('cityField').click()
    sleep(1)
    
    # Выбор региона для поиска
    a = browser.find_elements_by_xpath('//*[@id="regionslinks"]//*[@class="column part25"]/li/a')
    id_reg = [i.get_attribute('data-id') for i in a]
    browser.find_element_by_xpath('//*[@data-id=' + id_reg[0] + ']').click()
    sleep(0)

    # Выбор города для поиска
    b = browser.find_elements_by_xpath('//*[@id="subregionslinks"]//*[@class="column part25"]/li/a')
    id_sub_reg = [i.get_attribute('data-id') for i in b]
    browser.find_element_by_xpath('//*[@data-id=' + id_sub_reg[0] + ']').click()
    sleep(10)

    
except Exception as a:
    browser.close()
    print(a)
"""



def olx_serch(text_serch, choice_categories, choice_region):
    name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    browser = Chrome(os.path.join(os.getcwd(), 'chromedriver'))
    link = 'https://www.olx.ua/'
    browser.get(link)
    sleep(2)
    if choice_region:
        browser.find_element_by_id('cityField').click()
        sleep(1)
        # Выбор области
        browser.find_element_by_xpath('//*[@data-id=' + choice_region[0] + ']').click()
        sleep(2)
        # Выбор города
        browser.find_element_by_xpath('//*[@data-id=' + choice_region[1] + ']').click()
        sleep(2)
    if choice_categories:
        # Выбор категории
        browser.find_element_by_xpath('//*[@data-id=' + choice_categories[0] + ']').click()
        sleep(2)
        # Выбор подкатегории
        browser.find_element_by_xpath('//*[@data-id=' + choice_categories[1] + ']').click()
        sleep(2)
    if not text_serch:
        text_serch = ' '

    # Ввод текста для поиска
    try:
        input_serch = browser.find_element_by_id('search-text')
    except:
        input_serch = browser.find_element_by_id('headerSearch')
    input_serch.send_keys(text_serch)
    input_serch.submit()

    # Страница поиска
    try:
        not_found = browser.find_element_by_xpath('//*[@id="body-container"]/div[2]/div/div[2]')
        print(not_found.text)
    except:
        pass
    sleep(5)
    # Код парсинга ссылок объявлений и перехода по ним, сбора номеров телефонов
    list_links = []
    for i in range(1, 300):
        if i > 1:
            try:
                next_page = browser.find_element_by_xpath(
                    '//*[@class="pager rel clr"]//*[@class="fbold next abs large"]//a')
                browser.get(next_page.get_attribute('href'))
            except:
                break

        links_page = browser.find_elements_by_xpath("//*[@class='marginright5 link linkWithHash detailsLink']")

        for j in links_page:
            list_links.append(j.get_attribute('href'))

    phone_file = open('phone numbers ' + name + '.txt', 'w')

    for i in list_links:
        browser.get(i)
        element_phone = browser.find_elements_by_xpath('//*[@id="contact_methods"]/li[2]/div/span')
        if element_phone:
            element_phone[0].click()
            sleep(2)
            phone = browser.find_elements_by_xpath('//*[@id="contact_methods"]/li[2]/div/strong')
            a = str(phone[0].text)
            # Разбиение номера
            a = a.replace(' ', '')
            while a:
                if a.startswith('+38'):
                    a = a[3:]
                if a.startswith('38'):
                    a = a[2:]
                if a.startswith('00'):
                    a = a[1:]
                phone_file.write(a[:10] + '\n')
                a = a[10:]

    sleep(10)
    phone_file.close()
    browser.close()
 # toyota mark 2