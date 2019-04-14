import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.myList = []

    def clear(self):
        pass

    def test_getTest01(self):
        self.myList.append(1)
        print(self.myList)

    def test_getTest02(self):
        self.myList.append(2)
        print(self.myList)



if __name__ == '__main__':
    unittest.main()
