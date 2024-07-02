from vec3 import vec3

color = vec3

def write_color(pixel_color: color):
    r = int(255.999 * pixel_color.x)
    g = int(255.999 * pixel_color.y)
    b = int(255.999 * pixel_color.z)
    print(f"{r} {g} {b}\n")
