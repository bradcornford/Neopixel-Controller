from __future__ import print_function
from neopixelcontroller.lib.color import Color
import unittest


class ColorTestCase(unittest.TestCase):
    color = None

    def setUp(self):
        self.color = Color(0, 0, 0, 0)

    def test__init__(self):
        self.assertIsInstance(self.color, Color)

    def test_get_rgb(self):
        self.assertEqual(self.color.get_rgb(), 'rgb(0,0,0)')

    def test_get_hex(self):
        self.assertEqual(self.color.get_hex(), '#000000')

    def test_get_hsv(self):
        self.assertEqual(self.color.get_hsv(), 'hsv(0,0,0)')


if __name__ == '__main__':
    unittest.main()
