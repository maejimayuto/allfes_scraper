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

from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)

# MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
whole_page = driver.find_element_by_tag_name("html")
actions.move_to_element_with_offset(whole_page, 0, 0)

# MOVE TO DESIRED POSITION THEN CLICK
for x in range(80):
    print(x)
    actions.move_by_offset(x, 18)
    actions.click()
    actions.perform()
    driver.save_screenshot(f"search_results-{x}.png")

# ブラウザを終了する
driver.quit()