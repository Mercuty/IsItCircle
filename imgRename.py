import glob
import os

positive_path="C:/Users/a-zoshchuk/PycharmProjects/IsItCircle/triangles/"

for filename in glob.glob(os.path.join(positive_path, '*.jpg')):
	print(filename)
	filename2=filename[:filename.rfind("\\")+1]+"t"+filename[filename.rfind("\\")+1:]
	print(filename2)
	os.rename(filename, filename2)
