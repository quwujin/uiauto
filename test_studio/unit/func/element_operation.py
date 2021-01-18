import time
import allure


class Element_do:
    @allure.step("点击方法")
    def element_click(driver, xpath):
        """封装点击方法"""
        button_start = driver.find_element_by_xpath(xpath)
        button_start.click()
        time.sleep(0)
