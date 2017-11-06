from urllib.request import urlretrieve

urls=open("controlNegative.txt")

i=1
for url in urls:
	try:
		urlretrieve(url,".\\controlNegative/"+str(i)+".jpg")
		i += 1
		print(i)
	except:
		print("error"+str(i))