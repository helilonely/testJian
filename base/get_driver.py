# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  16:09
# 文件           :get_driver.py
# IDE            :PyCharm
from appium import webdriver
import yaml


def get_yaml(file_name):
    """
    读取yaml文件信息
    :param file_name:
    :return: 一个字典形式
    """
    with open(file_name, "r") as  f:
        return yaml.load(stream=f, Loader=yaml.FullLoader)


def get_driver():
    """
    获取driver ,默认路径是pytest.ini同级
    :return: driver
    """
    driver_info = get_yaml("base/driver.yaml")
    return webdriver.Remote(driver_info.get("url"),
                            desired_capabilities=driver_info.get("capabilities")
                            )


if __name__ == '__main__':
    print(get_yaml("driver.yaml"))
