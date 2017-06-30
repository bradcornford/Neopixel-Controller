from __future__ import print_function
from ..color import Color
from ..effect import Effect
import time


class EffectTest(Effect):

    def run(self, color=Color(0, 0, 0), milliseconds=0, iterations=0):
        print("[EffectTest][info] Test: '%s' to NeoPixel pixels" % (color.get_hex()))
