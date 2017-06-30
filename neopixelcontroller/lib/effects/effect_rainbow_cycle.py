from __future__ import print_function
from ..color import Color
from ..effect import Effect
import time


class EffectRainbowCycle(Effect):

    def run(self, color=Color(0, 0, 0), milliseconds=20, iterations=1):
        print("[EffectRainbowCycle][info] Rainbow cycle: to NeoPixel pixels with pause '%d' milliseconds and '%d' iterations" % (milliseconds, iterations))

        try:
            while self.ITERATE:
                for j in range(256 * iterations):
                    for i in range(self.controller.LEDS):
                        self.controller.pixel_color(i, self.controller.color_wheel((int(i * 256 / self.controller.LEDS) + j) & 255))

                    time.sleep(milliseconds / 1000.0)
        except AttributeError:
            print("[EffectRainbowCycle][error] An error occurred setting rainbow cycle to NeoPixel pixels")
