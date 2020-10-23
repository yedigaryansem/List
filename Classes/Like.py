from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains

from Project_List.Atributes.Atributes import *


class Like:
    def __init__(self, driver, car_xpath, liker_xpath):
        self.__driver = driver
        self.__car_xpath = car_xpath
        self.__liker_xpath = liker_xpath

    def __liking(self):
        time.sleep(1)
        self.__action = ActionChains(self.__driver)
        __car = self.__driver.find_element_by_xpath(self.__car_xpath)
        self.__action.move_to_element(__car).perform()

        self.__action.reset_actions()

        __liker = self.__driver.find_element_by_xpath(self.__liker_xpath)
        time.sleep(0.5)
        __liker.click()

    def __login(self):
        login = self.__driver.find_element_by_xpath(LOGIN_XPATH)
        login.click()
        login.send_keys(LOGIN)

        password = self.__driver.find_element_by_xpath(PASSWORD_XPATH)
        password.click()
        password.send_keys(PASSWORD)

        enter = self.__driver.find_element_by_xpath(ENTER_TO_ACCOUNT)
        enter.click()

    def try_to_like(self):
        self.__liking()

        time.sleep(2)
        try:
            checker = self.__driver.find_element_by_xpath(DIALOG)
            # print(checker.text)
            if checker.text == 'Խնդրում ենք մուտք գործեք կամ գրանցվեք, որպեսզի կարողանաք ավելացնել ընտրածների մեջ:':

                link_xpath = self.__driver.find_element_by_xpath('/html/head/link[3]')
                remember_link = link_xpath.get_attribute("href")

                enter = self.__driver.find_element_by_xpath(ENTER_FOR_GOING_TO_SIGN_IN_PAGE)
                enter.click()
                self.__login()

                self.__driver.get(remember_link)

                self.__liking()

        except NoSuchElementException:
            print("U already logined")
