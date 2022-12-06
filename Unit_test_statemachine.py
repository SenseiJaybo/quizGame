import unittest
from State_machine import GameMachine


class stateMachineTesting(unittest.TestCase):
    def setUp(self):
        self.machine = GameMachine()

    def testStart(self):
        self.assertEqual(self.machine.is_title, True)

    def testSettingsTransition(self):
        self.machine.openSettings()
        self.assertEqual(self.machine.is_settings, True)

    def testGoingBackFromSettings(self):
        self.machine.openSettings()
        self.machine.goBack()
        self.assertEqual(self.machine.is_settings, False)

    def testLevel1(self):
        self.machine.openLevel1()
        self.assertEqual(self.machine.is_level1, True)

    def testLevel2(self):
        self.machine.openLevel2()
        self.assertEqual(self.machine.is_level2, True)

    def testLevel1Finish(self):
        self.machine.openLevel1()
        self.machine.finishLevel1()
        self.assertEqual(self.machine.is_level1, False)
        self.assertEqual(self.machine.is_title, True)

    def testLevel2Finish(self):
        self.machine.openLevel2()
        self.machine.finishLevel2()
        self.assertEqual(self.machine.is_level2, False)
        self.assertEqual(self.machine.is_title, True)

    def testExit(self):
        self.machine.leaveGame()
        self.assertEqual(self.machine.is_leave, True)


testSuite = unittest.TestLoader().loadTestsFromTestCase(stateMachineTesting)

runner = unittest.TextTestRunner()
runner.run(testSuite)
