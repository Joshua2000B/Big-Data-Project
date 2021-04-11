import cv2
import numpy as np
import os
import math

def blur_compression(input_file, output_dir, segmentSize=16, threashold=1):
    '''Will only work if given png / jpgs. Relies on their compression to do the compressing
    segmentSize (int) - pixle size of squares to check
    threashold (float) - the difference of varience from image adverage to clear, lower is more sensitive.
    '''
    img = cv2.imread(input_file)
    blurMap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurMap = cv2.Laplacian(blurMap, cv2.CV_64F)
    vari = blurMap.var()
    segWidth = math.ceil(img.shape[1] / segmentSize)
    segHeight = math.ceil(img.shape[0] / segmentSize)
    print(vari)
    for h in range(segHeight):
        for w in range(segWidth):
            hMax = (h+1)*segmentSize if (h != segHeight-1) else img.shape[0]
            wMax = (w+1)*segmentSize if (w != segWidth-1) else img.shape[1]
            segMed = np.std(blurMap[h*segmentSize:hMax, w*segmentSize:wMax])
            if(blurMap[h*segmentSize:hMax, w*segmentSize:wMax].var() - vari < threashold):
                img[h*segmentSize:hMax, w*segmentSize:wMax] = np.average(np.average(img[h*segmentSize:hMax, w*segmentSize:wMax], axis=0), axis=0)
            blurMap[h*segmentSize:hMax, w*segmentSize:wMax] = blurMap[h*segmentSize:hMax, w*segmentSize:wMax].var()
    cv2.imwrite(os.path.join(output_dir, os.path.split(input_file)[1]), img)
    cv2.imwrite(os.path.join(output_dir, "laplace" + (os.path.split(input_file)[1])), blurMap)
