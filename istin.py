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
#stro = "P&Q|R&P"

class istin:
    def __init__(self, stro):
        #stroki = pow(2, len(self.simbol(stro)))
        m = self.massstrok(stro)
        otv = []
        i_mass = 0
        print stro
        # Отрицание
        for i in range(0, len(stro)):
            if stro[i] == "-":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.otric(stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i+1], str(i_mass))
                stro = stro.replace(stro[i], '')
                i_mass += 1
                break
        # Конъюнкция
        for i in range(0, len(stro)):
            if stro[i] == "&":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.conjunction(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass))
                i_mass += 1
                break
        # Дизъюнкция
        for i in range(0, len(stro)):
            if stro[i] == "|":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.disjunction(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass))
                i_mass += 1
                break
        print otv


    def disjunction(self, a, b, m, otv, i_mass):
        print a+"|"+b
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
        try:
            mass2 = otv[int(b)]
        except ValueError:
            for s in m:
                if s[0] == b:
                    mass2 = s
        otv.append([])
        print range(1, len(mass1))
        for i in range(0, len(mass1)):
            try:
                otv[i_mass].append(int(int(mass1[i]) | int(mass2[i])))
                print str(mass1[i])+"|"+str(mass2[i])+" = "+str(int(int(mass1[i]) | int(mass2[i])))
            except:
                pass
        return otv

    def conjunction(self, a, b, m, otv, i_mass):
        print a+"&"+b
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
        try:
            mass2 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == b:
                    mass2 = s
        otv.append([])
        print range(1, len(mass1))
        for i in range(0, len(mass1)):
            try:
                otv[i_mass].append(int(int(mass1[i]) & int(mass2[i])))
                print str(mass1[i])+"&"+str(mass2[i])+" = "+str(int(int(mass1[i]) & int(mass2[i])))
            except:
                pass
        return otv

    def otric(self, a, m, otv, i_mass):
        print "-"+a
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
        otv.append([])
        for i in range(1, len(mass1)):
            try:
                otv[i_mass].append(int(not int(mass1[i])))
                print "-"+str(mass1[i])+" = "+str(int(not int(mass1[i])))
            except:
                pass
        return otv

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
