import unittest
import time

class TestTeenagerModeExecute(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('这是测试青少年模式的部分')

    def test_ctime_demo(self):
        print(time.ctime())

if __name__ == "__main__":
    unittest.main()
