##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the compression algorithm                 #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################

def png_compression(input_file, output_dir):
    from PIL import Image

    img = Image.open(input_file)
    output_name = input_file.split("\\")[-1].split(".")[0]+".png"
    img.save(output_dir+output_name)



if(__name__ == "__main__"):
    png_compression("input\\david_ram_ranch.bmp","output\\")

