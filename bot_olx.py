from threading import Thread
from selenium.webdriver import Chrome
from time import sleep
import os


browser = Chrome(os.path.join(os.getcwd(), 'chromedriver'))
link = 'https://www.olx.ua/'
browser.get(link)
try:
    """
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

    # Ввод текста для поиска
    input_serch = browser.find_element_by_id('headerSearch')
    input_serch.send_keys('mark')
    input_serch.submit()
    
    # Страница поиска
    try:
        not_found = browser.find_element_by_xpath('//*[@id="body-container"]/div[2]/div/div[2]')
        print(not_found.text)
    except:
        pass
    sleep(5)
    """
   #   data-cy="page-link-next"
    # Тестовый код
    link = 'https://www.olx.ua/zapchasti-dlya-transporta/q-mark/'
    browser.get(link)
    list_links = browser.find_elements_by_xpath('//*[@id="offers_table"]//*[@class="space rel"]//a')
    try:
        while True:
            browser.find_element_by_xpath('//*[@class="fbold next abs large"]//*[@data-cy="page-link-next"]').click()
            list_links.append(browser.find_elements_by_xpath('//*[@id="offers_table"]//*[@class="space rel"]//a'))
    except:
        pass

    # for i in list_links:
    #     print(i.get_attribute('href'))
    print(list_links.__len__())
    sleep(10)
    browser.close()
except Exception as a:
    browser.close()
    print(a)