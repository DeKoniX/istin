#!/bin/python
# -*- coding: utf-8 -*-

#str = "(1->2)&(3<->1)"
#stro = "1&2~3||-4"
#stro = "1&2~3"
#stro = "(A|C&-B)&(A|C)"
#stro = "A|C&-B"
m = []
znak = ('&', '|')
stro = "A&B|C"

class istin:
    def __init__(self, stro):
        #stroki = pow(2, len(self.simbol(stro)))
        m = self.massstrok(stro)
        for s in stro:
            if s == "-":
                stro,  = otric()


    def simbol(self, stro):
        for i in stro:
            est = False
            for z in znak:
                if i == z:
                    est = True
            for j in m:
                if j == i:
                    est = True
            if est == False:
                m.append(i)
        return m

    def massstrok(self, stro):
        mass = []
        j = 0
        m = self.simbol(stro)
        d = pow(2, len(m))
        t = d
        for z in m:
            mass.append([z])
            t = t/2
            tt = 0
            for i in range(1, d+1):
                tt += 1
                if tt<=t:
                    mass[j].append(0)
                elif tt>t:
                    mass[j].append(1)
                    if tt == t*2:
                        tt=0
            #for i in range(0, d):
                #print "><"+str(i)
                #for nu in range(0, d):
                    #mass[j].append(0)
                #for nu in range(0, d):
                    #mass[j].append(1)
                #if i <= d:
                    #mass[j].append(0)
                #else:
                    #mass[j].append(1)
            j+=1
        return mass


        # k - количество символов
        #k = len(stro)
        #for i in range(0, len(znak)-1):
            #if stro.find(znak[i]) != -1:
                #k-=1
        #self.go(stro, k)

    #def go(self, stro, k):
        #print stro
        #print k

        #for i in range(0, len(stro)):
            #m.append(stro[i])

istin(stro)
