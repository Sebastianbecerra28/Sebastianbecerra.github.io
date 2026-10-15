# EE 021 Midterm Project
# Name: Sebastian Becerra
# Project: Color Detector

import matplotlib.pyplot as plt
import numpy as np

print("Color Detector Project")
print("This program will detect a color in an image.")
print("You can choose red, green, or blue.")
from pathlib import Path

image_path = Path(__file__).resolve().parent / "Test_imagine.jpg"
image = plt.imread(image_path)

if image.dtype == np.uint8:
    image = image.astype(float) / 255.0


processed_image = image.copy()

print()
print("Choose a color to detect:")
print("1. Red")
print("2. Green")
print("3. Blue")

choice = input("Enter 1, 2, or 3: ")

threshold = float(input("Enter a detection threshold from 0 to 1, such as 0.5: "))

red_pixels = 0
green_pixels = 0
blue_pixels = 0
detected_pixels = 0

height = image.shape[0]
width = image.shape[1]

for row in range(height):
    for column in range(width):

        red = image[row, column, 0]
        green = image[row, column, 1]
        blue = image[row, column, 2]

        # Count dominant red pixels
        if red > green and red > blue:
            red_pixels = red_pixels + 1
        # Count dominant green pixels
        elif green > red and green > blue:
            green_pixels = green_pixels + 1
        # Count dominant blue pixels
        elif blue > red and blue > green:
            blue_pixels = blue_pixels + 1
        # Detect red
        if choice == "1":
            if red > threshold and red > green and red > blue:
                detected_pixels = detected_pixels + 1
            else:
                processed_image[row, column, 0] = 0
                processed_image[row, column, 1] = 0
                processed_image[row, column, 2] = 0
        # Detect green
        elif choice == "2":
            if green > threshold and green > red and green > blue:
                detected_pixels = detected_pixels + 1
            else:
                processed_image[row, column, 0] = 0
                processed_image[row, column, 1] = 0
                processed_image[row, column, 2] = 0

        # Detect blue
        elif choice == "3":
            if blue > threshold and blue > red and blue > green:
                detected_pixels = detected_pixels + 1
            else:
                processed_image[row, column, 0] = 0
                processed_image[row, column, 1] = 0
                processed_image[row, column, 2] = 0

if choice == "1":
    print("You selected Red.")
elif choice == "2":
    print("You selected Green.")
elif choice == "3":
    print("You selected Blue.")
else:
    print("Invalid color choice.")

print("Red pixels:", red_pixels)
print("Green pixels:", green_pixels)
print("Blue pixels:", blue_pixels)
print("Detected pixels:", detected_pixels)

total_pixels = height * width

if total_pixels > 0:
    detected_percentage = (detected_pixels / total_pixels) * 100
else:
    detected_percentage = 0

print("Percentage of image detected:", detected_percentage, "%")

plt.imshow(image)
plt.title("Original Image")
plt.axis("off")
plt.show()

plt.imshow(processed_image)

if choice == "1":
    plt.title("Detected Red Regions")
elif choice == "2":
    plt.title("Detected Green Regions")
elif choice == "3":
    plt.title("Detected Blue Regions")
else:
    plt.title("Processed Image")
plt.axis("off")
plt.savefig("processed_image.png")
plt.show()

colors = ["Red", "Green", "Blue"]
pixel_counts = [red_pixels, green_pixels, blue_pixels]

plt.bar(colors, pixel_counts)
plt.title("Color Distribution in Image")
plt.xlabel("Color")
plt.ylabel("Number of Pixels")
plt.savefig("color_distribution.png")
plt.show()