import unittest
from Sprite import Sprite


class InitialisingTestCases(unittest.TestCase):

    # def testInitialisingNormalData(self):
    #     """General application of the __init__ method"""
    #     sprite = Sprite(5, 10, 1, 'blue_lock_presentation_du_personnage_de_meguru_bachira_en_video_15460.jpg')
    #     self.assertEqual(sprite.X, 5)
    #     self.assertEqual(sprite.Y, 10)
    #     self.assertEqual(sprite.image.get_width(), 750)
    #     self.assertEqual(sprite.image.get_height(), 421)
    #     self.assertEqual(sprite.show, True)

    def testInitialisingBoundaryData(self):
        """Slightly more complicated values for the method to handle"""
        sprite = Sprite(10000, 1000000000, 2.1,
                        'blue_lock_presentation_du_personnage_de_meguru_bachira_en_video_15460.jpg')
        self.assertEqual(sprite.X, 10000)
        self.assertEqual(sprite.Y, 1000000000)
        self.assertEqual(sprite.image.get_width(), 1575)
        self.assertEqual(sprite.image.get_height(), 884)
        sprite.show = False
        self.assertEqual(sprite.show, False)

    def testInitialisingErroneousData(self):
        """All of these are instances where the data should be rejected"""
        sprite = Sprite(-20, -999, 1,
                        'blue_lock_presentation_du_personnage_de_meguru_bachira_en_video_15460.jpg')
        self.assertEqual(sprite.X, -20)
        self.assertEqual(sprite.Y, -999)
        sprite.show = 9
        self.assertEqual(type(sprite.show), '<class \'bool\'>')

    # def testInitialisingOfZero(self):
    #     sprite = Sprite(0, 0, 0, 'blue_lock_presentation_du_personnage_de_meguru_bachira_en_video_15460.jpg')
    #     self.assertEqual(sprite.X, 0)
    #     self.assertEqual(sprite.Y, 0)
    #     self.assertEqual(sprite.image.get_width(), 0)
    #     self.assertEqual(sprite.image.get_height(), 0)


spriteClassSuite = unittest.TestLoader().loadTestsFromTestCase(InitialisingTestCases)

runner = unittest.TextTestRunner()
runner.run(spriteClassSuite)
