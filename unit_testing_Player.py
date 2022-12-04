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
#         self.keys = []
#
#     def testLeftAndRightAtOnce(self):
#         self.keys.append(0)
#         self.keys.append(1)
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.X, 10)
#         self.assertEqual(self.player.Y, 10)
#         self.assertEqual(self.player.left, False)
#         self.assertEqual(self.player.right, False)
#         self.assertEqual(self.player.walkCount, 0)
#
#     def testUpAndDownAtOnce(self):
#         self.keys.append(2)
#         self.keys.append(3)
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.X, 10)
#         self.assertEqual(self.player.Y, 10)
#
#     def testEverythingAtOnce(self):
#         self.keys.append(0)
#         self.keys.append(1)
#         self.keys.append(2)
#         self.keys.append(3)
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.X, 10)
#         self.assertEqual(self.player.Y, 10)
#         self.assertEqual(self.player.left, False)
#         self.assertEqual(self.player.right, False)
#         self.assertEqual(self.player.walkCount, 0)
#
#     def testLeftUpAndDown(self):
#         self.keys.append(0)
#         self.keys.append(2)
#         self.keys.append(3)
#         self.player.movement(self.keys)
#         self.assertEqual(self.player.X, 5)
#         self.assertEqual(self.player.Y, 10)
#         self.assertEqual(self.player.left, True)
#         self.assertEqual(self.player.right, False)
#         self.assertEqual(self.player.walkCount, 1)


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


# class BorderCollisionTestCases(unittest.TestCase):
#     def setUp(self):
#         self.player = Player(1, 1, 1)
#
#     def testNormalDataX(self):
#         self.player.X = 50
#         self.assertEqual(self.player.borderCollision(), False)
#
#     def testNormalDataY(self):
#         self.player.Y = 69
#         self.assertEqual(self.player.borderCollision(), False)
#
#     def testBoundaryDataX(self):
#         self.player.X = 0
#         self.assertEqual(self.player.borderCollision(), True)
#
#     def testBoundaryDataY(self):
#         self.player.Y = m.screen.get_height()
#         self.assertEqual(self.player.borderCollision(), True)
#
#     def testErroneousDataX(self):
#         self.player.X = -99
#         self.assertEqual(self.player.borderCollision(), True)
#
#     def testErroneousDataY(self):
#         self.player.Y = -108
#         self.assertEqual(self.player.borderCollision(), True)

class AnimatePlayerTestCases(unittest.TestCase):
    def setUp(self):
        self.player = Player(1, 1, 1)

    def testNormalDataRight(self):
        self.player.right = True
        self.player.walkCount = 10
        self.player.animate()
        self.assertEqual(self.player.image, self.player.walkRight[2])

    def testNormalDataLeft(self):
        self.player.left = True
        self.player.walkCount = 13
        self.player.animate()
        self.assertEqual(self.player.image, self.player.walkLeft[3])

    def testBoundaryDataRight(self):
        self.player.right = True
        self.player.walkCount = 0
        self.player.animate()
        self.assertEqual(self.player.image, self.player.walkRight[0])

    def testBoundaryDataLeft(self):
        self.player.left = True
        self.player.walkCount = 23
        self.player.animate()
        self.assertEqual(self.player.walkCount, 0)

    def testErroneousData(self):
        self.player.right = True
        self.player.left = True
        self.player.walkCount = 5
        self.player.animate()
        self.assertEqual(self.player.image, self.player.idle)


spriteClassSuite = unittest.TestLoader().loadTestsFromTestCase(AnimatePlayerTestCases)

runner = unittest.TextTestRunner()
runner.run(spriteClassSuite)
