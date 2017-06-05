#!/usr/bin/python
# -*- coding: latin-1 -*-
# Python2.7
#使用本脚本前请安装hashlib库， 在终端执行：pip install hashlib

import os,sys
import os.path
import hashlib 

filePath = raw_input('please input the path:') #输入文件夹路径
filePath = filePath.strip()
imagePathPool = () #创建图片路径储蓄池 ， 元组类型
duplicateImagePool = () #创建重复图片路径储蓄池

def compare_images(path_one, path_two) :
    image_one = open(path_one,"r").read()
    image_two = open(path_two, "r").read()
    hash_one = hashlib.md5(image_one).hexdigest()
    hash_two = hashlib.md5(image_two).hexdigest()
    global duplicateImagePool
    global imagePathPool
    if hash_one == hash_two:
        duplicateImagePool += (path_two,)
        duplicateImagePool = tuple( set(duplicateImagePool) )

#遍历项目文件树，找出所有图片路径
for parent,dirnames,filenames in os.walk(filePath): 
    for filename in filenames:    
        # print("parent folder is:" + parent) 
        # print("filename with full path:"+ os.path.join(parent,filename))
        imagePath = os.path.join(parent,filename)
        sufixStr = os.path.splitext(filename)[1][1:]
        if sufixStr == 'pdf' or sufixStr == 'png' or sufixStr == 'jpg' :
            imagePathPool += (imagePath,)  #已遍历项目中所有图片的文件路径，并添加到元组中

#开始遍历比较图片是否有重复
print("------------- wait -------------")
for path in imagePathPool:
    # print("path ===" +path)
    for originPath in imagePathPool:
        # print("originPath === " + originPath)
        if path != originPath:
            compare_images(originPath, path)

#输出重复图片路径
print(" ------------- end -------------")
if len(duplicateImagePool) :
    for dump in duplicateImagePool:
        print(dump)
else :
    print("无重复图片")







