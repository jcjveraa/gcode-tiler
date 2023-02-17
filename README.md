# gcode-tiler
A simple tool to tile gcode for 2.5D CAM / CNC by applying horizontal offsets and rotations. Initially this will need to be done manually, but if I'm feeling fancy I might extend it to something automatic.

Created with Python 3.10 because that's what I had installed - it will probably run with any Python 3 version.

The Cat I use as an example was downloaded from https://freesvg.org/cat-line-art and is public domain according to that website/the tags in the file. I edited it to make it more simple and generated simple gcode using http://jscut.org/jscut.html.

Run the example program by running `python runner.py`

## TODO
 - Detect & prevent motor start/stop between copies