"""
Day 15
图像
"""

from PIL import Image

def image_test():
    img = Image.open('./res/ball.png')
    print(img.size)
    print(img.format)
    print(img.format_description)
    img.save('./res/ball.png')

    img2 = Image.open('./res/ball.png')
    img3 = img2.crop((5, 5, 35, 35))
    for x in range(4):
        for y in range(5):
            img2.paste(img3, (95 * y, 180 * x))
    img2.resize((img.size[0] // 2, img.size[1] // 2))
    img2.rotate(90)
    img2.save('./res/ball-2.png')

if __name__ == '__main__':
    image_test()