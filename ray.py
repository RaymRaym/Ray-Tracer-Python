from vec3 import unit_vector, vec3, dot
from color import color

class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + self.direction * t
    

def hit_sphere(center: vec3, radius: float, r: ray):
    oc = center - r.origin
    a = dot(r.direction, r.direction)
    b = 2.0 * dot(oc, r.direction)
    c = dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    return discriminant >= 0

def ray_color(r: ray):
    if hit_sphere(vec3(0, 0, -1), 0.5, r):
        return color(1, 0, 0)
    unit_direction = unit_vector(r.direction)
    a = 0.5 * (unit_direction.y + 1.0)
    return (1.0-a) * vec3(1.0, 1.0, 1.0) + a * vec3(0.5, 0.7, 1.0)