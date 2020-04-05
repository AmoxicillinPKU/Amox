#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------Code modification log---------------
# 1.2020/04/03 - Create
# 2.Python version: v3.6
# ------------------------------------------

class A(object):
    def __init__(self):
        print("->Enter A")
        print("<-Leave A")

class B(A):
    def __init__(self):
        print("->Enter B")
        A.__init__(self)
        print("<-Leave B")

class C(A):
    def __init__(self):
        print("->Enter C")
        A.__init__(self)
        print("<-Leave C")

class D(B,C):
    def __init__(self):
        print("->Enter D")
        B.__init__(self)
        C.__init__(self)
        print("<-Leave D")

d = D()