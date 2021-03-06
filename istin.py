#!/bin/python
# -*- coding: utf-8 -*-
# DeKoniX =^_^= 2013

m = []
znak = ('&', '|', '-', '>', '~', '(', ')')
stro = "(-(A&B)|(C&B&A>-(A&-C~B&C))&(-A))"

class istin:
    def __init__(self, stro):
        print stro
        i_mass = 0
        otv = []
        m = self.massstrok(stro)
        self.massstr = self.massstrok(stro)
        print m
        self.otv, asd = self.go(stro, i_mass, otv, m)
        if self.otv == []:
            self.otv = m

    def go(self, stro, i_mass, otv, m):
        while stro.find('(') != -1:
            k = 0
            for i in range(0, len(stro)):
                if stro[i] == '(':
                    k += 1
                    if k == 1:
                        str_begin = i
                if stro[i] == ')':
                    k -= 1
                    if k == 0:
                        str_end = i
            otv, i_mass = self.go(stro[str_begin+1:str_end], i_mass, otv, m)
            stro = stro.replace(stro[str_begin:str_end+1], str(i_mass-1))

        # Отрицание
        i = 0
        while i<len(stro):
            if stro[i] == "-":
                d, p = self.chislo(stro, i, True)
                otv = self.otric(stro[i+1:i+p+1], m, otv, i_mass)
                stro = stro.replace(stro[i+1:i+p+1], str(i_mass), 1)
                stro = stro.replace(stro[i], '', 1)
                i_mass += 1
                i -= 1
            i += 1
        # Конъюнкция
        i = 0
        while i<len(stro):
            if stro[i] == "&":
                d, p = self.chislo(stro, i, False)
                otv = self.conjunction(stro[i-d:i], stro[i+1:i+p+1], m, otv, i_mass)
                stro = stro.replace(stro[i-d:i+p+1], str(i_mass), 1)
                i_mass += 1
                i -= 2
            i += 1
        # Дизъюнкция
        i = 0
        while i<len(stro):
            if stro[i] == "|":
                d, p = self.chislo(stro, i, False)
                otv = self.disjunction(stro[i-d:i], stro[i+1:i+p+1], m, otv, i_mass)
                stro = stro.replace(stro[i-d:i+p+1], str(i_mass))
                i_mass += 1
                i -= 2
            i += 1
        # Импликация
        i = 0
        while i<len(stro):
            if stro[i] == ">":
                d, p = self.chislo(stro, i, False)
                otv = self.implication(stro[i-d:i], stro[i+1:i+p+1], m, otv, i_mass)
                stro = stro.replace(stro[i-d:i+p+1], str(i_mass))
                i_mass += 1
                i -= 2
            i += 1
        # Эквиваленция
        i = 0
        while i<len(stro):
            if stro[i] == "~":
                d, p = self.chislo(stro, i, False)
                otv = self.equality(stro[i-d:i], stro[i+1:i+p+1], m, otv, i_mass)
                stro = stro.replace(stro[i-d:i+p+1], str(i_mass))
                i_mass += 1
                i -= 2
            i += 1
        return otv, i_mass

    def chislo(self, stro, i, otric):
        p = 0
        d = 0
        buf = i
        i += 1
        while i<len(stro):
            p += 1
            for z in znak:
                if z == stro[i]:
                    i = len(stro)
                    p -= 1
                    break
            i += 1

        if otric == False:
            i = buf
            i -= 1
            while i>=0:
                d += 1
                for z in znak:
                    if z == stro[i]:
                        i = 0
                        d -= 1
                        break
                i -= 1

        return d, p

    def equality(self, a, b, m, otv, i_mass):
        print a+"~"+b
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
            mass1 = mass1[1:]

        try:
            mass2 = otv[int(b)]
        except ValueError:
            for s in m:
                if s[0] == b:
                    mass2 = s
            mass2 = mass2[1:]
        otv.append([])
        for i in range(0, len(mass1)):
            otv[i_mass].append(int(int(mass1[i]) == int(mass2[i])))
            print str(mass1[i])+"~"+str(mass2[i])+" = "+str(int(int(mass1[i]) == int(mass2[i])))
        return otv


    def implication(self, a, b, m, otv, i_mass):
        print a+">"+b
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
            mass1 = mass1[1:]

        try:
            mass2 = otv[int(b)]
        except ValueError:
            for s in m:
                if s[0] == b:
                    mass2 = s
            mass2 = mass2[1:]
        otv.append([])
        for i in range(0, len(mass1)):
            otv[i_mass].append(int(not(int(mass1[i]))) | int(mass2[i]))
            print str(mass1[i])+">"+str(mass2[i])+" = "+str(int(not(int(mass1[i]))) | int(mass2[i]))
        return otv


    def disjunction(self, a, b, m, otv, i_mass):
        print a+"|"+b
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
            mass1 = mass1[1:]

        try:
            mass2 = otv[int(b)]
        except ValueError:
            for s in m:
                if s[0] == b:
                    mass2 = s
            mass2 = mass2[1:]
        otv.append([])
        for i in range(0, len(mass1)):
            otv[i_mass].append(int(int(mass1[i]) | int(mass2[i])))
            print str(mass1[i])+"|"+str(mass2[i])+" = "+str(int(int(mass1[i]) | int(mass2[i])))
        return otv

    def conjunction(self, a, b, m, otv, i_mass):
        print a+"&"+b
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
            mass1 = mass1[1:]

        try:
            mass2 = otv[int(b)]
        except ValueError:
            for s in m:
                if s[0] == b:
                    mass2 = s
            mass2 = mass2[1:]
        otv.append([])
        for i in range(0, len(mass1)):
            otv[i_mass].append(int(int(mass1[i]) & int(mass2[i])))
            print str(mass1[i])+"&"+str(mass2[i])+" = "+str(int(int(mass1[i]) & int(mass2[i])))
        return otv

    def otric(self, a, m, otv, i_mass):
        print "-"+a
        try:
            mass1 = otv[int(a)]
        except ValueError:
            for s in m:
                if s[0] == a:
                    mass1 = s
            mass1 = mass1[1:]
        otv.append([])
        for i in range(0, len(mass1)):
            otv[i_mass].append(int(not int(mass1[i])))
            print "-"+str(mass1[i])+" = "+str(int(not int(mass1[i])))
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
            j+=1
        return mass
#istin(stro)
