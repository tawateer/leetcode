#!/bin/env python
# -*- coding:utf-8 -*-

"""
变量名替换

给一些驼峰式的变量名，将它们转换为下划线式的，要求及说明如下：

输入数据一定为合法的“驼峰式”变量名，变量名由若干单词组成，单词应当为首字母大写，或全大写，或全小写。
如"Variable", "oneVariable”, "OneHTTPRequest"。
输出数据应当为合法的“下划线式”变量名，变量名由若干单词组成，单词应当为全小写，相邻单词之间以单个下划线连接。
如"variable", "one_variable", "one_http_request”。

"""

def replace_var(str):
    if len(str) == 0:
        return ""

    res = ""
    pre = True

    for i in range(len(str)):
        if str[i].isupper():
            if 0<i<len(str)-2 and str[i+1].islower():
                res += "_" + str[i].lower()
            elif not pre:
                res += "_" + str[i].lower()
            else:
                res += str[i].lower()
            pre = True
        else:
            res += str[i]
            pre = False

    return res


print replace_var("Variable")
print replace_var("oneVariable")
print replace_var("OneHTTPRequest")
print replace_var("HTTPRequest")
