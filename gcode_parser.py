import math
import re

last_x = 0
last_y = 0
x_coord_regex = r"X([\-0-9\.]+)"
y_coord_regex = r"Y([\-0-9\.]+)"


def get_coord(matcher, line):
    match = re.search(matcher, line)
    return match.groups(0)[0] if match else None


def parse_gcode_line(line: str):
    line = line.strip()
    # using_spaces = re.search(r"\s", line) is not None
    # sep = ' ' if using_spaces else ''
    x, y = get_coord(x_coord_regex, line), get_coord(y_coord_regex, line)
    return x, y, line


def update_gcode_line_xy(x: float, y: float, line: str, precision=4) -> str:
    line = re.sub(x_coord_regex, 'X' + str(round(x, precision)), line)
    line = re.sub(y_coord_regex, 'Y' + str(round(y, precision)), line)

    return line


# parse_gcode_line("G1 X22.7508 Y-21.8884")
# parse_gcode_line("G1X23.7508Y-21.8884")
# parse_gcode_line("G1X22.7508Y-21.8884")
# parse_gcode_line("G1Y-21.8884")
# parse_gcode_line("G1X-21.8884")

# print(update_gcode_line_xy(math.pi, -math.e, "G1X22.7508Y-21.8884"))
# print(update_gcode_line_xy(math.pi, -math.e, "G1 X22.7508 Y-21.8884"))
