#1 IMAGE IMPORT

import os
import csv
from PIL import Image
import matplotlib.pyplot as plt

# Path to the image folder
folder_path = "C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images"


# List to store image information
image_info_list = []

# Read all .jpg and .png files
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(folder_path, filename)

        # Open the image
        img = Image.open(img_path)
        width, height = img.size

        # Display image
        plt.imshow(img)
        plt.title(f"{filename} ({width}x{height})")
        plt.axis("off")
        plt.show()

        # Store data
        image_info_list.append({
            "filename": filename,
            "width": width,
            "height": height,
            "area": width * height
        })

# Determine largest and smallest image based on area
largest_image = max(image_info_list, key=lambda x: x["area"])
smallest_image = min(image_info_list, key=lambda x: x["area"])

print("Largest Image:", largest_image)
print("Smallest Image:", smallest_image)

# Save to CSV file
csv_file = "image_sizes.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["filename", "width", "height", "area"])
    writer.writeheader()
    writer.writerows(image_info_list)

print(f"Image information saved to {csv_file}")


