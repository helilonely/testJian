# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  17:41
# 文件           :DateTimePage.py
# IDE            :PyCharm

import base.base
import Pages
import allure


class DateTimePage(base.base.Base):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("将时间制改为24")
    def switch_24_time_sys(self):
        """
        将时间制度改为24
        :return:
        """
        #判断切换前的开关状态
        if "关闭" in self.get_switch_24_time_sys_text():
            self.hl_find_element(Pages.DateTimePageElement.sz_24).click()
        self.hl_allure_png(title="切换时间制")

    @allure.step("获取时间制的开关状态")
    def get_switch_24_time_sys_text(self):
        """
        获取时间制的开关状态
        :return:
        """
        return self.hl_find_element(Pages.DateTimePageElement.sz_24).get_attribute("text")
