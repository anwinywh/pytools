#encoding:utf-8
import os
import os.path

import sys

sys.path.append("libs")

from Config import Config

print "工程目录:", Config.PROJECT_DIR

dstFile = Config.PROJECT_DIR + "/resource/proto/game.proto"

print Config.PROBUF_DIR

writeFile = open(dstFile, 'w')

def readFile(fp):
    # print fp
    rf = open(fp, 'r')

    line = rf.readline()
    while line:
        if line.find("package ") != -1 or line.find("option java") != -1 or line.find("option opti") != -1 or line.find("import ") != -1:
            line = rf.readline()
            continue
        # if line == "\r\n":
        #     line = rf.readline()
        #     continue

        if fp == "/Users/yaowan/liyan/yaowan/protocol/trunk/protoFiles/trade.proto":
            print line

        writeFile.write(line)
        line = rf.readline()

    rf.close()


for root, dirs, files in os.walk(Config.PROBUF_DIR):

    for f in files:
        fp  = os.path.join(root, f)

        if fp.find(".DS_Store") != -1 or fp.find("/center") != -1 or fp.find("\center") != -1:
            continue
        readFile(fp)

print "make success"