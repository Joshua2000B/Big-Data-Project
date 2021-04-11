

def copy_compression(input_file, output_dir):
    file = open(input_file,'rb')
    data = file.read()
    file.close()

    output_file = "copy_"+input_file.split("\\")[-1]
    file = open(output_dir+output_file,'wb')
    file.write(data)
    file.close()


