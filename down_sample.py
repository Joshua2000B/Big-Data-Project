

##############################################################################
#                                                                            #
#                                                                            #
# Follow this example for creating the compression algorithm                 #
# It should take in the path to the input file and the output file location  #
#                                                                            #
#                                                                            #
##############################################################################


def pixelAverage(pixels, x, y):
    tl = pixels[2*x, 2*y] # Top Left
    tr = pixels[2*x+1, 2*y] # Top Right
    bl = pixels[2*x, 2*y+1] # Bot Left
    br = pixels[2*x+1, 2*y+1] # Bot Right

    if(type(tl) == int):
        r = g = b = int((tl + tr + bl + br)/4)
        return r
    elif len(tl) == 3: #RGB
        r = int((tl[0] + tr[0] + bl[0] + br[0])/4)
        g = int((tl[1] + tr[1] + bl[1] + br[1])/4)
        b = int((tl[2] + tr[2] + bl[2] + br[2])/4)
        return (r, g, b)
    else: # RGBA
        r = int((tl[0] + tr[0] + bl[0] + br[0])/4)
        g = int((tl[1] + tr[1] + bl[1] + br[1])/4)
        b = int((tl[2] + tr[2] + bl[2] + br[2])/4)
        a = int((tl[3] + tr[3] + bl[3] + br[3])/4)
        return (r, g, b, a)

def down_sample_compression(input_file, output_dir):
    from PIL import Image
    
    image = Image.open(input_file)
    width, height = image.size
    pixels = image.load()

    cImage = Image.new(mode = image.mode, size = (int(width/2), int(height/2)))
    cWidth, cHeight = cImage.size
    cPixels = cImage.load()

    for x in range(cWidth):
        for y in range(cHeight):
            cPixels[x, y] = pixelAverage(pixels, x, y)
            # print(pixelAverage(pixels, x, y))

    cImage.save(output_dir+"compressed_"+input_file.split("\\")[-1])
