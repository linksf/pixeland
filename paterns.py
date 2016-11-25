'''
example patter
'''

from bits import Bit
from color import hsv_to_rgb, HSV, rgb_to_hsv, RGB, Color
from grid import Grid
from projector import Projector
from random import randint, sample, choice
from itertools import count
from time import sleep
from opc import Client
client = Client('localhost:7890')
__all__ = ['RGB_CODES', 'HUES_primaries', 'create_random', 'spreaders', 'rainbow_test']

numLEDs = 40
RGB_CODES = dict(
    black=(0, 0, 0),
    red=(255, 0, 0),
    orange=(255, 128, 0),
    yellow=(255, 255, 0),
    pink=(255, 0, 128),
    purple=(255, 0, 255),
    lavendar=(128, 0, 255),
    green=(0, 255, 0),
    lime=(128, 255, 0),
    emerald=(0, 255, 128),
    turq=(128, 255, 128),
    blue=(0, 0, 255),
    cyan=(0, 255, 255),
    magenta=(255, 0, 255)
)
HUES_primaries = dict(
    red= 0,
    orange= 0.083333,
    yellow= 0.16667,
    green=0.33333,
    cyan= 0.5,
    blue = 0.66666,
    magenta= 0.83334
)
H = HUES_primaries
PRIMARY_OBJECTS = {}
for name, number in HUES_primaries.items():
    #print(name, number)
    PRIMARY_OBJECTS[name] =  HSV(number, 1, 1)

available_patterns = ['create_random', 'rainbow_test', ]
def create_random(projector, fps=30, duration=180):
    if fps < projector.fps:
        _fps = fps
    assert duration > 0
    count_down= _fps * duration
    print("test_generator")
    frame = 0
    _c = count(count_down, -1, -1)
    pixels = [(randint(0, 100), randint(100, 200), randint(0, 200)) for i in range(numLEDs)]
    c = next(_c)
    while c:
        if frame < fps:
            frame = frame +1
            c = next(_c)
            yield pixels
        else:
            r = randint(100, 200)
            g = randint(100, 200)
            b = randint(100, 200)
            pixels = [(r, g, b) for x in range(numLEDs)]
            frame = 0
            yield pixels



# def test_generator_2():
#     print("test_generator_2")
#     _c = count()
#     while
#         pixels = []
#         for j in range(numLEDs):
#             pixels.append((i + 20, i + 25, i + 35))
#         yield pixels

class Pattern(object):
    def __init__(self, seeds, commands=None, fps=60, duraiton=180, flags=None):
        self.fps = fps
        # a seed is a list of 2-tuples (joint, bit_dict) where joint is a 2-tuple (x,y)
        # and bit_dict is dict of bit key/value pairs
        self._seeds = seeds
        #
        self._commands = commands

    @property
    def seeds(self):
        string = ""
        for seed in self._seeds:
            for point, dic in seed:
                string += point
                for key, value in dic.items():
                    string += "{}: {}, ".format(key, value)
        return string

    @property
    def commands(self):
        result = ''
        for command in self._commands:
            result = result + ".{}()".format(command)
        return result

def rainbow_test(fps=60, duration=180):
    print("rainbow_test")
    _c = count(duration*fps)
    rainbow = [(hsv_to_rgb(((i / 1000), 1, 10 / 10.0))) for i in range(1000)]
    pixels = rainbow[0:numLEDs]

rainbow_trail = Pattern(Bit(seed=(0.0,1.0,1.0), core=(0,0), heading='e', speed=5))




def place_random(num,dim):
    return sample(num,range(dim[0]*dim[1]))



def spreaders(fps="5", grid=Grid(), color_list=[value for key, value in RGB_CODES.items()]):
    print(color_list)

