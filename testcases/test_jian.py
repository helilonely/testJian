# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/17  15:23
# 文件           :test_jian.py
# IDE            :PyCharm


import os, sys, allure

sys.path.append(os.getcwd())

import base.get_driver
import pytest
import Pages.PageOne
import base.performaceApp


class TestSword:
    def setup_class(self):
        self.driver = base.get_driver.get_driver()
        self.page_one = Pages.PageOne.PageOne(self.driver)
        self.settingsPage = self.page_one.get_settings_page()
        self.dateTimePage = self.page_one.get_dateTime_page()

    def teardown_class(self):
        self.driver.quit()

    @allure.feature("设置首页")
    @allure.story("日期时间页")
    @pytest.mark.settings
    def test_settings(self):
        self.settingsPage.click_date_time()
        self.dateTimePage.switch_24_time_sys()

    @pytest.mark.sword
    def test_sword(self):
        print("ok")


if __name__ == '__main__':
    try:
        print(base.performaceApp.get_start_time(" com.android.browser", ".BrowserActivity"))
    except Exception as e:
        print(e, type(e))
