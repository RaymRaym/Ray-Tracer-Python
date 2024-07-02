from hittable import hittable
from vec3 import vec3, dot

class sphere (hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = max(0, radius)
    
    def hit(self, r, ray_tmin, ray_tmax, rec):
        oc = r.origin - self.center
        a = r.direction.squared_length()
        h = dot(r.direction, oc)
        c = oc.squared_length() - self.radius * self.radius
        discriminant = h * h - a * c
        if discriminant < 0:
            return False
        sqrtd = discriminant ** 0.5
        # Find the nearest root that lies in the acceptable range.
        root = (h - sqrtd) / a
        if root <= ray_tmin or ray_tmax <= root:
            root = (h + sqrtd) / a
            if root <= ray_tmin or ray_tmax <= root:
                return False
            
        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal= (rec.p - self.center) / self.radius

        return True

    
