# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/20  16:16
# 文件           :performaceApp.py
# IDE            :PyCharm
import os


def get_start_time(app_package, app_activity):
    """
    获取app的启动时间
    :param app_package: 包名
    :param app_activity: 启动名
    :return: 字典 包含Starting、Warning、Status、Activity、ThisTime、TotalTime、WaitTime
    """
    try:
        #执行adb 命令
        data = os.popen("adb shell am start  -W  {0}/{1}".format(app_package, app_activity))
        #读取cmd执行结果
        data2 = data.read()
        data.close()

        #start_info
        start_info = {}
        #去掉末尾的complete
        data2 = (data2.split("\n\n"))[0:-2]
        #将每一行的内容按：分割后加入字典start_info
        for line in data2:
            two_parts = line.split(": ")
            start_info[two_parts[0]] = two_parts[1]
        return start_info

    except Exception as e:
        #TODO 异常的处理
        print(e)


    def get_top_innfo(app_package):
        # 执行adb 命令
        data = os.popen("adb shell top | findstr {0}".format(app_package))
        # 读取cmd执行结果
        data2 = data.read()
        data.close()