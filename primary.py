from color import Color
from random import random, randint

__all__


class Primary(Object):
    def __init__(self, name="", h_min=0.0, h_max=1.0, base=None, mixer=None):
        self._name = name
        self._h_min = h_min
        self._h_max = h_max
        self._base = base
        self._mixer = mixer
