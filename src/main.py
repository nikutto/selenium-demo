from selenium import webdriver
from PIL import Image

def main():
    print("Start")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options,
    )

    driver.get('https://github.com/nikutto')

    path = 'output/example.png'
    with open(path, 'wb') as f:
        f.write(driver.get_screenshot_as_png())

    with Image.open(path, 'r') as img:
        img.show()

    print("Done")

if __name__ == '__main__':
    main()