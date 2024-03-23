from shutil import rmtree
from os import mkdir, path
from urllib.request import urlretrieve
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def ScrapeImages(search_query: str, images_number: int, download_location: str) -> None:
    THUMBNAIL_CLASS_NAME: str = "Q4LuWd"
    BUTTON_CLASS_NAME: str = "FAGjZe"
    IMAGE_CLASS_NAME: str = "iPVvYb"
    RESULTS_END_CLASS_NAME: str = "OuJzKb"
    
    images_number *= 1.4
    images_number = int(images_number)

    driver: Chrome = Chrome()

    driver.get("https://images.google.com/")

    driver.implicitly_wait(5)

    search_bar = driver.find_element(By.NAME, "q")

    search_bar.send_keys(search_query)
    search_bar.submit()

    while len(driver.find_elements(By.CLASS_NAME, THUMBNAIL_CLASS_NAME)) <= images_number and not driver.find_element(By.CLASS_NAME, RESULTS_END_CLASS_NAME).is_displayed():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            driver.find_element(By.CLASS_NAME, BUTTON_CLASS_NAME).click()
        except Exception:
            pass

    thumbnails = driver.find_elements(By.CLASS_NAME, THUMBNAIL_CLASS_NAME)[:images_number]

    urls: list[str] = []
    for thumbnail in thumbnails:
        try:
            thumbnail.click()
            urls.append(driver.find_element(By.CLASS_NAME, IMAGE_CLASS_NAME).get_attribute("src"))
        except Exception:
            pass

    driver.quit()

    database: str = f"{download_location}/images"

    if not path.exists(database):
        mkdir(database)

    directory: str = f"{database}/{search_query}"

    if path.exists(directory):
        rmtree(directory)

    mkdir(directory)

    for i in range(1, len(urls)):
        try:
            urlretrieve(urls[i], f"{directory}/image {i}.jpeg")
        except Exception:
            pass
