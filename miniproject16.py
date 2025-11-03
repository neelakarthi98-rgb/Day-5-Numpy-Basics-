import numpy as np

# Example 2D grayscale image (5x5 array)
image = np.random.randint(0, 256, size=(5, 5))

# Create an empty output array of same shape
blurred = np.zeros_like(image)

# Iterate over the image, skipping the border pixels
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        # Get the 3x3 region around the current pixel
        region = image[i-1:i+2, j-1:j+2]
        
        # Compute the average
        blurred[i, j] = np.mean(region)

# Print results
print("Original Image:\n", image)
print("\nBlurred Image:\n", blurred)
