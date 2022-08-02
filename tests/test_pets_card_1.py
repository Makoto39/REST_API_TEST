import time
import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

def test_show_my_pets():
   pytest.driver.find_element_by_id('email').send_keys('dude@dude.ru')
   pytest.driver.find_element_by_id('pass').send_keys('dude')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_petfriends(selenium):
    selenium.get("https://petfriends.skillfactory.ru/my_pets")

    time.sleep(5)

    name = selenium.find_element_by_css_selector(
        "#all_my_pets > table > tbody > tr:nth-child(1) > td:nth-child(2)").text

    time.sleep(5)

    breed = selenium.find_element_by_css_selector(
        "#all_my_pets > table > tbody > tr:nth-child(1) > td:nth-child(3)").text

    time.sleep(5)

    age = selenium.find_element_by_css_selector("#all_my_pets > table > tbody > tr:nth-child(1) > td:nth-child(4)").text

    if name == "Нори" and breed == "гриффон" and age == "3":
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("pet card error")
