# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/28  17:45
# 文件           :test_api.py
# IDE            :PyCharm
import requests
import re
import urllib


class TestInterface:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_interface(self):
        """
        用接口 涉及 search  cookie   reqeusts
        :return:
        """
        sess = requests.session()
        # sess.cookies["BAIDUID"]="09DA37CA244BB61D5C7DA220A84A7AA6:FG=1"
        # sess.cookies["BDUSS"]="gwNlZ0Qkt5eVZsVnY4aUI1Y0xPQ29vcGV5ZHUzWWdTSm9OWVpMN3hsV2pRbXhlRVFBQUFBJCQAAAAAAAAAAAEAAAAR2XMous7A7TNnbwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKO1RF6jtURed2"

        header = {
            "Cookie": "BAIDUID=09DA37CA244BB61D5C7DA220A84A7AA6:FG=1;BDUSS=gwNlZ0Qkt5eVZsVnY4aUI1Y0xPQ29vcGV5ZHUzWWdTSm9OWVpMN3hsV2pRbXhlRVFBQUFBJCQAAAAAAAAAAAEAAAAR2XMous7A7TNnbwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKO1RF6jtURed2; "}
        response_data = sess.get(url=r"http://www.baidu.com", headers=header)
        print(re.search("何理3go", urllib.parse.unquote(response_data.text)))
        print(response_data.cookies)
        assert r'<a href="http://i.baidu.com" id="user" class="username">何理3go<i class="c-icon"></i></a>' in urllib.parse.unquote(
            response_data.text)
