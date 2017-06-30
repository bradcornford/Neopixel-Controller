from __future__ import print_function
from ..color import Color
from ..effect import Effect
import time


class EffectColorWipe(Effect):

    def run(self, color=Color(0, 0, 0), milliseconds=50, iterations=1):
        print("[EffectColorWipe][info] Color wipe: '%s' to NeoPixel pixels" % (color.get_hex()))

        try:
            while self.ITERATE:
                for j in range(iterations):
                    for i in range(self.controller.LEDS):
                        self.controller.pixel_color(i, color)
                        time.sleep(milliseconds / 1000.0)
        except AttributeError:
            print("[EffectColorWipe][error] An error occurred setting color wipe to NeoPixel pixels")
