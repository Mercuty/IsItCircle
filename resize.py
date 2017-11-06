import glob
import os

import cv2

path = "C:/Users/a-zoshchuk/PycharmProjects/IsItCircle/controlNegative/"
i = 1
for filename in glob.glob(os.path.join(path, '*.jpg')):
	print(i)
	try:
		img = cv2.imread(filename, 1)
		img2 = cv2.resize(img, (100, 100), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(path + "res" + str(i) + ".jpg", img2)
		i += 1
		os.remove(filename)
	except:
		print("error")
