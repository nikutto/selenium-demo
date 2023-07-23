from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def main():
    print("Start")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options,
    )
    print(type(driver))

    driver.get('http://fe-server/index.html')

    take_screen_shot_demo(driver)
    test_demo(driver)

    print("Done")


def take_screen_shot_demo(driver: WebDriver):
    path = 'output/example.png'
    with open(path, 'wb') as f:
        f.write(driver.get_screenshot_as_png())

    with Image.open(path, 'r') as img:
        img.show()


def test_demo(driver: WebDriver):
    h1 = driver.find_element(By.ID, 'index-hello')
    assert h1.text == "HELLO"
    print("OK1")
    a = driver.find_element(By.XPATH, "/html/body/div/a")
    assert a.text == "about"
    print("OK2")
    a.click()
    about_elem = driver.find_element(By.XPATH, "/html/body/div")
    assert about_elem.text == "This is a test message."
    print("OK3")


if __name__ == '__main__':
    main()