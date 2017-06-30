from __future__ import print_function
from neopixelcontroller.lib.color import Color
from neopixelcontroller.lib.controller import Controller
import unittest


class ControllerTestCase(unittest.TestCase):
    controller = None

    def setUp(self):
        self.controller = Controller()

    def test__init__(self):
        self.assertIsInstance(self.controller, Controller)

    def test_color(self):
        self.assertIs(self.controller.color(Color(0, 0, 0)), None)

    def test_start_effect(self):
        self.assertIs(self.controller.start_effect('effect_test', Color(0, 0, 0)), None)

    def test_stop_effect(self):
        self.assertIs(self.controller.stop_effect(), None)

    def test_quit_effect(self):
        self.assertIs(self.controller.quit_effect(), None)

    def test_effects(self):
        self.assertIs(type(self.controller.effects()), list)

    def test__exit__(self):
        self.assertIs(self.controller.__exit__(), None)


if __name__ == '__main__':
    unittest.main()
