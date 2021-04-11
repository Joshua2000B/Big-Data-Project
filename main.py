from img_copy import *
from png import *
from jpg import *
from inflate_deflate import *

import os
import time

import pymysql

input_dir = "input\\"
output_dir = "output\\"

conn = pymysql.connect(host = "10.0.0.216", port=3306,user="Joshua",password="BigData",db="image")

for filename in os.listdir(input_dir):
    print(filename)
    start = time.time()
    copy_compression(input_dir+filename,output_dir)
    print("copy done:",time.time()-start)
    start = time.time()
    png_compression(input_dir+filename,output_dir)
    print("png done:",time.time()-start)
    start = time.time()
    jpg_compression(input_dir+filename,output_dir)
    print("jpg done:",time.time()-start)
    start = time.time()
    inflate_compression(input_dir+filename,output_dir)
    print("deflate done:",time.time()-start)
    
