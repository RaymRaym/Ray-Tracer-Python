import logging
from color import color, write_color
from vec3 import vec3, point3
from ray import ray, ray_color

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] - %(message)s')
    logger = logging.getLogger()

    # image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    image_height = 1 if image_height == 0 else image_height

    # camera
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    camera_center = point3(0, 0, 0)

    viewport_u = vec3(viewport_width, 0, 0)
    viewport_v = vec3(0, -viewport_height, 0)

    viewport_u_delta = viewport_u / image_width
    viewport_v_delta = viewport_v / image_height

    viewport_upper_left = camera_center - viewport_u / 2 - viewport_v / 2 - vec3(0, 0, focal_length)
    pixel00_loc = viewport_upper_left + 0.5 * (viewport_u_delta + viewport_v_delta)


    # render
    print(f"P3\n{image_width} {image_height}\n255\n")

    for j in range(image_height):
        logger.info(f"current line: {j}/{image_height}")
        for i in range(image_width):
            pixel_center = pixel00_loc + i * viewport_u_delta + j * viewport_v_delta
            ray_direction = pixel_center - camera_center
            r = ray(camera_center, ray_direction)
            pixel_color = ray_color(r)
            write_color(pixel_color)
    logger.info("Done!")

    