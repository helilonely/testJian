# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  16:16
# 文件           :base.py
# IDE            :PyCharm

from selenium.webdriver.support.wait import WebDriverWait
import allure


class Base:

    def hl_find_element(self, element_locator, timeout=15, frequency=0.5):
        """
        查找定位 元素
        :param element_locator: 元素定位方式
        :param timeout: 超时时间
        :param frequency: 频率
        :return:
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
            lambda x: x.find_element(*element_locator))

    def hl_send_keys(self, element_locator, txt, timeout=15, frequency=0.5):
        """
        元素中填写数据
        :param element_locator: 元素定位方式
        :param txt: 输入的文本
        :param timeout: 超时时间
        :param frequency: 频率
        :return:
        """
        self.hl_find_element(element_locator, timeout=timeout, frequency=frequency).send_keys(txt)

    def hl_allure_png(self, title):
        """
        allure 报告附件方式截图
        :param title: 截图标题
        :return:
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=title, attachment_type=allure.attachment_type.PNG)

    def hl_scroll_screen(self):
        """
        滑动屏幕，从0.8 到0.2
        :return:
        """

        if "WEBVIEW" in self.driver.current_context:
            self.driver.execute_script("window.scrollTo(0,1000)")
        else:
            win_size = self.driver.get_window_size()
            self.driver.swipe(win_size.get("width") * 0.5, win_size.get("height") * 0.8, win_size.get("width") * 0.5,
                              win_size.get("height") * 0.2)
