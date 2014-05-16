import unittest
from mysql import Mysql


class test_db(unittest.TestCase):

    def testRowCount(self):
        self.mql = Mysql()
        self.mql.populate()
        self.failIf(self.mql.rowcount() != 5)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
