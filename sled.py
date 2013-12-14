import istin

class sled:
    def __init__(self, posil, zakl):
        self.go(posil, zakl)

    def go(self, posil, zakl):
        a = istin.istin(posil)
        mass_posil = a.massstr
        b = istin.istin(zakl)
        mass_zakl = b.massstr

        if mass_posil != mass_zakl:
            print "NOOOO!!!"
        else:
            otv_posil = a.otv[-1]
            otv_zakl = b.otv[-1]
            if len(zakl) <= 1:
                otv_zakl = otv_zakl[1:]
            m1 = self.method1(otv_posil, otv_zakl)
            m2 = self.method2(posil, zakl)
            if m1:
                print "VERNO METHOD1"
            else:
                print "NE VERNO METHOD1"
            if m2:
                print "VERNO METHOD2"
            else:
                print "NE VERNO METHOD2"


    def method1(self, posil, zakl):
        print posil
        print zakl
        for i in range(len(posil)):
            if posil[i] == 1:
                if zakl[i] == 0:
                    return 0
        return 1

    def method2(self, posil, zakl):
        if len(zakl) <= 1:
            sttro = "("+posil+")>"+zakl
        else:
            sttro = "("+posil+")>("+zakl+")"
        otv = istin.istin(sttro)
        gg = otv.otv[-1]
        print gg
        for i in gg:
            if i == 0:
                return 0
        return 1

#sled("x&y","x")
