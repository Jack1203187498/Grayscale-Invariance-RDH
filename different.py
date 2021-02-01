
# 检查两幅图片的相似性
import numpy
import numpy as np
import cv2
from start import  *

def mtx_similar(arr1:np.ndarray, arr2:np.ndarray):
	if arr1.shape != arr2.shape:
		minx = min(arr1.shape[0], arr2.shape[0])
		miny = min(arr1.shape[1], arr2.shape[1])
		differ = arr1[:minx, :miny] - arr2[:minx, :miny]
	else:
		differ = arr1 - arr2
	numera = np.sum(differ ** 2)
	denom = np.sum(arr1 ** 2)
	similar = 1 - (numera / denom)
	return similar

img_path1 = "small.png"
img_path2 = "Rlena.png"
img_2 = cv2.imdecode(numpy.fromfile(img_path2,dtype=numpy.uint8),-1)

img_1 = cv2.imread(img_path1)
# img_2 = cv2.imread(img_path2)
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
# img_1 = cvtGray(img_1)
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
# img_2 = cvtGray(img_2)
# img_1 = cv2.cvtColor(img_1,cv2.COLOR_RGB2GRAY)
# img_2 = cv2.cvtColor(img_2,cv2.COLOR_RGB2GRAY)
img_1_squ = np.array(img_1)
img_2_squ = np.array(img_2)
print(mtx_similar(img_1_squ, img_2_squ))
