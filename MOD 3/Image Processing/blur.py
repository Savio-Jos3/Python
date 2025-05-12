from PIL import Image

def blur(image):
    """
    Returns a new image which is a blurred version of the original.
    Each pixel is averaged with its 4 neighbors.
    """
    width, height = image.size
    new = Image.new("RGB", (width, height))

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Get RGB tuples of center and 4 neighbors
            center = image.getpixel((x, y))
            left = image.getpixel((x - 1, y))
            right = image.getpixel((x + 1, y))
            top = image.getpixel((x, y - 1))
            bottom = image.getpixel((x, y + 1))

            # Sum the RGB values
            r_total = center[0] + left[0] + right[0] + top[0] + bottom[0]
            g_total = center[1] + left[1] + right[1] + top[1] + bottom[1]
            b_total = center[2] + left[2] + right[2] + top[2] + bottom[2]

            # Compute average
            r_avg = r_total // 5
            g_avg = g_total // 5
            b_avg = b_total // 5

            # Set the pixel in the new image
            new.putpixel((x, y), (r_avg, g_avg, b_avg))

    return new

# Load and blur the image
image = Image.open("emoji.jpg").convert("RGB")
image.show()

blurred = blur(image)
blurred.show()
