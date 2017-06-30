from __future__ import print_function
from neopixelcontroller.lib.color import Color
from neopixelcontroller.lib.controller import Controller
import unittest


class ControllerTestCase(unittest.TestCase):
    controller = None

    LEDS = 1
    NEOPIXEL_GPIO_PIN = 1
    NEOPIXEL_FREQUENCY = 0
    NEOPIXEL_DMA = 0
    NEOPIXEL_INVERT = False
    NEOPIXEL_BRIGHTNESS = 0
    NEOPIXEL_CHANNEL = 0
    NEOPIXEL_STRIP = 0

    def setUp(self):
        self.controller = Controller(
            self.LEDS,
            self.NEOPIXEL_GPIO_PIN,
            self.NEOPIXEL_FREQUENCY,
            self.NEOPIXEL_DMA,
            self.NEOPIXEL_INVERT,
            self.NEOPIXEL_BRIGHTNESS,
            self.NEOPIXEL_CHANNEL,
            self.NEOPIXEL_STRIP
        )

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
