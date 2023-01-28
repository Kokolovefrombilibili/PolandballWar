import unittest
import time

class TestTeenagerModeExecute(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('这是测试青少年模式的部分')

    def test_ctime_demo(self):
        print(time.ctime())

    # 测试能否将时间切片
    def test_cut_time_demo(self):
        print({time.ctime().split(" ")[0], time.ctime().split(" ")[1],
               time.ctime().split(" ")[2], time.ctime().split(" ")[4]})

if __name__ == "__main__":
    unittest.main()
