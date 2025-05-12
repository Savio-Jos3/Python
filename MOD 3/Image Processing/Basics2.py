from PIL import Image
import numpy as np

# Open the image
img = Image.open("emoji.jpg")  # Make sure this file exists in the same directory

# Print image format (e.g., JPEG, PNG)
print(img.format)

# Get image size as a NumPy array: (width, height)
a = np.array(img.size)

# Convert image to RGB mode (required for setting RGB tuples)
img = img.convert("RGB")

# Loop over every pixel (width = a[0], height = a[1])
for i in range(a[0]):       # x-coordinate (width)
    for j in range(a[1]):   # y-coordinate (height)
        # Set each pixel to a new RGB color based on position
        # Using modulo 256 to keep values in the valid 0–255 range
        img.putpixel((i, j), ((j - i) % 256, (i - j) % 256, (i + j) % 256))

# Display the modified image
img.show()
