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
    a = r.direction.squared_length()
    h = dot(oc, r.direction)
    c = oc.squared_length() - radius * radius
    discriminant = h * h - a * c
    if discriminant < 0:
        return -1.0
    else:
        return (h - discriminant ** 0.5) / a

def ray_color(r: ray):
    t = hit_sphere(vec3(0, 0, -1), 0.5, r)
    if t > 0:
        N = unit_vector(r.at(t) - vec3(0, 0, -1))
        return 0.5 * color(N.x + 1, N.y + 1, N.z + 1)
    
    unit_direction = unit_vector(r.direction)
    a = 0.5 * (unit_direction.y + 1.0)
    return (1.0-a) * vec3(1.0, 1.0, 1.0) + a * vec3(0.5, 0.7, 1.0)