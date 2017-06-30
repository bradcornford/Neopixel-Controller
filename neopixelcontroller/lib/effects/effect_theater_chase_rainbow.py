from __future__ import print_function
from ..color import Color
from ..effect import Effect
import time


class EffectTheaterChaseRainbow(Effect):

    def run(self, color=Color(0, 0, 0), milliseconds=50, iterations=1):
        print("[EffectTheaterChaseRainbow][info] Theater chase rainbow: to NeoPixel pixels with pause '%d' milliseconds" % milliseconds)

        try:
            while self.ITERATE:
                for l in range(iterations):
                    for k in range(256):
                        for j in range(3):
                            for i in range(0, self.controller.LEDS, 3):
                                self.controller.pixel_color(i + j, self.controller.color_wheel((i + k) % 255))

                            time.sleep(milliseconds / 1000.0)

                            for i in range(0, self.controller.LEDS, 3):
                                self.controller.pixel_color(i + j, Color(0, 0, 0))
        except AttributeError:
            print("[EffectTheaterChaseRainbow][error] An error occurred setting theater chase rainbow to NeoPixel pixels")
