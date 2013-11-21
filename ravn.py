#!/bin/python
# -*- coding: utf-8 -*-
# DeKoniX =^_^= 2013

class ravn:
    def __init__(self, a, b):
        import istin

        ai = istin.istin(a)
        bi = istin.istin(b)

        ai = ai.otv[-1]
        bi = bi.otv[-1]

        print "#####"
        print a, " = ", ai
        print b, " = ", bi
        if ai == bi:
            print "Формулы: ", a, " и ", b, " равносильны"
        else:
            print "Формулы: ", a, " и ", b, " не равносильны"

#ravn("A&B", "B&A")
ravn("(A&(B|C))","((A&B)|(A&C))")
