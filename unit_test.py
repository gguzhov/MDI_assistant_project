import unittest
from bot import check
from unittest.mock import MagicMock


# from unittest.mock import MagicMock

class TestMain(unittest.TestCase):
    def setUp(self):
        self.message = MagicMock()
        self.message.chat.id = 2

    def test_check1(self):
        self.message.text = "🏼 academic writing"
        self.assertEqual(0, check(self.message))

    def test_check2(self):
        self.message.text = "🖥 programming in Python"
        self.assertEqual(1, check(self.message))

    def test_check3(self):
        self.message.text = "🧮 financial & organizational accounting"
        self.assertEqual(2, check(self.message))

    def test_check4(self):
        self.message.text = "📊 probability theory & mathematical statistics"
        self.assertEqual(3, check(self.message))

    def test_check5(self):
        self.message.text = "🗣 business communications"
        self.assertEqual(4, check(self.message))

    def test_check6(self):
        self.message.text = "⌨️ data management in database design"
        self.assertEqual(5, check(self.message))


if __name__ == "__main__":
    unittest.main()
