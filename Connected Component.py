import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra
img = cv2.imread('D:/ss/charlie.jpeg', 0)

# Mengubah citra ke biner
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Menerapkan connected components
num_labels, labels_im = cv2.connectedComponents(binary_img)

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Connected Components']
images = [img, binary_img, labels_im]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Menampilkan jumlah komponen terhubung
print(f'Jumlah connected components: {num_labels - 1}')  # Mengurangi 1 untuk tidak menghitung background
