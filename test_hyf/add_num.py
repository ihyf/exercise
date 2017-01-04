# coding:utf-8
from PIL import Image, ImageDraw, ImageFont
import string,random
# https://github.com/Yixiaohan/show-me-the-code


def add_num(img):

    draw = ImageDraw.ImageDraw(img)
    myfont = ImageFont.truetype('/System/Library/Fonts/Keyboard.ttf', size=30)
    fillcolor = '#f0ffff'
    width, height = img.size
    draw.paste(fillcolor,box=None,mask=None)
    # draw.text((width - 20, 0), '3', font=myfont, fill=fillcolor)
    img.save('/Users/00301953/Desktop/result.jpg', 'jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('/Users/00301953/Desktop/hyf.jpeg')
    add_num(image)
