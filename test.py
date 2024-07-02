from vec3 import vec3, dot, cross, unit_vector, point3


a = vec3(1, 2, 3)
b = vec3(4, 5, 6)
# b /= 3
# print(b)

print(0.5 * b)

print(dot(a, b))
print(cross(a,b))
print(unit_vector(a), a)
# print(c.x, c.y, c.z)


