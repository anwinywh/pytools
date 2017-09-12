#encoding:utf-8

import csv

from Config import Config

dstFile = Config.PROJECT_DIR + "/src/com/dfh3/App/Config/ConfigField.ts"

class ConfigMaker:

    def __init__(self):
        self.m_pText = "module dfh3 {\n"
        self.m_pText += "   export class ConfigField {\n"
        self.m_pText += "       private static _instance: ConfigField;\n"
        self.m_pText += "       public static getInstance() {\n"
        self.m_pText += "           if( ! ConfigField._instance ) {\n"
        self.m_pText += "               ConfigField._instance = new ConfigField();\n"
        self.m_pText += "           }\n"
        self.m_pText += "           return ConfigField._instance;\n"
        self.m_pText += "       }\n"
        self.m_pText += "       private m_pFieldNames: Array<any>[];\n"
        self.m_pText += "       public constructor() {\n"
        self.m_pText += "           this.m_pFieldNames = new Array();\n"


    def addFile(self, path, fileName):

        csvReader = csv.reader(open(path, 'rb'))

        pTableName = fileName.replace(".csv", "")

        text = "           this.m_pFieldNames[\"" + pTableName + "\"] = [";

        isFirst = True
        for row in csvReader:
            for item in row:
                if item.find(":") != -1:
                    field,t = item.split(":")
                else:
                    field = item

                if not isFirst:
                    text += ", "
                isFirst = False
                text += '"'+ field +'"'
            break

        text += "];\n"

        self.m_pText += text


    def end(self):
        self.m_pText += "       }\n"
        self.m_pText += "       public getFieldName(name:string) {\n"
        self.m_pText += "            return this.m_pFieldNames[name];\n"
        self.m_pText += "       }\n"
        self.m_pText += "   }\n"
        self.m_pText += "}\n"

    def output(self):
        print self.m_pText

        writeFile = open(dstFile, 'w')
        writeFile.write(self.m_pText)
        writeFile.close()






