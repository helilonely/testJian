# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  16:54
# 文件           :PageOne.py
# IDE            :PyCharm

import Pages.settings_page
import Pages.DateTimePage


class PageOne():

    def __init__(self, driver):
        self.driver = driver

    # 获取设置页
    def get_settings_page(self):
        return Pages.settings_page.SettingsFirstPage(self.driver)

    # 获取设置页中的日期时间页
    def get_dateTime_page(self):
        return Pages.DateTimePage.DateTimePage(self.driver)
