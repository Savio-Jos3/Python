from PIL import Image

# Open an existing image file
img = Image.open("D:\Python\emoji.jpg")  # Replace with your image path

# Display the image in the default viewer
img.show()

# Get image size (width, height)
print(img.size)  # Example output: (800, 600)

# Get the format of the image (e.g., JPEG, PNG)
print(img.format)

# Convert image to grayscale
gray_img = img.convert("L")  # "L" mode is for grayscale
gray_img.show()

# Resize image to 200x200 pixels
resized_img = img.resize((200, 200))
resized_img.show()

# Rotate image 90 degrees counter-clockwise
rotated_img = img.rotate(90)
rotated_img.show()

# Crop image: (left, upper, right, lower) tuple
cropped_img = img.crop((100, 100, 400, 400))
cropped_img.show()

# Save the modified image to a new file
cropped_img.save("cropped_example.jpg")

# Create a new blank image (e.g., 100x100 white image)
blank_img = Image.new("RGB", (100, 100), "white")
blank_img.show()

# Paste an image onto another (must be same mode and size or provide a box)
# Example: Paste resized_img at position (0,0) on blank_img
blank_img.paste(resized_img, (0, 0))
blank_img.show()
