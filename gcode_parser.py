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
    global last_x, last_y
    
    line = line.strip()
    x, y = get_coord(x_coord_regex, line), get_coord(y_coord_regex, line)

    if y is None and x is None:
        return None, None, line

    # Fill in missing values from previous line for linear moves
    if x is not None:
        last_x = x
    else:
        x = last_x

    if y is not None:
        last_y = y
    else:
        y = last_y
    return x, y, line


def update_gcode_line_xy(x: float, y: float, line: str, precision=4) -> str:
    line = re.sub(x_coord_regex, 'X' + str(round(x, precision)), line)
    line = re.sub(y_coord_regex, 'Y' + str(round(y, precision)), line)

    return line
