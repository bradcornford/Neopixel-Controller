from __future__ import print_function
from ..color import Color
from ..effect import Effect
import time


class EffectTheaterChase(Effect):

    def run(self, color=Color(0, 0, 0), milliseconds=50, iterations=10):
        print("[EffectTheaterChase][info] Theater chase: '%s' to NeoPixel pixels with pause '%d' milliseconds and '%d' iterations" % (color.get_hex(), milliseconds, iterations))

        try:
            while self.ITERATE:
                for j in range(iterations):
                    for k in range(3):
                        for i in range(0, self.controller.LEDS, 3):
                            self.controller.pixel_color(i + k, color)

                        time.sleep(milliseconds / 1000.0)

                        for i in range(0, self.controller.LEDS, 3):
                            self.controller.pixel_color(i + k, Color(0, 0, 0))
        except AttributeError:
            print("[EffectTheaterChase][error] An error occurred setting theater chase to NeoPixel pixels")
