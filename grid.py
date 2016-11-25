from color import Color, is_hsv_tuple, is_rgb_tuple, HSV, RGB, rgb_to_hsv, hsv_to_rgb
import bits

__all__ = ['Grid']

#created by MASTER CONTROLER


class Point(object):
    def __init__(self, x, y):

        self._x = x
        self._y = y

    @property
    def coord(self):
        return (self._x, self._y)

    @coord.setter
    def coord(self, value):
        assert is_coord(value)
        self._x = value[0]
        self._y = value[1]


class Cell(object):
    def __init__(self, x, y,rgb=(0,0,0), visible=True):
        self._point = Point(x, y)
        self._visible = visible
        self._rgb = rgb
        self._x = x
        self._y = y
        self._neighbors = []

    def __repr__(self):
        return "Cell(x = {},y = {}, rgb = {}, visible={}".format(self._x, self._y, self._rgb, self._visible)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        pass

    @y.setter
    def y(self, value):
        pass

    @property
    def rgb(self):
        return self._rgb

    @rgb.setter
    def rgb(self, value):
        if is_rgb_tuple(value):
            self._rgb = value
        elif is_hsv_tuple(value):
            self._rgb = hsv_to_rgb(value)
        elif isinstance(value, Color):
            self._rgb = value.rgb
        else:
            self._rgb = self._rgb

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        pass

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, cell):
        self._neighbors.append(cell)


class Grid(object):
    def __init__(self, dimentions=(16, 16)):
        self._min_x, self._min_y = (0, 0)
        self._max_x = dimentions[0] -1
        self._max_y = dimentions[1] -1
        self._grid = [[Cell(x, y) for y in range(dimentions[1]-1)] for x in range(dimentions[0]-1)]
        self._bits = []
        self._assign_neighbors()
        self._list = self._make_list()

    def _make_list(self):
        list = []
        for row in self._grid:
            for cell in row:
                list.append(cell)
        return list
    def _assign_neighbors(self):
        def neighbor():
            while True:
                for x in range(-1,2):
                    for y in range(-1,2):
                        yield (x,y)

        for row in self._grid:
            n = neighbor()
            for cell in row:
                for i in range(8):
                    try:
                        x,y = next(n)
                        if (x, y) != (cell.x, cell.y) and self._min_x <= x <= self._max_x and self._min_y <= y <= self._max_y:
                            cell._neighbors.append((x + cell.x, y + cell.y))
                    except StopIteration:
                        continue
    @property
    def grid(self):
        return self._grid

    @property
    def __repr__(self):
        return self._list

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bit(self, bit):
        for b in self._bits:
            if b.id == bit.id:
                del b
                self._bits.append(bit)
                self._sort_bits()

    def _sort_bits(self):
        self._bits.sort(key=lambda x: x.z, reverse=False)

    def print_frame(self):
        for bit in self._bits:
            for b in bit.body:
                yield b

    def pixelator(self, pattern):
        total_frames = pattern.fps * (pattern.duration/1000)
        miliseconds_per_frame = 1000.00/fps
        def setup(pattern):
            for bit in pattern.seed:
                self._bits.insert(0, Bit)

