import cv2
import numpy as np
import math


def psnr1(img1, img2):
	mse = np.mean((img1 / 1.0 - img2 / 1.0) ** 2)
	if mse < 1.0e-10:
		return 100
	return 10 * math.log10(255.0 ** 2 / mse)


def psnr2(img1, img2):
	mse = np.mean((img1 / 255. - img2 / 255.) ** 2)
	if mse < 1.0e-10:
		return 100
	PIXEL_MAX = 1
	return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

result = []
for i in range(5):
	gt = cv2.imread('lena' + str(10000 + 10000 * i) + '.png')
	img = cv2.imread('lena.png')
	result.append(psnr1(gt, img))
	print(psnr1(gt, img))

import numpy as np
import matplotlib.pyplot as plt

x = [10000, 20000, 30000, 40000, 50000]

plt.plot(x, result, marker='*')

plt.title('PSNR')
plt.xlabel('bit')
plt.ylabel('PSNR')

plt.show()