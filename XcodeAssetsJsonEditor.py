#!/usr/bin/python
# -*- coding: latin-1 -*-
import os,sys
import os.path
import string
import json

def changeJsonFileContents(filePath):
    try:
        file = open(filePath)
        content = file.read()
        dictionary = json.loads(content)
        images = dictionary["images"]
        replace_image = []
        for element in images:
          if "filename" in element:
            if "scale" in element:
              del element["scale"]
            replace_image = [element,]
            dictionary["images"] = replace_image
            json_str = json.dumps(dictionary,sort_keys=False,indent =2,separators=(',',' : '),encoding="gbk",ensure_ascii=True )
            temp = open(filePath,'w')
            temp.write(json_str)
    finally:
        file.close()

projectPath = raw_input('please input the project path:')
projectPath = projectPath.strip()

print("---------- Changing ----------")
for parent,dirnames,filenames in os.walk(projectPath):  #parent:父目录 2.所有文件夹名字 3：所有文件名字
    for filename in filenames:    
        imagePath = os.path.join(parent,filename)
        sufixStr = os.path.splitext(filename)[1][1:] #文件后缀
        if sufixStr == 'pdf' and 'Contents.json' in filenames:
          jsonPath = parent + "/Contents.json"
          changeJsonFileContents(jsonPath)

print("----------- Finish -----------")






