from PIL import Image
import os

dir = input("Enter input dir: ")
output = input("Enter output dir: ")

for filename in os.listdir(dir):
    img = Image.open(dir+"\\"+filename)
    img.save(output+"\\"+filename.split(".")[0]+".bmp")
