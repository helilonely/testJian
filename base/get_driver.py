# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/19  16:09
# 文件           :get_driver.py
# IDE            :PyCharm
from appium import webdriver
import yaml, os


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
    :return: browserdriver
    """
    driver_yaml = get_yaml("base/driver.yaml")
    desired_capabilities = get_yaml("base/driver.yaml").get("browser")

    desired_capabilities["chromedriverExecutable"] = os.getcwd() + r"\base\browserdriver\chromedriver.exe"
    return webdriver.Remote(driver_yaml.get("url"), desired_capabilities=desired_capabilities)



if __name__ == '__main__':
    driver_info = get_yaml("driver.yaml").get("browser")
    driver_info["chromedriverExecutable"] = os.getcwd() + r"\base\browserdriver\chromedriver.exe"
    print(driver_info)
