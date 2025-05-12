from PIL import Image

def detectEdges(image, amount):
    """
    Builds and returns a new image in which the edges of the argument image 
    are highlighted and the colors are reduced to black and white.
    """

    # Helper function to calculate average intensity (luminance)
    def average(r, g, b):
        return (r + g + b) / 3

    # Define black and white pixel values
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)

    # Make a copy of the image to draw on
    new = image.copy()

    # Load pixel data
    original_pixels = image.load()
    new_pixels = new.load()

    # Get image dimensions
    width, height = image.size

    # Iterate through image pixels
    for y in range(height - 1):
        for x in range(1, width - 1):
            oldPixel = original_pixels[x, y]
            leftPixel = original_pixels[x - 1, y]
            bottomPixel = original_pixels[x, y + 1]

            oldLum = average(*oldPixel)
            leftLum = average(*leftPixel)
            bottomLum = average(*bottomPixel)

            # Edge detection condition
            if abs(oldLum - leftLum) > amount or abs(oldLum - bottomLum) > amount:
                new_pixels[x, y] = blackPixel
            else:
                new_pixels[x, y] = whitePixel

    return new

def main():
    # Load the image
    image = Image.open("emoji.jpg").convert("RGB")  # Convert to RGB just in case
    image.show(title="Original")

    # Detect edges with a threshold amount
    edgeDetectedImage = detectEdges(image, 20)
    edgeDetectedImage.show(title="Edge Detected")

if __name__ == "__main__":
    main()
# This code will open the original image and the edge-detected image in separate windows.