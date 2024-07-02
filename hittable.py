from ray import ray

class hit_record:
    def __init__(self, p, normal, t):
        self.p = p
        self.normal = normal
        self.t = t


class hittable:

    def hit(self, r: ray, ray_tmin: float, ray_tmax: float, rec: hit_record):
        pass
