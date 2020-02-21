# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  16:29
# 文件           :__init__.py
# IDE            :PyCharm

from appium.webdriver.common.mobileby import MobileBy


class SettingsFirstPageElement:
    """
    设置的首页元素
    """
    #时间和日期
    date_xpath = (MobileBy.XPATH, "//*[contains(@text,'日期和时间')]")


class DateTimePageElement:
    """
    时间和日期界面
    """
    sz_24 = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[5]//android.widget.Switch")
