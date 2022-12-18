import unittest
from Classes.Button_class import Button


class ButtonTests(unittest.TestCase):
    def setUp(self):
        b = Button(10, 10)

    def test(self):
        self.assertEqual(True, False)  # add assertion here


testSuite = unittest.TestLoader().loadTestsFromTestCase(ButtonTests)

runner = unittest.TextTestRunner()
runner.run(ButtonTests)
