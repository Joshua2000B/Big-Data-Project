##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the compression algorithm                 #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################


def inflate_compression(input_file, output_dir):
    import zlib
    
    file = open(input_file,'rb')
    data = file.read()
    file.close()

    compressed = zlib.compress(data, zlib.Z_BEST_COMPRESSION)

    compress_ratio = (float(len(data)) - float(len(compressed))) / float(len(data))

    #print('Compressed: %d%%' % (100.0 * compress_ratio))
    
    output_name = input_file.split("\\")[-1].split(".")[0]+".gz"


    # Pretend this is a compressed image file we just generated
    file = open(output_dir+output_name,'wb')
    file.write(compressed)
    file.close()



    
##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the decompression algorithm               #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################



def inflate_decompression(input_file, output_dir):
    import zlib

    compressed = open(input_file,'rb').read()
    data = zlib.decompress(compressed)
    
    output_name = input_file.split("\\")[-1].split(".")[0]+".bmp"

    file = open(output_dir+output_name,'wb')
    file.write(data)
    file.close()

if(__name__ == "__main__"):
    inflate_compression("input\\david_ram_ranch.bmp","output\\")
    inflate_decompression("output\\david_ram_ranch.gz","decompress\\")
