import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
from utils.driver_utils import DriverUtils
from pages.login_page import LoginPage

class FirstCase(unittest.TestCase):

    def setUp(self):
        self.driver = DriverUtils.get_driver()
        self.driver.implicitly_wait(5)
        self.driver.get()
        self.driver.maximize_window()

    def test_01(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("")
        loginPage.input_password("")
        loginPage.click_submit()
        time.sleep(3)
        ele = self.driver.get_window_size()
        print(ele)
        # 下拉滚动条
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"a[href=\"?C=Member\"]").click()
        # 添加用户
        # self.driver.find_element(By.CSS_SELECTOR,".s1 .primary-btn.h30.add").click()
        # self.driver.find_element(By.XPATH,"//input[@placeholder=\"姓名\"]").send_keys("daine")
        # self.driver.find_element(By.XPATH,"//input[@placeholder=\"手机号\"]").send_keys("18758796451")
        # self.driver.find_element(By.XPATH,"//input[@placeholder=\"登录密码\"]").send_keys("111111")
        # self.driver.find_element(By.CSS_SELECTOR,"button[id=\"addUserBtn\"]").click()

        users = []
        all_user = self.driver.find_elements(By.CSS_SELECTOR,"tr[class=\"nt\"] p font")
        # self.driver.find_element(By.LINK_TEXT,">").click()
        for one in all_user:
            users.append(one.text)

        print(users+"\n"+len(users))

    def test_02(self):
        self.driver.get("http://www.baidu.com")
        current_window = self.driver.current_window_handle
        self.driver.find_element_by_css_selector("#u1 a:nth-child(1)").click()
        time.sleep(5)
        handles = self.driver.window_handles
        for handle in handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                self.driver.find_element_by_link_text("迁徙地图").click()
                time.sleep(5)

    def test_03(self):
        self.driver.get("https://ke.qq.com/")
        ele = self.driver.find_element(By.CSS_SELECTOR,".header-index-category-text a")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.CSS_SELECTOR,"a[title=\"IT·互联网\"]").click()
        self.driver.find_element(By.CSS_SELECTOR,".mod-nav__link-nav-second a[title=\"软件测试\"]").click()
        time.sleep(5)

    def test_04(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.CSS_SELECTOR,"#kw.s_ipt").send_keys(Keys.RETURN)
        time.sleep(4)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()