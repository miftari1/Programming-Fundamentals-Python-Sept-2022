point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())


def closest_point(first, second, third, fourth):
    from math import floor
    sum_first_point = abs(first) + abs(second)
    sum_second_point = abs(third) + abs(fourth)
    if sum_first_point <= sum_second_point:
        result = f"({floor(first)}, {floor(second)})"
    else:
        result = f"({floor(third)}, {floor(fourth)})"
    return result


print(closest_point(point_x1, point_y1, point_x2, point_y2))
