#encoding:utf-8

import os
import os.path
import re
import sys

sys.path.append("tool")

from FontTool import FontTool

fontTool = FontTool()

srcDir = "/Users/yaowan/liyan/yaowan/qmdfh/h5/dfh3/resource/skin"
# srcDir = "/Users/yaowan/Desktop/skinTest"

def isExml(pFileName):
    #过滤svn
    if pFileName.find("svn") != -1 or pFileName.find(".meta") != -1 or pFileName.find(".DS_Store") != -1:
        return False
    imgSuffixs = [".exml"]
    for str in imgSuffixs:
        index = pFileName.find(str)
        if index != -1:
            return True
    return False

isBreak = False

print srcDir

for root, dirs, files in os.walk(srcDir):
    for f in files:
        fp = os.path.join(root, f)
        dstFp = os.path.join(root, f)

        if not isExml(f):
            continue

        isBreak = True

        text = fontTool.parseFile(fp, dstFp)

    # if isBreak:
    #     break




