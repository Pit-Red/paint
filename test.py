import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        db.create_database()
        db.create_table()

    def test_insert(self):
        db.insert_draw('suca','coglione')

        self.assertTrue(db.contain_title('suca'))

    def test_get_description(self):
        db.insert_draw('suca','coglione')
        db.insert_draw('suc','coglione')
        db.insert_draw('sua','coglione')
        db.insert_draw('sca','coglione')
        db.insert_draw('uca','coglione')

        self.assertNotEqual(db.get_descriprion('cuao'),'coglion')


class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"SUCCESS: {test.id()}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"FAILURE: {test.id()}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"ERROR: {test.id()}")


if __name__ == '__main__':
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDatabase)
        runner = unittest.TextTestRunner(resultclass=CustomTestResult)
        result = runner.run(suite)