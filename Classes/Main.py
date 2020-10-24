from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from Project_List.Atributes.Atributes import *
from Project_List.Classes.Like import Like


class Main:
    def __init__(self, car_mark, environment):
        self.driver = webdriver.Chrome()
        self.__environment = environment
        self.action = ActionChains(self.driver)
        self.__car_mark = car_mark

    def enter_to_environment(self):
        """Entering to environment.(environment should be Link)"""

        self.driver.get(self.__environment)

    def go_to_cars_page(self):
        """Going to cars page with actions"""

        __first_window = self.driver.find_element_by_xpath(FIRST_WINDOW)
        self.action.move_to_element(__first_window).perform()

        __second_window = self.driver.find_element_by_xpath(SECOND_WINDOW)
        self.action.move_to_element(__second_window).perform()

        __third_window = self.driver.find_element_by_xpath(THIRD_WINDOW)
        __third_window.click()

        self.action.reset_actions()

    def pick_cars_mark(self):
        """Opel,Mercedes etc..."""

        __mark_type = self.driver.find_element_by_xpath(MARK_TYPE)
        __mark_type.click()
        __mark_type.send_keys(self.__car_mark)
        __mark_type.click()

    def __cars_count_in_page(self):
        cars_list = self.driver.find_elements_by_xpath(CARS_LIST)

        return len(cars_list)

    def __go_to_last_page(self):
        __a = self.driver.find_elements_by_xpath(BUTTON_NEXT)

        __count = 0
        while len(__a) > 0:
            __count += 1
            time.sleep(1)
            __a[0].click()
            __a = self.driver.find_elements_by_xpath(BUTTON_NEXT1)

        return __count

    def cars_count(self):
        """Calculating all cars count in all pages"""

        __first_page = self.__cars_count_in_page()
        __page_count = self.__go_to_last_page()
        __last_page = self.__cars_count_in_page()

        __total_cars_count = __first_page * __page_count + __last_page

        print(__total_cars_count)
        return __total_cars_count

    def liking(self):
        car = CAR_FOR_LIKING  # XPath
        liker = LIKER   # XPath
        a = Like(self.driver, car, liker)
        a.try_to_like()

    def go_to_fav_pub_page(self):
        """Go To Favourite Publications Page"""

        self.action = ActionChains(self.driver)
        user_icon = self.driver.find_element_by_xpath(USER_ICON)
        self.action.move_to_element(user_icon).perform()

        favourite_publications = self.driver.find_element_by_xpath(FAVOURITE_PUBLICATION)
        favourite_publications.click()

