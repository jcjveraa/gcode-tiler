from gcode_parser import parse_gcode_line, update_gcode_line_xy
from gcode_tiler import rotate_point_around_origin, translate_point

input = open("./example/kitty_edited_jscut.gcode")
output = open("./example/kitty_edited_jscut_edited.gcode", "w")

for line in input.readlines():
    x, y, line = parse_gcode_line(line)
    if x is not None:
        x, y = rotate_point_around_origin((x, y), 180)
        x, y = translate_point((x, y), (50, 0))
        line = update_gcode_line_xy(x,y,line)
    print(x, y, line)

input.close()
output.close()
