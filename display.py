import pymysql

from PIL import Image

from inflate_deflate import *

conn = pymysql.connect(host = "localhost", port=3306,user="Joshua",password="BigData",db="bigdata")

handler = conn.cursor()

def getData(alg):
    x = """
SELECT * FROM image WHERE compression_type = "{0}" ORDER BY id ASC
""".format(alg)
    handler.execute(x)
    return handler.fetchall()

def compareImage(img1,img2):
    if(img1.size == img2.size):
        counter = 0
        x,y = img1.size
        pix1 = img1.load()
        pix2 = img2.load()
        for i in range(x):
            for j in range(y):
                if(pix1[i,j] == pix2[i,j]):
                    counter += 1
                else:
                    #Red
                    if(pix1[i,j][0] == pix2[i,j][0]):
                        counter += 1/3
                    else:
                        counter += (1/3)*(1-(abs(pix1[i,j][0] - pix2[i,j][0])/255))
                    #Green
                    if(pix1[i,j][1] == pix2[i,j][1]):
                        counter += 1/3
                    else:
                        counter += (1/3)*(1-(abs(pix1[i,j][1] - pix2[i,j][1])/255))
                    #Blue
                    if(pix1[i,j][2] == pix2[i,j][2]):
                        counter += 1/3
                    else:
                        counter += (1/3)*(1-(abs(pix1[i,j][2] - pix2[i,j][2])/255))
        return counter / (x * y) * 100
    else:
        x1,y1 = img1.size
        x2,y2 = img2.size
        return (x2*y2) / (x1*y1) * 100


copy_data = getData("copy")
png_data = getData("png")
jpg_data = getData("jpg")
inf_data = getData("inflate/deflate")
down_data = getData("down_sample")
blur_data = getData("blur")
rle_data = getData("rle")


copy_total = png_total = jpg_total = inf_total = down_total = blur_total = rle_total = 0
copy_time = png_time = jpg_time = inf_time = down_time = blur_time = rle_time = 0
png_loss = jpg_loss = inf_loss = down_loss = blur_loss = rle_loss = 0


for x in range(len(copy_data)):
    copy_total += copy_data[x][3]
    png_total += png_data[x][3]
    jpg_total += jpg_data[x][3]
    inf_total += inf_data[x][3]
    down_total += down_data[x][3]
    blur_total += blur_data[x][3]
    rle_total += rle_data[x][3]

    copy_time += copy_data[x][2]
    png_time += png_data[x][2]
    jpg_time += jpg_data[x][2]
    inf_time += inf_data[x][2]
    down_time += down_data[x][2]
    blur_time += blur_data[x][2]
    rle_time += rle_data[x][2]

    copy = Image.open(copy_data[x][4])
    png = Image.open(png_data[x][4])
    jpg = Image.open(jpg_data[x][4])
    inf = Image.open("output/inflated_"+inf_data[x][4].split("/")[-1].split(".")[0]+".bmp")
    down = Image.open(down_data[x][4])
    blur = Image.open(blur_data[x][4])
    rle = Image.open(rle_data[x][4])

    png_loss += compareImage(copy,png)
    jpg_loss += compareImage(copy,jpg)
    inf_loss += compareImage(copy,inf)
    down_loss += compareImage(copy,down)
    blur_loss += compareImage(copy,blur)
    rle_loss += compareImage(copy,rle)

    print(x+1,"/",len(copy_data))
    

copy_time /= len(copy_data)
png_time /= len(copy_data)
jpg_time /= len(copy_data)
inf_time /= len(copy_data)
down_time /= len(copy_data)
blur_time /= len(copy_data)
rle_time /= len(copy_data)

png_loss /= len(copy_data)
jpg_loss /= len(copy_data)
inf_loss /= len(copy_data)
down_loss /= len(copy_data)
blur_loss /= len(copy_data)
rle_loss /= len(copy_data)

    
print("RATIO")
print("Copy:",copy_total)
print("PNG:",png_total,str(png_total/copy_total*100)+"%")
print("JPG:",jpg_total,str(jpg_total/copy_total*100)+"%")
print("Inflate/Deflate:",inf_total,str(inf_total/copy_total*100)+"%")
print("Down Sampling:",down_total,str(down_total/copy_total*100)+"%")
print("Blur:",blur_total,str(blur_total/copy_total*100)+"%")
print("RLE:",rle_total,str(rle_total/copy_total*100)+"%")

print("TIME")
print("Copy",copy_time)
print("PNG",png_time)
print("JPG",jpg_time)
print("Inflate/Deflate",inf_time)
print("Down Sampling",down_time)
print("Blur",blur_time)
print("RLE",rle_time)

print("LOSS")
print("Copy 100 % of original")
print("PNG",png_loss,"% of original")
print("JPG",jpg_loss,"% of original")
print("Inflate/Deflate",inf_loss,"% of original")
print("Down Sampling",down_loss,"% of original")
print("Blur",blur_loss,"% of original")
print("RLE",rle_loss,"% of original")
