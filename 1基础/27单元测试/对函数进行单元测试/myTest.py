import unittest

from 对函数进行单元测试 import add
from 对函数进行单元测试 import remove


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时候自动调用")

    def tearDown(self):
        print("结束测试时自动调用")

    # 为了测试 add 方法
    def test_add(self):
        self.assertEqual(add(1, 2), 3, "加法有误")
        pass

    # 为了测试 remove 方法
    def test_remove(self):
        self.assertEqual(remove(1, 2), -1, "减法有误")


if __name__ == '__main__':
    unittest.main()