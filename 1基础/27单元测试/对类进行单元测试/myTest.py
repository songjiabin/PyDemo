import unittest

from Person import Person


class Test(unittest.TestCase):

    def test_init(self):
        p = Person("基本密码", 18)
        self.assertEqual(p.name, "基本密码", "属性值name有误·")
        pass

    def test_getAge(self):
        p=Person("基本密码",20)
        self.assertEqual(p.getAge(),p.age,"方法getAge()有误")
        pass



if __name__ == '__main__':
    unittest.main()
