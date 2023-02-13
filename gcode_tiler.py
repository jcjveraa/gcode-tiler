import math

rounding_precision = 4


def rotate_point_around_origin(
        point: tuple[float, float], angle: float, degrees=True, round_result=False
) -> tuple[float, float]:
    if degrees:
        angle = angle / 180 * math.pi

    cos_angle, sin_angle = math.cos(angle), math.sin(angle)

    x, y = point[0], point[1]
    new_x = x * cos_angle - y * sin_angle
    new_y = y * cos_angle + x * sin_angle
    if round_result:
        new_x = round(new_x, rounding_precision)
        new_y = round(new_y, rounding_precision)

    return new_x, new_y


def rotate_point_around_point(
        point: tuple[float, float],
        rotation_point: tuple[float, float],
        angle: float,
        degrees=True,
        round_result=False,
) -> tuple[float, float]:
    center_x, center_y = rotation_point[0], rotation_point[1]
    # translate to origin
    x, y = translate_point(point, (-center_x, - center_y))
    # rotate
    x, y = rotate_point_around_origin((x, y), angle=angle, degrees=degrees)
    # translate back
    x, y = x + center_x, y + center_y

    if round_result:
        x = round(x, rounding_precision)
        y = round(y, rounding_precision)

    return x, y

def translate_point(point: tuple[float, float], translation: tuple[float, float]) -> tuple[float, float]:
    return point[0]+translation[0], point[1]+translation[1]

# print(rotate_point_around_origin((0, 2), 90))
# print(rotate_point_around_point((0, 2), (0, 1), 90))
