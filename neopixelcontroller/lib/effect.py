from abc import ABCMeta, abstractmethod
from color import Color
import sys


class Effect:

    __metaclass__ = ABCMeta

    ITERATE = True

    controller = None

    def __init__(self, controller):
        self.ITERATE = True
        self.controller = controller

    @abstractmethod
    def run(self, color=Color(0, 0, 0), milliseconds=0, iterations=0):
        return NotImplemented

    def stop(self):
        self.ITERATE = False
