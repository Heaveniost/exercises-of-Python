"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
"""
import os
from PIL import Image

IPHONE5_WIDTH = 1136
IPHONE5_HEIGHT = 640


def get_imgs_path():
    list = []
    for path in os.listdir('./original'):
        list.append('./original' + '/' + path)
    return list


def reset_image_size(path):
    image = Image.open(path)
    width, height = image.size
    scale_width = width / IPHONE5_WIDTH
    scale_height = height / IPHONE5_HEIGHT
    scale = max(scale_width, scale_height)
    result_img = image.resize((int(width / scale), int(height / scale)), Image.ANTIALIAS)
    img_name = os.path.basename(path)
    result_img.save('./result' + "/" + img_name)


if __name__ == '__main__':
    paths = get_imgs_path()
    for path in paths:
        reset_image_size(path)