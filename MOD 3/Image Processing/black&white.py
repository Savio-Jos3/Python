from PIL import Image

def convert_to_black_and_white(image):
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Loop through each pixel using width and height
    for i in range(image.width):      # Correct usage
        for j in range(image.height): # Correct usage
            pixel = image.getpixel((i, j))  # Get RGB tuple

            # Calculate brightness by averaging RGB values
            brightness = sum(pixel) // 3  # [:3] ensures we handle RGB or RGBA

            # Set pixel to black or white based on brightness threshold
            if brightness < 128:
                image.putpixel((i, j), black)
            else:
                image.putpixel((i, j), white)

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
