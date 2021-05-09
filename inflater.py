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


inf_data = getData("inflate/deflate")

for x in range(len(inf_data)):
    inflate_decompression(inf_data[x][4],"output/")
    #inf = Image.open("output/inflated_"+inf_data[x][4].split("/")[-1].split(".")[0]+".bmp")
