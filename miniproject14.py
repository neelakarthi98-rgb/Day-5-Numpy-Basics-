import numpy as np
import matplotlib.pyplot as plt

fake_images=np.random.rand(100,100)

inversion=1.0-fake_images

cropping=fake_images[25:75,25:75]

visualization=plt.imshow(fake_images,cmap='gray')
plt.title("Original Fake Grayscale Image")
plt.axis('off')
plt.show()
