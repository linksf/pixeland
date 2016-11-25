#!/usr/bin/env python

from color import Color, HSV, RGB, hsv_to_rgb, rgb_to_hsv, is_rgb_tuple, is_hsv_tuple
from itertools import count
import opc, time
from random import randint

numLEDs = 20
client = opc.Client('localhost:7890')

black = [(0, 0, 0)] * numLEDs
white = [(255, 255, 255)] * numLEDs
c = count(100)

__all__ = ["Bit"]


def is_coord(value):
    return len(value) == 2 and all([type(x) == int for x in value])


class Bit(object):
    def __init__(self, core, seed,z,  speed=10, heading="e", limbs=None):
        self._core = core
        self._z = z
        self._id = next(c)
        self._base = seed
        self._body = [self._core,  ]
        self._limbs = limbs
        self._speed = speed
        self._directions = dict(n=(0, -1), ne=(1, -1), e=(1, 0), se=(1, 1), s=(0, 1), sw=(-1, 1), w=(-1, 0),
                                nw=(-1, -1))
        self.heading = heading
        self.set_limbs(limbs)

    def set_limbs(self, limbs):
        for limb in limbs:
            self.limbs
                append(limb)

    def move(self):
        delta_x, delta_y = self._heading
        self._core = (self._core[0] + delta_x, self._core[1] + delta_y)
        if self._limbs:
            print("self._limbs: {}".format(self._limbs))
            print("self._body: {}".format(self._body))


    def __repr__(self):
        return "Bit({}"

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        assert value in self._directions
        self._heading = self._directions[value]

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, seed):
        assert len(seed) == 3
        if is_hsv_tuple(seed):
            self._base = HSV(*seed)

    @property
    def limbs(self):
        return self._limbs

    @limbs.setter
    def limbs(self, limbs):
        for key, value in limbs:
            print("K: {}, V: {}".format(key, value))
            self._body.append(value)


    @property
    def body(self):
        return self._body

    def __sizeof__(self):
        return len(self._body)

    def __lt__(self, other):
        return self.z < other.z

    def __gt__(self, other):
        return self.z > other.z

    def __eq__(self, other):
        return self.z == other.z

    def __copy__(self):
        return Bit(self._grid, adjacent(self._core))

    #
    # @body.setter
    # def body(self, value):
    #

    def __add__(self, value):
        assert is_coord(value)
        if value not in self._body:
            self._body.append(value)

    def __sub__(self, value):
        assert is_coord(value)
        if value in self._body:
            self._body.remove(value)

    @property
    def body(self):
        result = [x for x in self._body]
        return result

    @property
    def rgb(self):
        return self._base.rgb

    @property
    def __sizeof__(self):
        return len(self._body)

    @property
    def core(self):
        return self._core

    @core.setter
    def core(self, value):
        assert is_coord(value)
        self._core = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        assert type(z) == int
        self._z = value
        # todo add to grid class
        grid.sort_bits()

    @property
    def grid(self):
        return self._grid

    @property
    def id(self):
        return self._id


def randpoint():
    while True:
        q= randint(0, 1000) / 1000.0
        print(q)
        yield q

p = randpoint()


def test_bits():
    n = "n"
    ne = "ne"
    e = "ne"
    se = "se"
    s = "s"
    sw = "sw"
    w = "w"
    nw = "nw"
    h, s, v = (next(p), next(p), next(p))
    # try:
    _x_ = randint(0,15)
    _y_ = randint(0,15)
    bit = Bit((_x_, _y_), HSV(h, s, v), randint(0, 10), limbs= {
        "point": [(_x_ + i, _y_) for i in range(5)], "color": HSV(h *.8, s*1.2 %1, v)})
    #   except:
    #      print("hmm, gotta fix somethin")
    print("bit.core: {}, bit.z: {}, bit.base.rgb: {}, bit.body: {}".format(bit.core, bit.z, bit.base.rgb, bit.body))
    bit.move()
    print("bit.core: {}, bit.z: {}, bit.base.rgb: {}, bit.body: {}".format(bit.core, bit.z, bit.base.rgb, bit.body))
    bit.heading = sw
    bit.move()
    print("bit.core: {}, bit.z: {}, bit.base.rgb: {}, bit.body: {}".format(bit.core, bit.z, bit.base.rgb, bit.body))
test_bits()