import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try :
    # Chrome のオプションを設定する
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Selenium Server に接続する
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=options.to_capabilities(),
        options=options,
    )
    artist_name_list_for_test = [
        "Def Tech",
        "AK-69",
        "kZm",
        "SHE'S",
    ]

    event_dict = dict()
    for artist_name in artist_name_list_for_test:
        time.sleep(5)
        url = 'https://t.pia.jp/pia/search_all.do?kw=' + artist_name
        driver.get(url)
        # Wait for the page to load
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'event_link'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # For debug
        import os
        directory = 'results'
        if not os.path.exists(directory):
            os.makedirs(directory)
        driver.save_screenshot(f"results/search_results-{artist_name}.png")
        with open(f"results/output-{artist_name}.html", "w", encoding = 'utf-8') as file:
            file.write(str(soup.prettify()))

        # Get event_url
        event_dict[artist_name] = []
        print(f'==================================== artist_name: {artist_name} ====================================')
        for event in soup.find_all('div', class_='event_link'):
            event_dict[artist_name].append(event.find('a').get('href'))
            # TODO: イベントのどの情報を取得したい？
            print(event.find('a').get('href'))
        print("event_dict:", event_dict)
    
    print("event_dict:", event_dict)
except Exception as e:
    print(e)
finally :
    # ブラウザを終了する
    driver.quit()