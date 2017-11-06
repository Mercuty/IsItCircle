import cv2
import glob
import os
import numpy as np


samples=[]
success=0
positive_path="C:/Users/a-zoshchuk/PycharmProjects/IsItCircle/controlPositive/"
negative_path="C:/Users/a-zoshchuk/PycharmProjects/IsItCircle/controlNegative/"
svm=cv2.ml.SVM_load("svm_data.dat")
hog = cv2.HOGDescriptor("hog.xml")

for filename in glob.glob(os.path.join(positive_path, '*.jpg')):
	img = cv2.imread(filename, 1)
	hist = hog.compute(img)
	samples.append(hist)

samples = np.float32(samples)

results = svm.predict(samples)

for result in results[1]:
	if (result > 0.5):
		success+=1

print(success/len(results[1]))

success=0
results=[]
samples=[]
for filename in glob.glob(os.path.join(negative_path, '*.jpg')):
	img = cv2.imread(filename, 1)
	hist = hog.compute(img)
	samples.append(hist)

samples = np.float32(samples)

results = svm.predict(samples)

for result in results[1]:
	if (result < 0.5):
		success+=1

print(success/len(results[1]))