from PIL import Image
import os

def copy_compression(input_file, output_dir):
    img = Image.open(input_file)
    img.save(os.path.join(output_dir, os.path.split(input_file)[1]))

def copy_decompression(input_file, output_dir):
    img = Image.open(input_file)
    img.save(os.path.join(output_dir, os.path.split(input_file)[1]))
