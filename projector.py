

from itertools import count

import self as self
from pygame import time
import pygame
from random import randint, sample, choice
from grid import Grid
from color import Color, HSV, rgb_to_hsv, hsv_to_rgb, Primary
import opc
from copy import copy

clock = time.Clock()

client = opc.Client('localhost:7890')

c = count()
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'purple', 'blue', 'green', 'yellow', 'orange',
           'red']
frame = ([HSV(randint(0,100) / 100.0, 1, 1).rgb] * 40 for x in range(1000))


class Projector(object):
    def __init__(self, fps=60, grid=Grid()):
        self._fps = fps
        self._grid = grid
        self._patterns_master =[]

        self._clock = pygame.time.Clock()
        self._count = count()
        self.current_pattern = self._patterns[0]
        self._load_pattern
        self._set_frame()

    def _default(self):
        while True:
            yield [(0,0,0) for x in range(numLEDs)]


    #paterns will be a list of paterns generator
    def setPatterns(self, pattern_list):
        assert type(pattern_list, list)
        self._patterns_master.extend(pattern_list)
        if not self._patterns:
            self._patterns = copy(self._patterns_master)
        if not self._current:
            self._current = self._patterns.pop(0)


    @property
    def current_pattern(self):
        return self._current_pattern

    @current_pattern.setter
    def current_pattern(self, generator):
        print("setting new pattern")
        self._current_pattern = generator

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, value):
        assert 0 < value <60
        self._fps = value

    def _set_frame(self):
        if not self._patterns:
            self._patterns = copy(self._patterns_master)
        self._current = self._patterns.pop(0)
        return self._current

    def show(self):
        frame = self._set_frame(self)
        print(frame)
        while True:
            self._clock.tick(self._fps)
            try:
                f = next(frame)
                client.put_pixels(f)
                print(f)
            except StopIteration:
               self.show()


