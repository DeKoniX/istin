#!/bin/python
# -*- coding: utf-8 -*-
# DeKoniX =^_^= 2013
import istin

class ravn:
    def __init__(self):
        import istin
        self.form = ""

    def __call__(self, a):
        print "Добавлена функция: ", a
        if self.form == "":
            self.form += "("+a+")"
        else:
            self.form += "~("+a+")"

    def go(self):
        bol = True
        gg = ""
        gg = istin.istin(self.form)
        gg = gg.otv[-1]
        print "####"
        print ">", self.form, "<"

        for i in range(len(gg)):
            if gg[i] != 1:
                bol = False

        if bol:
            print self.form, " равносильна"
        else:
            print self.form, " не равносильна"


#r = ravn()

#r("A")
#r("A|(B&-B)")

#r.go()
