import cv2
import matplotlib.pyplot as plt

# Read grayscale image
img = cv2.imread('input.jpg', 0)

# Negative transformation
negative = 255 - img

# Save image
cv2.imwrite('negative.jpg', negative)

# Display
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(negative, cmap='gray')
plt.title("Negative")
plt.axis('off')

plt.show()