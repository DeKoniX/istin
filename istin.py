#!/bin/python
# -*- coding: utf-8 -*-
# DeKoniX =^_^= 2013

#str = "(1->2)&(3<->1)"
#stro = "1&2~3||-4"
#stro = "1&2~3"
#stro = "(A|C&-B)&(A|C)"
#stro = "A|C&-B"
m = []
znak = ('&', '|', '-')
stro = "A&B|-C"

class istin:
    def __init__(self, stro):
        #stroki = pow(2, len(self.simbol(stro)))
        m = self.massstrok(stro)
        otv = []
        i_mass = 0
        for i in range(0, len(stro)):
            #try:
            if stro[i] == "-":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.otric(stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i+1], str(i_mass))
                stro = stro.replace(stro[i], '')
                print 'ONE: '+stro
                i_mass += 1
                break
            #except IndexError:
                #pass
        for i in range(0, len(stro)):
            #try:
            if stro[i] == "&":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.conjunction(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass))
                print stro
                i_mass += 1
                break
            #except IndexError:
                #pass
        print otv


    def conjunction(self, a, b, m, otv, i_mass):
        print a
        print b
        if type(a) == int:
            mass1 = otv[a]
        else:
            for s in m:
                if s[0] == a:
                    mass1 = s
        if type(b) == int:
            mass2 = otv[b]
        else:
            for s in m:
                if s[0] == b:
                    mass2 = s
        print mass1
        print mass2
        otv.append([])
        print range(1, len(mass1))
        for i in range(1, len(mass1)):
            otv[i_mass].append(int(int(mass1[i]) & int(mass2[i])))
        return otv

    def otric(self, vir, m, otv, i_mass):
        # Принимаю выражение, массив с начальными значениями, массив ответов, в какую ячейку записывать
        # Составлять новый массив и назначить ему номер, вернуть строку с заменой символов на номер, или просто вернуть носер, замену сделать там
        #print 'Выражение: '+vir
        if type(vir) == int:
            # ToDo: если выражение число, то искать в другом массиве и менять его
            print 'fix_me'
        else:
            for s in m:
                #print s
                if s[0] == vir:
                    otv.append([])
                    for i in s:
                        if i == 0:
                            otv[i_mass].append(1)
                        elif i == 1:
                            otv[i_mass].append(0)

        #print m
        #print otv
        return otv
            #for s in range(0, len(m)):
                #print m[s][0]
                #if m[s][0] == vir:
                    #for i in range(1, len(m[s])):
                        #if m[s][i] == 0:
                            #m[s][i] = 1
                        #elif m[s][i] == 1:
                            #m[s][i] = 0

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
