import cv2
import numpy as np
import os
import statistics
import math


def copy_compression(input_file, output_dir):
    segmentSize = 8
    threashold = 1
    img = cv2.imread(input_file)
    blurMap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurMap = cv2.Laplacian(blurMap, cv2.CV_64F)
    stdev = statistics.stdev(np.nditer(blurMap))
    med = statistics.median(np.nditer(blurMap))
    segWidth = math.ceil(img.shape[0] / segmentSize)
    segHeight = math.ceil(img.shape[1] / segmentSize)
    for h in range(segHeight):
        for w in range(segWidth):
            hMax = (h+1)*segmentSize if (h != segHeight-1) else img.shape[1]
            wMax = (w+1)*segmentSize if (w != segWidth-1) else img.shape[0]
            segMed = statistics.stdev(np.nditer(blurMap[h*segmentSize:hMax, w*segmentSize:wMax]))
            if(math.abs(segMed - med) / stdev > threashold):
                img[h*segmentSize:hMax, w*segmentSize:wMax] = (0, 0, 0)
    img.imwrite(os.path.join(output_dir, os.path.split(input_file)[1]))

def copy_decompression(input_file, output_dir):
    img = cv2.imread(input_file)
    img.imwrite(os.path.join(output_dir, os.path.split(input_file)[1]))

