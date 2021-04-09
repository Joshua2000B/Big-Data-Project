from rle import RLEBitmap

##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the compression algorithm                 #
# It should take in the path to the input file and the output file location  #
# Takes .png and converts to .rle                                            #
#                                                                            #
##############################################################################

def example_compression(input_file, output_dir):
    rle = RLEBitmap()
    rle.open_png(input_file)
    file = open(output_dir+input_file.split("/")[-1].split('.')[0]+".rle",'w')
    # Pretend this is a compressed image file we just generated
    rle.write_rle_tostream(file)
    file.close()
    
##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the decompression algorithm               #
# It should take in the path to the input file and the output file location  #
# Opens .rle file and converts back to .png                                  #
#                                                                            #
##############################################################################



def example_decompression(input_file, output_dir):

    rle = RLEBitmap()
    fs = open(input_file, 'r')
    rle.read_rle_fromstream(fs)
    fs.close()
    rle.write_memory_tofile(output_dir+input_file.split("/")[-1].split('.')[0]+".png")
