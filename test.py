import os

import cv2
import matplotlib.pyplot as plt
import numpy as np

test_path = []

for filename in os.listdir(r"C:/Users/Artorius/PycharmProjects/model/EW-API/images"):
    test_path.append("C:/Users/Artorius/PycharmProjects/model/EW-API/images/" + filename)


image = cv2.imread(test_path[0])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.title("Clean", fontsize = 20)
plt.axis('off')
plt.show()

X_test = []

for path in test_path:
    image = cv2.imread(path)
    image = cv2.resize(image, (100, 100))
    X_test.append(image)

X_test = np.array(X_test)

print(X_test.shape)

X_test = X_test.astype('float32')

X_test /= 255

print(X_test.shape)