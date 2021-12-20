############################################################
# File Selector                                            #
# up : pass, left : move, right : delete end : exit        #
# Example                                                  #
# python fileSelector.py --dir ./ --type image --to ./dir  #
############################################################

import glob
import os
import shutil
import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--dir", default="./")
parser.add_argument("--type", default = "*", help="image or file")
parser.add_argument("--to", required=True)
args = parser.parse_args()

print("################################################################")
print("#                                                              #")
print("#    down : pass, left : move, right : delete,  end : exit     #")
print("#                                                              #")
print("################################################################")

def dealing(content, isImage = False):
    title = "title"
    if isImage:
        cv2.imshow(title, content)
        cv2.moveWindow(winname=title, x=200, y=200)
        cv2.resizeWindow(winname=title, width=800, height=600)
    else:
        canvas = np.full((100, 200, 3), (255, 255, 100), np.uint8)
        cv2.putText(canvas, content, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.imshow(title, canvas)
    flag = False
    while True:
        key = cv2.waitKeyEx()
        # left arrow : move
        if key == 0x250000:
            fname = os.path.join(args.to, file.split("\\")[-1])
            print(fname)
            if not os.path.isfile(fname):
                shutil.move(file, fname)
            break
        # right arrow : delete
        elif key == 0x270000:
            os.remove(file)
            break
        # up arrow : pass
        elif key == 0x280000:
            break
        # end : Exit Program
        elif key == 0x230000:
            flag = True
            break
        else:
            print("Unvalid Input")
    if flag:
        return True

files = glob.glob(args.dir+"/*")

cnt =  1
total = len(files)
if args.type == "image":
    for file in files:
        print(file,"    ", cnt, "  /  ", total)
        cnt += 1
        img = cv2.imread(file)
        try:
            dst = cv2.resize(img, dsize=(800, 600), interpolation=cv2.INTER_CUBIC)
        except:
            continue
        endFlag = dealing(dst, True)
        if endFlag:
            break

elif args.type == "file":
    for file in files:
        f = dealing(file, False)
        if f:
            break
else:
    print("Unvalid Parameter, --type = image or file")
    exit(0)
