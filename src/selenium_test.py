from selenium import webdriver
from time import sleep


def get_whole_page(page_link: str, filename: str):
    
    with webdriver.Chrome() as chrome:
        
        chrome.get(page_link)
        
        # Берём вертикальное положение прокрутки страницы:
        offset = chrome.execute_script("return window.pageYOffset;")
        while True:
            # Дальше мы прокручиваем до самого конца:
            chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            # Задержка в секундах, в течение которой страница подгрузится:
            sleep(3)
            # Если есть возможность прокручивать дальше, то мы прокручиваем:
            if (new_offset := chrome.execute_script("return window.pageYOffset;")) != offset:
                offset = new_offset
            else:
                break

        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(chrome.page_source)
		
        chrome.quit()



example = get_whole_page('http://sample.oc.pro.project.garrip91.beget.tech/', 'index.html')
print(example)