from point import Point

point: Point = Point(2.00, 4.00)

new_point: Point = point.scale(2)

print(point.x, point.y)
print(new_point.x, new_point.y)