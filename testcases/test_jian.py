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
import time


class TestSword:
    def setup_class(self):
        self.driver = base.get_driver.get_driver()

        self.page_one = Pages.PageOne.PageOne(self.driver)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    @allure.feature("设置首页")
    @allure.story("日期时间页")
    @pytest.mark.settings
    @pytest.mark.skip(reason="暂时不运行")
    def test_settings(self):
        self.settingsPage = self.page_one.get_settings_page()
        self.dateTimePage = self.page_one.get_dateTime_page()

        self.settingsPage.click_date_time()
        self.dateTimePage.switch_24_time_sys()

    @pytest.mark.browser
    def test_browsers(self):
        """
       切换contect  [ NATIVE_APP  、  WEBVIEW_com.android.browser  ]
        :return:
        """
        # 判断是否有 WEBVIEW ,有则切换
        for context in self.driver.contexts:
            if "WEBVIEW" in context:
                self.driver.switch_to.context(context)
                print(self.driver.current_context)

        # 切换后h5后， 基本按web自动化操作
        self.driver.get("https://www.baidu.com")
        self.page_one.get_baidu_page().search_keys("cctv")


if __name__ == '__main__':
    try:
        print(base.performaceApp.get_start_time("com.android.browser", ".BrowserActivity"))
    except Exception as e:
        print(e, type(e))
