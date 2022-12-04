import unittest
from Player import *


# class NormalTestCases(unittest.TestCase):
#     def setUp(self):
#         self.player = Player(1, 1, 1)
#
#     def testSpeed(self):
#         self.assertEqual(type(self.player.speed), type(1))
#
#     def testLeftAndRight(self):
#         self.assertEqual(self.player.left, False)
#         self.assertEqual(self.player.right, False)
#
#     def testWalkCount(self):
#         self.assertEqual(self.player.walkCount, 0)
#
#     def testSprite(self):
#         self.assertEqual(type(self.player.image.get_width()), type(1))
#         self.assertEqual(type(self.player.image.get_height()), type(1))
#
#     def testWalkLeftAndWalkRight(self):
#         self.assertEqual(len(self.player.walkLeft), 6)
#         self.assertEqual(len(self.player.walkRight), 6)
#         self.assertEqual(type(self.player.walkLeft[0].get_height()), type(1))
#         self.assertEqual(type(self.player.walkLeft[4].get_width()), type(1))
#         self.assertEqual(type(self.player.walkLeft[1].get_height()), type(1))
#         self.assertEqual(type(self.player.walkLeft[3].get_width()), type(1))


# class MovementTestCases(unittest.TestCase):
#     def setUp(self):
#         self.player = Player(10, 10, 1)
#         self.keys = 0
#
#     def testLeftMovement(self):
#         self.keys = 0
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.X, 10 - self.player.speed)
#         self.assertEqual(self.player.left, True)
#         self.assertEqual(self.player.right, False)
#         self.assertEqual(self.player.walkCount, 1)
#
#     def testRightMovement(self):
#         self.keys = 1
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.X, 10 + self.player.speed)
#         self.assertEqual(self.player.left, False)
#         self.assertEqual(self.player.right, True)
#         self.assertEqual(self.player.walkCount, 1)
#
#     def testUpMovement(self):
#         self.keys = 2
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.Y, 10 - self.player.speed)
#
#     def testDownMovement(self):
#         self.keys = 3
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.Y, (10 + self.player.speed))
#
#     def testIdle(self):
#         self.keys = 4
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.left, False)
#         self.assertEqual(self.player.right, False)
#         self.assertEqual(self.player.walkCount, 0)


class BorderCollisionTestCases(unittest.TestCase):
    def setUp(self):
        self.player = Player(1, 1, 1)

    def testNormalData(self):
        self.player.X = 50
        self.assertEqual(self.player.borderCollision())


spriteClassSuite = unittest.TestLoader().loadTestsFromTestCase(BorderCollisionTestCases)

runner = unittest.TextTestRunner()
runner.run(spriteClassSuite)
