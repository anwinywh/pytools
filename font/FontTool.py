#encoding:utf-8

import re
import os
import os.path

class FontTool:

    def __init__(self):
        pass

    def parseFile(self, srcFile, dstFile):

        rf = open(srcFile, 'r')

        line = rf.readline()

        allText = ""

        while line:
            text = self.parse(line)
            allText += text
            line = rf.readline()

        rf.close()

        writeFile = open(dstFile, 'w')
        writeFile.write(allText)
        writeFile.close()


    def parse(self, text):
        # text = self.parseFontSize(text)

        # text = self.parseFloat(text)

        # text = self.parseDfh3(text)
        # text = self.parseLabel(text)
        # text = self.parseEditableText(text)
        # text = self.parseComponent(text)

        text = self.clearFontLabel(text)
        text = self.clearEditText(text)

        return text

    def parseFontSize(self, text):

        regStr = "(.*? size=\")(.*?)(\"[\s\S]*)"

        matchObj = re.search(regStr, text)

        if matchObj:
            size = int(matchObj.group(2))
            if size == 14 or size == 16:
                size = size - 2
            text = matchObj.group(1) + str(size) + matchObj.group(3)

        return text

    def parseFloatByKey(self, key, text):

        regStr = "(.*? " + key +"=\")(.*?)(\"[\s\S]*)"

        matchObj = re.search(regStr, text)

        if matchObj:
            group2 = matchObj.group(2)
            if group2.find("%") != -1:
                return text
            val = float(matchObj.group(2))
            rval = round(val)
            if val != rval:
                rval = int(rval);
                print key, val, rval
                text = matchObj.group(1) + str(int(rval)) + matchObj.group(3)

        return text

    def parseFloat(self, text):  #解析小数点

        text = self.parseFloatByKey("x", text)
        text = self.parseFloatByKey("y", text)
        text = self.parseFloatByKey("width", text)
        text = self.parseFloatByKey("height", text)
        text = self.parseFloatByKey("horizontalCenter", text)
        text = self.parseFloatByKey("verticalCenter", text)
        text = self.parseFloatByKey("left", text)
        text = self.parseFloatByKey("right", text)
        text = self.parseFloatByKey("top", text)
        text = self.parseFloatByKey("bottom", text)
        text = self.parseFloatByKey("anchorOffsetX", text)
        text = self.parseFloatByKey("anchorOffsetY", text)

        return text

    def parseDfh3(self, text):

        matchObj = re.search("(.*?<e:Skin.*?)(>[\s\S]*)", text)

        if matchObj:
            match = re.search("(.*?<e:Skin.*?)xmlns:dfh3=\"dfh3.*\"(.*?>[\s\S]*)", text)

            if not match:
                text = matchObj.group(1) + ' xmlns:dfh3="dfh3.*"' + matchObj.group(2)

        return text


    def clearFontLabel(self, text):
        matchObj = re.search("(.*?<e:Label.*?)fontFamily=\"(.*?)\"(.*?/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + matchObj.group(3)
        else:
            matchObj = re.search("(.*?)(<e:Label)(.*?)(/>)([\s\S]*)", text)
            if matchObj:
                text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + matchObj.group(4) + matchObj.group(5)

        matchObj = re.search("(.*?)(<e:Label)(.*?)( bold=\"true\")(.*?\/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + matchObj.group(5)
        return text


    def clearEditText(self, text):
        matchObj = re.search("(.*?<e:EditableText.*?)fontFamily=\"(.*?)\"(.*?/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + matchObj.group(3)
        else:
            matchObj = re.search("(.*?)(<e:EditableText)(.*?)(/>)([\s\S]*)", text)
            if matchObj:
                text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + matchObj.group(4) + matchObj.group(5)

        matchObj = re.search("(.*?)(<e:EditableText)(.*?)( bold=\"true\")(.*?\/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + matchObj.group(5)

        return text


    def parseLabel(self, text):
        matchObj = re.search("(.*?<e:Label.*?)fontFamily=\"(.*?)\"(.*?/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + "fontFamily=\"dfh3Font\"" + matchObj.group(3)
        else:
            matchObj = re.search("(.*?)(<e:Label)(.*?)(/>)([\s\S]*)", text)
            if matchObj:
                text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + " fontFamily=\"dfh3Font\"" + matchObj.group(4) + matchObj.group(5)

        matchObj = re.search("(.*?)(<e:Label)(.*?)( bold=\"true\")(.*?\/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + matchObj.group(5)

        return text

    def parseEditableText(self, text):

        matchObj = re.search("(.*?<e:EditableText.*?)fontFamily=\"(.*?)\"(.*?/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + "fontFamily=\"dfh3Font\"" + matchObj.group(3)
        else:
            matchObj = re.search("(.*?)(<e:EditableText)(.*?)(/>)([\s\S]*)", text)
            if matchObj:
                text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + " fontFamily=\"dfh3Font\"" + matchObj.group(4) + matchObj.group(5)

        matchObj = re.search("(.*?)(<e:EditableText)(.*?)( bold=\"true\")(.*?\/>[\s\S]*)", text)
        if matchObj:
            text = matchObj.group(1) + matchObj.group(2) + matchObj.group(3) + matchObj.group(5)

        return text


    def parseComponent(self, text):

        matchObj = re.search("(.*?<)(e:Component)(.*?.*?/>[\s\S]*)", text)

        if matchObj:
            text = matchObj.group(1) + "dfh3:CComponent" + matchObj.group(3)

        return text

