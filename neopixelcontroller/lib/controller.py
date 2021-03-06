from __future__ import print_function
from color import Color
from mock import MagicMock, patch
from effects import *
import os
import threading
import time

try:
    from neopixel import Adafruit_NeoPixel as Adafruit_Neopixel
except ImportError:
    print("[Neopixel][error] An error occurred importing 'neopixel.Adafruit_NeoPixel'")
    mock = MagicMock()
    mock.begin.return_value = True
    mock.show.return_value = True
    mock.setBrightness.return_value = True
    mock.setPixelColor.return_value = True
    with patch.dict('sys.modules', {'neopixel': mock, 'neopixel.Adafruit_NeoPixel': mock.Adafruit_NeoPixel}):
        from neopixel import Adafruit_NeoPixel as Adafruit_Neopixel


class Controller:

    LEDS = None

    NEOPIXEL_GPIO_PIN = None
    NEOPIXEL_FREQUENCY = None
    NEOPIXEL_DMA = None
    NEOPIXEL_INVERT = None
    NEOPIXEL_BRIGHTNESS = None
    NEOPIXEL_CHANNEL = None
    NEOPIXEL_STRIP = None

    neopixel = None

    thread = None

    effect = None

    def __init__(self, leds, neopixel_gpio_pin, neopixel_frequency, neopixel_dma, neopixel_invert, neopixel_brightness, neopixel_channel, neopixel_strip):
        print("[Neopixel][info] Initialising NeoPixel")

        self.LEDS = leds
        self.NEOPIXEL_GPIO_PIN = neopixel_gpio_pin
        self.NEOPIXEL_FREQUENCY = neopixel_frequency
        self.NEOPIXEL_DMA = neopixel_dma
        self.NEOPIXEL_INVERT = neopixel_invert
        self.NEOPIXEL_BRIGHTNESS = neopixel_brightness
        self.NEOPIXEL_CHANNEL = neopixel_channel
        self.NEOPIXEL_STRIP = neopixel_strip

        self.neopixel = Adafruit_Neopixel(
            self.LEDS,
            self.NEOPIXEL_GPIO_PIN,
            self.NEOPIXEL_FREQUENCY,
            self.NEOPIXEL_DMA,
            self.NEOPIXEL_INVERT,
            self.NEOPIXEL_BRIGHTNESS,
            self.NEOPIXEL_CHANNEL,
            self.NEOPIXEL_STRIP
        )

        try:
            self.neopixel.begin()
        except AttributeError:
            print("[Neopixel][error] An error occurred initialising NeoPixel")

    def pixel_color(self, pixel, color):
        print("[Controller][info] Setting color: '%s' to NeoPixel pixel '%d'" % (color.get_hex(), pixel))

        try:
            self.neopixel.setPixelColor(pixel, color.get_bit())
            self.neopixel.show()
        except AttributeError:
            print("[Controller][error] An error occurred setting color to NeoPixel pixel")

    def color_wheel(self, pos):
        print("[Controller][info] Generation a color wheel")

        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85

            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170

            return Color(0, pos * 3, 255 - pos * 3)

    def brightness(self, brightness):
        print("[Controller][info] Setting brightness: '%d' to NeoPixel pixels" % (brightness))

        try:
            self.neopixel.setBrightness(brightness)
            self.neopixel.show()
        except AttributeError:
            print("[Neopixel][error] An error occurred setting brightness on NeoPixel")

    def color(self, color):
        print("[Controller][info] Setting color: '%s' to NeoPixel pixels" % (color.get_hex()))

        try:
            for i in range(self.LEDS):
                self.pixel_color(i, color)

            self.neopixel.show()
        except AttributeError:
            print("[Controller][error] An error occurred setting color to NeoPixel pixels")

    def start_effect(self, effect, color):
        print("[Controller][info] Starting effect: '%s' to NeoPixel pixels" % (effect))

        try:
            self.effect = eval(effect + '.' + effect.replace('_', ' ').title().replace(' ', ''))(self)

            self.thread = threading.Thread(target=self.effect.run, args=(color,))
            self.thread.daemon = True
            self.thread.start()
        except AttributeError:
            print("[Controller][error] An error occurred starting effect to NeoPixel pixels")

    def stop_effect(self):
        print("[Controller][info] Stopping effect to NeoPixel pixels")

        try:
            if self.effect is not None:
                self.effect.stop()
        except AttributeError:
            print("[Controller][error] An error occurred stopping effect to NeoPixel pixels")

    def quit_effect(self):
        print("[Controller][info] Quitting effect to NeoPixel pixels")

        try:
            if self.effect is not None:
                self.thread.terminate()
        except AttributeError:
            print("[Controller][error] An error occurred quitting effect to NeoPixel pixels")

    def effects(self):
        print("[Controller][info] Getting a list of NeoPixel effects")

        try:
            effects = [file for file in os.listdir('./neopixelcontroller/lib/effects') if not file.startswith('.') and not file.startswith('__init__') and not file.endswith('.pyc') and not file.startswith('effect_test')]

            return [effect.replace('.py', '') for effect in effects]
        except AttributeError:
            print("[Controller][error] An error occurred get NeoPixel effects")

    def clear(self):
        print("[Controller][info] Clearing pixels on NeoPixel")

        try:
            self.stop_effect()
            self.quit_effect()
            self.color(Color(0, 0, 0))
            self.brightness(0)
        except AttributeError:
            print("[Controller][error] An error occurred clearing all pixels on NeoPixel")

    def cleanup(self):
        print("[Controller][info] NeoPixel clean up")

        self.clear()

    def __exit__(self):
        print("[Controller][info] NeoPixel exit")

        self.cleanup()
