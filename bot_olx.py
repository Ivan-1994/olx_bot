from threading import Thread
from selenium.webdriver import Chrome
from time import sleep
import os


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



def olx_serch(text_serch, choice_categories):
    browser = Chrome(os.path.join(os.getcwd(), 'chromedriver'))
    link = 'https://www.olx.ua/'
    browser.get(link)
    sleep(2)
    # Выбор категории
    browser.find_element_by_xpath('//*[@data-id=' + choice_categories[0] + ']').click()
    sleep(2)
    # Выбор подкатегории
    browser.find_element_by_xpath('//*[@data-id=' + choice_categories[1] + ']').click()
    sleep(2)
    # Ввод текста для поиска
    input_serch = browser.find_element_by_id('search-text')
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
    """
    link = 'https://www.olx.ua/zapchasti-dlya-transporta/avtozapchasti-i-aksessuary/q-toyota-mark'
    browser.get(link)
    """
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

    for i in list_links:
        browser.get(i)
        element_phone = browser.find_elements_by_xpath('//*[@id="contact_methods"]/li[2]/div/span')
        if element_phone:
            element_phone[0].click()
            sleep(2)
            phone = browser.find_elements_by_xpath('//*[@id="contact_methods"]/li[2]/div/strong')
            print(phone[0].text)
    sleep(10)
    browser.close()
