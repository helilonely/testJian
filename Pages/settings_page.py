# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  16:39
# 文件           :settings_page.py
# IDE            :PyCharm

import Pages
import allure
from base.base import Base


class SettingsFirstPage(Base):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("点击日期时间页")
    def click_date_time(self):
        self.hl_scroll_screen()
        self.hl_scroll_screen()
        self.hl_find_element(Pages.SettingsFirstPageElement.date_xpath).click()
