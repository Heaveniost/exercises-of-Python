from PIL import Image, ImageDraw, ImageFont
#PIL https://pillow.readthedocs.org/
def add_num(img):
    draw = ImageDraw.Draw(img)
    #加载TrueType或OpenType字体文件，并创建一个字体对象。
    #windows系统中字体文件所在的位置 macOS也能运行是为什么
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=100)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-80, 0), '2', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')
    return 0

image = Image.open('d.jpg')
print(image.format,image.size,image.mode)
add_num(image)




