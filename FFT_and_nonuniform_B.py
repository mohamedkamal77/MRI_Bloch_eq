import cv2
import numpy as np
import matplotlib.pyplot as plt
import random



def non_uniform_B():
    B = random.sample(range(1, 101), 100)
    z = list(range(1, 101))
    plt.plot(z,B)
    plt.title('Non Uniformity of External Magnetic Field')
    plt.ylabel('External Magnetic Field')
    plt.xlabel('z')
    plt.show()


def FFT_image(path):
    img = cv2.imread(path, 0)
    FFT = np.fft.fft2(img)
    FFT_shift = np.fft.fftshift(FFT)
    FFT_abs=20*np.log(np.abs(FFT_shift))
    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title('Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(FFT_abs,cmap = 'gray')
    plt.title('FT of The Image'), plt.xticks([]), plt.yticks([])
    plt.show()

path="cairo.jpg"
FFT_image(path)
non_uniform_B()




