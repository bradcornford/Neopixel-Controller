from __future__ import print_function
from ..color import Color
from ..effect import Effect
import time



class EffectKnightRider(Effect):

    def run(self, color=Color(0, 0, 0), milliseconds=20, iterations=1):
        print("[EffectKnightRider][info] Knight rider: to NeoPixel pixels with pause '%d' milliseconds and '%d' iterations" % (milliseconds, iterations))

        try:
            while self.ITERATE:
                for j in range(iterations):
                    for i in range(self.controller.LEDS):
                        self.controller.pixel_color(i, Color(255, 0, 0))
                        time.sleep(milliseconds / 1000.0)

                    for i in range(self.controller.LEDS, -1, -1):
                        self.controller.pixel_color(i, Color(0, 0, 0))
                        time.sleep(milliseconds / 1000.0)

                time.sleep(milliseconds / 1000.0)
        except AttributeError:
            print("[EffectKnightRider][error] An error occurred setting knight rider to NeoPixel pixels")
