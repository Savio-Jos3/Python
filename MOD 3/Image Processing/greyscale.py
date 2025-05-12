from PIL import Image
import numpy as np

def convert_to_black_and_white(image):
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Loop through each pixel using width and height
    for i in range(image.width):      # Correct usage
        for j in range(image.height): # Correct usage
            pixel = np.array(image.getpixel((i, j)))  # Get RGB tuple

            pixel[0] = pixel[0] * 0.299
            pixel[1] = pixel[1] * 0.587
            pixel[2] = pixel[2] * 0.114

            # Calculate brightness by averaging RGB values
            Lum = sum(pixel[:3]) // 3 

            image.putpixel((i, j), (Lum,Lum,Lum))

def main():
    # Open the image and ensure it is in RGB mode
    img = Image.open("emoji.jpg").convert("RGB")

    # Convert image to black and white
    convert_to_black_and_white(img)

    # Save and display the new image
    img.save("black_and_white_emoji.jpg")
    img.show()

if __name__ == "__main__":
    main()
