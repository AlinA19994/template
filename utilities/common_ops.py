import csv
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


def get_time_stamp():
    return time.time()

def get_data(node_name):
    root = ET.parse('../configuration/data.xml').getroot()
    return root.find('.//'+node_name).text


def read_data_from_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def wait(for_element, elem, text=None):
    if for_element == 'element_exists':
        WebDriverWait(conf.web_driver, 10).until(ES.presence_of_element_located((elem[0], elem[1])))

    if for_element == 'element_displayed':
        WebDriverWait(conf.web_driver, 10).until(ES.visibility_of_element_located((elem[0], elem[1])))

    if for_element == 'element_to_be_clickable':
        WebDriverWait(conf.web_driver, 10).until(ES.element_to_be_clickable((elem[0], elem[1])))

    if for_element == 'text_to_be_present_in_element_value':
        WebDriverWait(conf.web_driver, 10).until(ES.text_to_be_present_in_element_value((elem[0], elem[1]), text))

    if for_element == 'text_to_be_present_in_element':
        WebDriverWait(conf.web_driver, 10).until(ES.text_to_be_present_in_element((elem[0], elem[1]), text))

    if for_element == 'disappear':
        WebDriverWait(conf.web_driver, 10).until_not(ES.visibility_of_element_located((elem[0], elem[1])))

    if for_element == 'staleness_of':
        WebDriverWait(conf.web_driver, 10).until_not(ES.staleness_of((elem[0], elem[1])))

    if for_element == 'element_located':
        WebDriverWait(conf.web_driver, 10).until_not(ES.presence_of_element_located((elem[0], elem[1])))

    if for_element == 'visibility_of':
        WebDriverWait(conf.web_driver, 10).until_not(ES.visibility_of((elem[0], elem[1])))

    if for_element == 'visibility_of_element_located':
        WebDriverWait(conf.web_driver, 10).until_not(ES.visibility_of((elem[0], elem[1])))


# Enum for selecting displayed element or exist element , my method uses this emun
class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_TO_BE_CLICKABLE = 'element_to_be_clickable'
    TEXT_TO_BE_PRESENT_IN_ELEMENT_VALUE = 'text_to_be_present_in_element_value'
    TEXT_TO_BE_PRESENT_IN_ELEMENT = 'text_to_be_present_in_element'
    DISAPPEAR = 'disappear'
    STALENESS_OF = 'staleness_of'
    ELEMENT_LOCATED = 'element_located'
    VISIBILITY_OF = 'visibility_of'
    VISIBILITY_OF_ELEMENT_LOCATED = 'visibility_of_element_located'