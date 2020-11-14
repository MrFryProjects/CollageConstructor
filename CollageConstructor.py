from PIL import Image
import glob
import math

filePath = '\\Desktop\\'
downloadPath = '\\Desktop\\steamIcons\\'

def imageLine():
    x = glob.glob(downloadPath+'*.jpg')
    print(len(x))
    a = (int(math.floor(len(x)/120)))
    b = (int(len(x)%120))
    for n in range(a):
        x_offset = 0
        images = []
        lineImage = Image.new('RGB', (120*32, 32))
        for i in range(120):
            images.append(Image.open(x.pop(0)))
        for j in images:
            lineImage.paste(j, (x_offset,0))
            x_offset += j.size[0]
        lineImage.save(filePath+'inc\\_'+str(n)+'_incremental.jpg')
    x_offset = 0
    images = []
    lineImage = Image.new('RGB', (b*32, 32))
    for i in range(b):
        images.append(Image.open(x.pop(0)))
        print(len(x))
    for j in images:
        lineImage.paste(j, (x_offset,0))
        x_offset += j.size[0]
        print(len(x))
    lineImage.save(filePath+'inc\\_'+str(a)+'_incremental.jpg')

#def lineStack():
#    y = glob.glob(filePath+'inc\\'+'*_incremental.jpg')
#    print(y)
#    stackImage = Image.new('RGB', (120*32, len(y)*32))
#    images = []
#    y_offset = 0
#    for i in range(len(y)):
#        images.append(Image.open(y.pop(0)))
#        print(len(y))
#    for i in images:
#        stackImage.paste(i, (0,y_offset))
#        y_offset += 32
#    stackImage.save(filePath+'inc\\Collage.jpg')

def stackStack(number):
    y = glob.glob(filePath+'inc\\'+str(number)+'\\'+'*_incremental.jpg')
    print(len(y))
    stackImage = Image.new('RGB', (120*32, len(y)*32))
    images = []
    y_offset = 0
    for i in range(len(y)):
        images.append(Image.open(y.pop(0)))
        print(len(y))
    for i in images:
        stackImage.paste(i, (0,y_offset))
        y_offset += 32
    stackImage.save(filePath+'inc\\'+str(number)+'.jpg')

def collage():
    z = glob.glob(filePath+'inc\\'+'*.jpg')
    images = [Image.open(i) for i in z]
    widths, heights = zip(*(j.size for j in images))
    cImage = Image.new('RGB', (max(widths), sum(heights)))
    y_offset = 0
    count = 0
    for n in images:
        cImage.paste(n, (0,y_offset))
        y_offset += heights[count]
        count += 1
    cImage.save(filePath+'inc\\Collage.jpg')

#imageLine()
#for i in range(5):
#    stackStack(i)

collage()