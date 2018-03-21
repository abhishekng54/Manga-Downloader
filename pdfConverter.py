from PIL import Image 
import os, re

def pdfMaker(term, c):

	address = os.path.abspath("Chapter " + c[0])
	files = os.listdir(address)
	files.sort(key=natural_keys)
	
	image_list = []
	for file in files:
		image = Image.open(address + "\\" + file)
		if image.mode == "RGBA": 
			image = im.convert("RGB")
		image_list.append(image)
	
	first = image_list.pop(0)

	#print(files)

	newFilename = address+"\\Chapter %s.pdf"%(c[0]) 

	if not os.path.exists(newFilename): 
		first.save(newFilename, "PDF", resolution=100.0, save_all=True, append_images=image_list)
	
	for imag in files:
		os.remove(address + "\\" + imag)
	
	print("It\'s done. Check it out.")

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]
	
	
#pdfMaker("one piece", 123)