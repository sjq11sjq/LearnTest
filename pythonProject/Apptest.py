# -*- encoding=utf8 -*-
__author__ = "v-shenjiaqing"

from airtest.core.api import *
from time import sleep
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from unittestreport import TestRunner
import unittest
import os

# 打开MuMu模拟器
os.startfile(r'D:\MuMu\emulator\nemu\EmulatorShell\NemuPlayer.exe'), sleep(50)
# adb连接MuMu模拟器
os.system('adb connect 127.0.0.1:7555')
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


class WYCDApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 开启app:网易有道词典
        start_app("com.youdao.dict")
        poco(name='com.youdao.dict:id/toolbar').wait(40), sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        stop_app("com.youdao.dict")


if __name__ == '__main__':
    unittest.main()
    FileDir = "D:\\pythonProject\\case"
    suite1 = unittest.defaultTestLoader.discover(FileDir, pattern="case*.py", top_level_dir=None)
    runner = TestRunner(suite1, filename='D:\\pythonProject\\case\\apptest.html', report_dir='D:\\pythonProject\\report'
                        , title='APP自动化测试', tester='沈家庆')
    runner.run(suite1)
