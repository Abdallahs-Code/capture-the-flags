from PIL import Image
import numpy as np

img1 = Image.open("Layer1.png")
img2 = Image.open("Layer2.png")

arr1 = np.array(img1)
arr2 = np.array(img2)

# Addition
result = ((arr1.astype(int) + arr2.astype(int)) % 256).astype(np.uint8)
Image.fromarray(result).save("Addition.png")

# Subtraction
result = ((arr1.astype(int) - arr2.astype(int)) % 256).astype(np.uint8)
Image.fromarray(result).save("Subtraction.png")

# Average
result = ((arr1.astype(int) + arr2.astype(int)) // 2).astype(np.uint8)
Image.fromarray(result).save("Average.png")