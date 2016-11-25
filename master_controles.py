'''
The master controler instantiates and holds the various objects and establishes global parameters.

The cycle:

Set up - done once at the begining:
1. Controller sets FPS and dimensions then uses them to create a grid and projector
2. Controller sends the list of patterns to the projector via projector.show(list_of_patterns)
Loop - repeated for the rest of the cycle:
3. projector sends a pattern to the grid
4. grid returns a generator object which [next() => list of rgb tuples]
5. projector sets the clock and puts the pixels contained in next(generator) to the LEDs

Modules:
    (Controller) sets parameters and gets things going. It is a simple series of comands which will eventually get a GUI
    (Patterns) are made up of a setup and a loop cycle and are what determine which Bits get created and what methods are
        called on them. Patterns will be designed to real time (i.e. Bit a will travel across the screen in 1.5 seconds)
    (Bits) represent the objects (often abstract shapes) that travel around the grid and are represented by how pixels are
        lit up. A bit is made up of a CORE - which is the pixel that is actually being controlled - and a series of LIMBS
        - which are the pixels attached to it that move and change based on methods called to the core. All of the actions
        (movements, changes in color, shape, etc) that a bit can make are contained within itself and are called by the
        grid based on the instructions in the pattern.
        (Color) is an external class of objects that transition smoothly between various color spaces and easily manipulates
            common color attributes. Each Bit has a BASE color object that it uses.
    (Grid) represents the space in which bits move around, including space inside and outside the physical / viewable
        pixel board. It takes a set of instructions from the projector, instantiates bits, and runs a loop that yields
        frames (lists of rgb tuples). It's primary contributions to the process are in maintaining a consistent spacial
        structure, applying physics to bits, and transitioning from serpentine grid to pixel list;
    (Projector) stores the pattens from the controller, feeds a pattern to the Grid, taking a generator object of
     frames in return. It then creates a clock and puts the frame to the physcial pixels at the appropriate fps. When
     a generator is out of instances the projector sends the next pattern to the grid and starts the process again.

Bit Cycle (specific steps between loading the current pattern and putting pixels):
    a. (Projector) frame = calls self._grid.pixelate(pattern, fps, duration)
    b. (Grid) runs a setup for pattern which creates 1 or more Bit objects and any limbs it/they have
    c. (Grid) uses the loop part of the pattern to call methods on all or some of the bits, causing them to change one or
        more attributes such as size, position, color, etc. and yields the result to (Projector) under the variable 'frame'
        ** the generator object will produce at least (fps * duration) frames**
    d. (Projector) uses the pyGame clock ticker to put_pixles (next(frame)) to the client a fps frames per second
'''

# internal imports
from grid import Grid
from bits import Bit
from paterns import *
from projector import Projector

#external imports

# create 'global' variables
fps = 60
dimensions = (16,16)
# CREATE GRID
grid = Grid(dimensions=dimensions)
# CREATE PROJECTOR
projector = Projector(fps=fps, grid=grid)
# send patterns to grid and initialize

