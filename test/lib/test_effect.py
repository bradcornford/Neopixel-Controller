from __future__ import print_function
from neopixelcontroller.lib.effect import Effect
from neopixelcontroller.lib.controller import Controller
from neopixelcontroller.lib.color import Color
import unittest


class EffectMock(Effect):
    def __init__(self, parameter):
        super(EffectMock, self).__init__(parameter)

    def run(self, color=Color(0, 0, 0), milliseconds=50, iterations=0):
        return None


class EffectTestCase(unittest.TestCase):
    effect = None

    def setUp(self):
        self.effect = EffectMock(Controller())

    def test__init__(self):
        self.assertIs(type(self.effect), EffectMock)

    def test_stop(self):
        self.assertIs(self.effect.stop(), None)
        self.assertFalse(self.effect.ITERATE)


if __name__ == '__main__':
    unittest.main()
