from selenium import webdriver

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

# Selenium 経由でブラウザを操作する
driver.get('https://carpe.dev')
print(driver.current_url)
driver.save_screenshot('search_results.png')

# ブラウザを終了する
driver.quit()