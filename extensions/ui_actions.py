import time
import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
import test_cases.conftest as conf
from utilities.common_ops import wait, For



class UiActions:
    @staticmethod
    @allure.step('click on Element')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('submit')
    def submit(elem: WebElement):
        elem.submit()

    @staticmethod
    @allure.step('update text in Element')
    def update_text(elem: WebElement, value):
        elem.clear()
        elem.send_keys(value)

    @staticmethod
    @allure.step('clear text from field')
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step('get text from Element')
    def get_text(elem: WebElement):
        return elem.text

    @staticmethod
    @allure.step('upload file to element')
    def upload_file(elem: WebElement, file_name):
        elem.send_keys(file_name)

    @staticmethod
    @allure.step('Drop down select by text')
    def select_by_text(elem: WebElement, value):
        drop_down = Select(elem)
        drop_down.select_by_visible_text(value)

    @staticmethod
    @allure.step('Drop down select by value')
    def select_by_value(elem: WebElement, value):
        drop_down = Select(elem)
        drop_down.select_by_value(value)

    @staticmethod
    @allure.step('Drop down select by index')
    def select_by_index(elem: WebElement, value):
        drop_down = Select(elem)
        drop_down.select_by_index(value)

    @staticmethod
    @allure.step('print all options from drop down')
    def print_all_dropdown(elem: WebElement):
        drop_down = Select(elem)
        list_to_return = drop_down.options
        for option in list_to_return:
            return option.text

    @staticmethod
    def switch_to_iframe(elem: WebElement):
        return conf.web_driver.switch_to.frame(elem)


    @staticmethod
    @allure.step('select imgs')
    def clicks_on_imgs(container: WebElement):
        elems = container
        for img in elems:
            img.click()

    @staticmethod
    @allure.step('count of elements')
    def count_of_element(container: WebElement):
        count = 0
        elems = container
        for img in elems:
            count += 1
        return  count

    @staticmethod
    @allure.step('verify URL')
    def current_url():
        return conf.web_driver.current_url

    @staticmethod
    @allure.step('verify URL title')
    def current_title():
        return conf.web_driver.title

    @staticmethod
    @allure.step('Navigate to Url')
    def navigate_to_url(url):
        time.sleep(1)
        return conf.web_driver.get(url)

    @staticmethod
    @allure.step('delete cookie')
    def clear_cookie():
        return conf.web_driver.get_cookies()

    @staticmethod
    @allure.step('refresh page')
    def refresh_page():
        return conf.web_driver.refresh()