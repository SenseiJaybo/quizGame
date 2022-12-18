import unittest
from Classes.Settings import Slider


class VolumeSettingsTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Slider(0, 0, machine=5)

    # def testFarRight(self):
    #     self.s.X = 440
    #     self.s.setVolume()
    #     self.assertEqual(self.s.volume, 2)
    #
    # def testFarLeft(self):
    #     self.s.X = -262
    #     self.s.setVolume()
    #     self.assertEqual(self.s.volume, 0)
    #
    # def testNormalValue1(self):
    #     self.s.X = 100
    #     self.s.setVolume()
    #     self.assertEqual(self.s.volume, 1.0313390313390314)
    #
    # def testNormalValue2(self):
    #     self.s.X = 89
    #     self.s.setVolume()
    #     self.assertEqual(self.s.volume, 1)

    def testErroneous1(self):
        self.s.X = -300
        self.s.setVolume()
        self.assertEqual(self.s.volume, 0)

    def testErroneous2(self):
        self.s.X = 1000
        self.s.setVolume()
        self.assertEqual(self.s.volume, 2)


ClassSuite = unittest.TestLoader().loadTestsFromTestCase(VolumeSettingsTestCase)

runner = unittest.TextTestRunner()
runner.run(ClassSuite)
