from PIL  import Image

def shrink(image, factor):
    """
    Builds and returns a new image which is a smaller copy of the
    argument image, by the given factor.
    """
    width = image.getWidth()
    height = image.getHeight()

    # Create a new smaller image
    new = Image(width // factor, height // factor)

    oldY = 0
    newY = 0

    while oldY < height - factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            # Get pixel from the original image
            oldP = image.getPixel(oldX, oldY)

            # Set the pixel in the new image
            new.setPixel(newX, newY, oldP)

            oldX += factor
            newX += 1

        oldY += factor
        newY += 1

    new.draw()
    return new  # Return the new image object

# Load the image and call the function
image = Image("emoji.jpg")
shrunk_image = shrink(image, 2)
 