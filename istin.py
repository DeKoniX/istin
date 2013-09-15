#!/bin/python
# -*- coding: utf-8 -*-
# DeKoniX =^_^= 2013

m = []
znak = ('&', '|', '-', '>', '~', '(', ')')
stro = "(-(A&B)|(C&B&A>-(A&-C~B&C)))"

class istin:
    def __init__(self, stro):
        print stro
        i_mass = 0
        otv = []
        m = self.massstrok(stro)
        self.go(stro, i_mass, otv, m)

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
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.otric(stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i+1], str(i_mass), 1)
                stro = stro.replace(stro[i], '', 1)
                i_mass += 1
                i -= 1
            i += 1
        print otv
        # Конъюнкция
        i = 0
        while i<len(stro):
            if stro[i] == "&":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.conjunction(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass), 1)
                i_mass += 1
                i -= 2
            i += 1
        print otv
        # Дизъюнкция
        i = 0
        while i<len(stro):
            if stro[i] == "|":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.disjunction(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass))
                i_mass += 1
                i -= 2
            i += 1
        print otv
        # Импликация
        i = 0
        while i<len(stro):
            if stro[i] == ">":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.implication(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass))
                i_mass += 1
                i -= 2
            i += 1
        print otv
        # Эквиваленция
        i = 0
        while i<len(stro):
            if stro[i] == "~":
                # ToDo: передовать не следующий символ, а смотреть сколько символов, для чисел больше 9
                otv = self.equality(stro[i-1], stro[i+1], m, otv, i_mass)
                stro = stro.replace(stro[i-1:i+2], str(i_mass))
                i_mass += 1
                i -= 2
            i += 1
        return otv, i_mass

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
            otv[i_mass].append(int(int(mass1[i]) > int(mass2[i])))
            print str(mass1[i])+">"+str(mass2[i])+" = "+str(int(int(mass1[i]) > int(mass2[i])))
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
        print mass1
        print mass2
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
