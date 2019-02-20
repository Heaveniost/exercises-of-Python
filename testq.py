import os 
from PIl import Image 

IPHONEWIDTH = 1136
IPHONEHEIGHT = 765

def get_imgs_path():
	list = []
	for path in os.listdir('./original'):
		list.append('./original' + '/' + 'path')
	return list 

def reset_image_size(path):
	image = Image.open(path)
	width, height = image.size 
	scale_width = width/IPHONEWIDTH
	scale_height = height/IPHONEHEIGHT
	scale = max(scale_width, scale_height)
	result_img = image.resize((int(width/scale), int(height/scale)), image.ANITI)
	img_name = os.path.basename(path)
	result_img.save('./rusult/' + img_name)

if __name__ == '__main__':
	paths = get_imgs_path()
	for path in paths:
		reset_image_size(path)
	