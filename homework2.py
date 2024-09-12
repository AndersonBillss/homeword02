from byuimage import Image

def flipped(filename):
    source_image = Image(filename)
    flipped_image = Image.blank(source_image.width, source_image.height)

    for x in range(flipped_image.width):
        for y in range(flipped_image.height):
            target_pixel = flipped_image.get_pixel(x,flipped_image.height-y-1)
            source_pixel = source_image.get_pixel(x,y)
            target_pixel.red = source_pixel.red
            target_pixel.green = source_pixel.green
            target_pixel.blue = source_pixel.blue
    return flipped_image

def make_borders(filename, thickness, red, green, blue):
    thickness-=1
    source_image = Image(filename)
    bordered_image = Image.blank(source_image.width + thickness * 2+2, source_image.height + thickness * 2+2)

    for x in range(bordered_image.width):
        for y in range(bordered_image.height):
            target_pixel = bordered_image.get_pixel(x,y)
            new_pixel= target_pixel
            if x>thickness and y>thickness and x<=source_image.width+thickness and y<=source_image.height+thickness:
                new_pixel = source_image.get_pixel(x-thickness-1, y-thickness-1)
            else:
                new_pixel.red = red
                new_pixel.green = green
                new_pixel.blue = blue

            target_pixel.red = new_pixel.red
            target_pixel.green = new_pixel.green
            target_pixel.blue = new_pixel.blue
    return bordered_image


def main():
    result = make_borders("test_files/landscape.png", 25, 0, 255, 0)
    result.show()

if __name__ == "__main__":
    pass

# main()