# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 15:14
# @Author  : if
# @File    : test.py
# @Software: PyCharm
def say(e,f,g=2,*args,**kwargs):
    a=args
    b=kwargs
    print(a,b,e,f,g)
say(1,2,3,b={1,2,3,4,5})