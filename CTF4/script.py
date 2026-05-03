import cv2
import numpy as np
import re

def solve(imagePath):
    # Read the image as gray scale
    image = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
    print("Image loaded successfully.")
    
    # Flatten the 2D image matrix into a 1D array
    pixels = image.flatten()
    
    LSB = pixels & 1
    
    # Pack the 1s and 0s into actual byte values (0-255)
    bytes = np.packbits(LSB)
    
    # Convert the bytes into standard ASCII text ignoring binary garbage
    extractedText = bytes.tobytes().decode('ascii', errors='ignore')
    
    # Search for the specific CTF flag formats using Regex
    print("Scanning extracted data for flags...")
    match = re.search(r'(CMPN\{.*?\}|FLAG\{.*?\})', extractedText)
    
    if match:
        return f"\nFlag found: {match.group(0)}"

print(solve("CTF4/stego.png"))