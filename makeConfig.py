#encoding:utf-8

import sys
import os
import os.path
sys.path.append("libs")

from Config import Config
from ConfigMaker import ConfigMaker

def isCsv(pFileName):
    #过滤svn
    if pFileName.find("svn") != -1 or pFileName.find(".meta") != -1:
        return False
    imgSuffixs = [".csv"]
    for str in imgSuffixs:
        index = pFileName.find(str)
        if index != -1:
            return True
    return False

pConfigMaker = ConfigMaker()

for root, dirs, files in os.walk(Config.CSV_DIR):
    for f in files:
        fp = os.path.join(root, f)
        dstFp = os.path.join(root, f)

        if not isCsv(f):
            continue
        pConfigMaker.addFile(fp, f)

pConfigMaker.end()
pConfigMaker.output()