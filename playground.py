from color import Color, HSV, rgb_to_hsv, hsv_to_rgb
import opc
from itertools import count
from time import sleep
from random import  randint
#from randomcolor import random_color

from bits import Bit
import pygame
numLEDs = 40
client = opc.Client('localhost:7890')
client.put_pixels([(0, 0, 0)] * 20)
pixels = [Color((0, 0, 0))] * 100
black = (0,0,0)
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
pink = (255, 0, 128)
purple = (255, 0, 255)
lavendar = (128,0,255)
green = (0, 255, 0)
lime = (128, 255, 0)
emerald = (0,255, 128)
turq = (128,255, 128)
blue = (0,0,255)
cyan = (0,255,255)
magenta = (255,0,255)
b = Bit()
color_variables = [red, orange, yellow, pink, purple, lavendar, green, lime, emerald, turq, blue, cyan, magenta]

def primaries():
    pixels = [red, green, blue, black, black, cyan, magenta, yellow]
    client.put_pixels([black]*20)
    client.put_pixels(pixels)

def putEm(pix):
    return [x.rgb for x in pix]


rainbow=['red','orange', 'yellow', 'green', 'blue','purple', 'blue', 'green','yellow','orange','red']

HUES = dict(red= 0/12.0, orange= 1/12.0, yellow=2/12.0, green=4/12.0, cyan= 6/12.0, blue=8/12.0, magenta=10/12.0)
pixels = []
c = count()
fps = 30
beat = next(c)
bps = 129/120.0
bong = 0.5
while True:
    beat = next(c)
    print
    if beat > (fps /bps):
        bong = 1.0
        pixels = [hsv_to_rgb(((beat%90)/100.0, 1.0, bong)) for i in range(numLEDs)]
        client.put_pixels(pixels)
        bong = 0.5
        c = count()
        beat = next(c)
    else:
        pixels = [hsv_to_rgb(((beat%900)/1000.0, 1.0, bong)) for i in range(0, 900, 10)]
        client.put_pixels(pixels)
    sleep(fps/6000.0)

