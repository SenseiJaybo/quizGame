import unittest
import TextBox
import Level


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.text = TextBox.Text()
        self.level = Level.Level()

    def testParagraph(self):
        self.text.getDialogue(self.level)
        print(self.text.dialogue)


if __name__ == '__main__':
    unittest.main()
