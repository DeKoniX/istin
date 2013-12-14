#!/bin/python

import istin

class skdnf:
    def __init__(self, stro):
        self.sknf = ""
        self.sdnf = ""
        otv = ""
        otv = istin.istin(stro)
        mass = otv.massstr
        gg = otv.otv[-1]
        self.go(gg, mass)

    def go(self, otv, mass):
        for i in range(len(otv)):
            if otv[i] == 0:
                if self.sknf == "":
                    self.sknf = "("+self.skdnf(i, otv, mass)+")"
                else:
                    self.sknf += "&("+self.skdnf(i, otv, mass)+")"
            else:
                if self.sdnf == "":
                    self.sdnf = "("+self.skdnf(i, otv, mass)+")"
                else:
                    self.sdnf += "|("+self.skdnf(i, otv, mass)+")"

        print "SKNF: "+self.sknf
        print "SDNF: "+self.sdnf

    def skdnf(self, i, otv, mass):
        stro = ""
        if otv[i] == 0:
            for j in mass:
                if j[i+1] == 0:
                    if stro == "":
                        stro = j[0]
                    else:
                        stro += "|"+j[0]
                else:
                    if stro == "":
                        stro = "-"+j[0]
                    else:
                        stro += "|"+"-"+j[0]
        else:
            for j in mass:
                if j[i+1] == 0:
                    if stro == "":
                        stro = "-"+j[0]
                    else:
                        stro += "&-"+j[0]
                else:
                    if stro == "":
                        stro = j[0]
                    else:
                        stro += "&"+j[0]
        return stro

#skdnf("x&y|z")
