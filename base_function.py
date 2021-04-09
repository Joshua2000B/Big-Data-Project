##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the compression algorithm                 #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################


def example_compression(input_file, output_dir):

    # Pretend this is a compressed image file we just generated
    file = open(output_dir+input_file.split("/")[-1],'w')
    file.write("1")
    file.close()



    
##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the decompression algorithm               #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################



def example_decompression(input_file, output_dir):

    # Pretend this is a compressed image file we just generated
    file = open(output_dir+input_file.split("/")[-1],'w')
    file.write("11")
    file.close()
