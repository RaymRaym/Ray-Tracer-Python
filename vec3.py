class vec3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return vec3(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def __sub__(self, v):
        return vec3(self.x - v.x, self.y - v.y, self.z - v.z)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vec3(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return vec3(self.x * other, self.y * other, self.z * other)
    
    
    def __truediv__(self, other):
        return vec3(self.x / other, self.y / other, self.z / other)
        
    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"
    
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def squared_length(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
    

def dot(a: vec3, b: vec3):
    return a.x * b.x + a.y * b.y + a.z * b.z

def cross(a: vec3, b: vec3):
    return vec3(a.y * b.z - a.z * b.y,
                a.z * b.x - a.x * b.z,
                a.x * b.y - a.y * b.x)

def unit_vector(v: vec3):
    return v / v.length()

point3 = vec3





    

    