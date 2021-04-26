from img_copy import *
from png import *
from jpg import *
from inflate_deflate import *
from down_sample import *
from blur_sensitive import *
from rle import *

import os
import time
import hashlib

import random

import pymysql



#input_dir = "C:\\Users\\Joshu\\Desktop\\Big-Data-Project\\img\\rabbit\\"
input_dir = "C:\\Users\\Joshu\\Desktop\\Big-Data-Project\\img\\demo\\"
output_dir = "output\\"

conn = pymysql.connect(host = "localhost", port=3306,user="Joshua",password="BigData",db="bigdata")

handler = conn.cursor()

for filename in os.listdir(input_dir):
    print(filename)

    random.seed(filename)
    id = random.randint(0,2**32)

    #COPY
    start = time.time()
    copy_compression(input_dir+filename,output_dir)
    elapsed = time.time()-start
    data = open(output_dir+"copy_"+filename,'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/copy_"+filename
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="copy",file_type="bmp",data=dir,num=len(data),time=elapsed)
    #print(x)
    handler.execute(x)
    print("copy done:",elapsed)

    #PNG
    start = time.time()
    png_compression(input_dir+filename,output_dir)
    elapsed = time.time()-start
    data = open(output_dir+"\\"+filename.split(".")[0]+".png",'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/"+filename.split(".")[0]+".png"
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="png",file_type="png",data=dir,num=len(data),time=elapsed)
    handler.execute(x)
    print("png done:",elapsed)

    #JPG
    start = time.time()
    jpg_compression(input_dir+filename,output_dir)
    elapsed = time.time()-start
    data = open(output_dir+""+filename.split(".")[0]+".jpg",'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/"+filename.split(".")[0]+".jpg"
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="jpg",file_type="jpg",data=dir,num=len(data),time=elapsed)
    handler.execute(x)
    print("jpg done:",elapsed)

    #Inflate/Deflate
    start = time.time()
    inflate_compression(input_dir+filename,output_dir)
    elapsed = time.time()-start
    data = open(output_dir+"\\"+filename.split(".")[0]+".gz",'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/"+filename.split(".")[0]+".gz"
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="inflate/deflate",file_type="gz",data=dir,num=len(data),time=elapsed)
    handler.execute(x)
    print("deflate done:",elapsed)

    #Down sample
    start = time.time()
    down_sample_compression(input_dir+filename,output_dir)
    elapsed = time.time()-start
    data = open(output_dir+"compressed_"+filename,'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/compressed_"+filename
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="down_sample",file_type="gz",data=dir,num=len(data),time=elapsed)
    handler.execute(x)
    print("down sample done:",elapsed)

    #Blur
    start = time.time()
    blur_compression(output_dir+filename.split(".")[0]+".png",output_dir)
    elapsed = time.time()-start
    data = open(output_dir+"blur_"+filename.split(".")[0]+".png",'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/blur_"+filename.split(".")[0]+".png"
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="blur",file_type="png",data=dir,num=len(data),time=elapsed)
    handler.execute(x)
    print("blur done:",elapsed)

    #RLE
    start = time.time()
    rle_compression(output_dir+filename.split(".")[0]+".png",output_dir)
    elapsed = time.time()-start
    data = open(output_dir+"rle_"+filename.split(".")[0]+".png",'rb').read()
    dir = "C:/Users/Joshu/Desktop/Big-Data-Project/output/rle_"+filename.split(".")[0]+".png"
    x = "INSERT INTO image(id,compression_type,file_type,img_data_path,num_bytes,time_elapsed) VALUES({id},'{comp_type}','{file_type}','{data}',{num},{time})".format(id=id,comp_type="rle",file_type="png",data=dir,num=len(data),time=elapsed)
    handler.execute(x)
    print("rle done:",elapsed)
    
handler.execute("COMMIT")  
