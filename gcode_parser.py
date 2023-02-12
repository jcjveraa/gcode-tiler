import re


last_x = 0
last_y = 0
x_coord_regex = r"X([\-0-9\.]+)"
y_coord_regex = r"Y([\-0-9\.]+)"

def get_coord(matcher, line):
    match = re.search(matcher, line)
    return match.groups(0) if match else None


def parse_gcode_line(line: str):
    line = line.strip()
    using_spaces = re.search(r"\s", line) is not None
    sep = ' ' if using_spaces else ''
    x, y = get_coord(x_coord_regex, line), get_coord(y_coord_regex, line)
    print(x, y, sep=sep)


parse_gcode_line("G1 X22.7508 Y-21.8884")
parse_gcode_line("G1X23.7508Y-21.8884")
parse_gcode_line("G1X22.7508Y-21.8884")
parse_gcode_line("G1Y-21.8884")
parse_gcode_line("G1X-21.8884")
