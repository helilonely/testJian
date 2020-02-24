# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/21  17:19
# 文件           :BaiduFirstPage.py
# IDE            :PyCharm


import base.base
import Pages


class BaiduFirstPage(base.base.Base):
    def __init__(self, driver):
        self.driver = driver

    def search_keys(self, content):
        self.hl_send_keys(element_locator=Pages.BaiduElement.search_key_id, txt=content)
        self.hl_find_element(element_locator=Pages.BaiduElement.search_btn_id).click()
        self.hl_scroll_screen()

