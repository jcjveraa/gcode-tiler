from gcode_parser import parse_gcode_line, update_gcode_line_xy
from gcode_tiler import rotate_point_around_origin, translate_point

input = open("./example/kitty_edited_jscut.gcode")
output = open("./example/kitty_edited_jscut_rotate_translate.gcode", "w")


for copy in range(4):
    for line in input.readlines():
        x, y, line = parse_gcode_line(line)
        if x is not None:
            angle_degrees = 180 if copy%2 == 1 else 0
            x, y = rotate_point_around_origin((x, y), angle_degrees)
            x, y = translate_point((x, y), (copy*25, 0))
            line = update_gcode_line_xy(x,y,line)
        output.write(line + '\n')
    input.seek(0)

input.close()
output.close()
