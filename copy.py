##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the compression algorithm                 #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################


def copy_compression(input_file, output_dir):

    file.open(input_file,'rb')
    data = file.read()
    file.close()

    output_file = "copy_"+input_file.split("\\")[-1]

    # Pretend this is a compressed image file we just generated
    file = open(output_dir+input_file.split("/")[-1],'wb')
    file.write(data)
    file.close()


