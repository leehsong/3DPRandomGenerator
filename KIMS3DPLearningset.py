import numpy as np
import sys
import os

class Randomset:
    name = "KIMS3DPLearingset"
    Xsize = 10
    Ysize = 10
    nTotal = Xsize * Ysize
    nType = 3
    nSeed = 5000
    strname = 'test.scad'
    def __init__(self, Xsize, Ysize, nType, nSeed):
        print("=======Init=====")
        self.Xsize = Xsize
        self.Ysize = Ysize
        self.nTotal = self.Xsize*self.Ysize
        self.nType = nType
        self.nSeed = nSeed
        np.random.seed(self.nSeed)
        self.strname = "S{size}_T{type}_R{seed}".format(size=Xsize, type=nType, seed=nSeed)
        print("============================")
        print(self.strname)
        print("============================")
    def info(self):
        print('This is the class named ', self.name, '!')
    def generate(self):
        print("=======generate=====")
        A = np.random.normal(loc=0.8, scale=0.1, size=self.nTotal)

        rA = np.reshape(A, (self.Xsize, self.Ysize))
        ## Type Selection ( 0: circle , 1:Triangle, 2:Square, 3:Pentagon, 4: Hexagon)

        print("=======12=====")
        B = np.random.random(self.nTotal)
        for i in range(self.nTotal):
            B[i] = int(B[i]*self.nType)
            if B[i] == 0:
                B[i]= 20
            else:
                B[i] = B[i] + 2
        print("=======Reshape=====")
        rB = np.reshape(B, (self.Xsize, self.Ysize))
        Z = rA
        np.savez_compressed (self.strname, Size=rA,Shape= rB)

        f = open(self.strname+'.scad', 'w')
        f.write("union(){\n")
        for x in range(0,self.Xsize):
            for y in range(0,self.Ysize):
                s0 = 'translate(v=[{x0}, {y0}, 0]) '
                s1 = ' cylinder(h=1, r={r0}, $fn={fn} ) ;'
                f.write(s0.format(x0=x, y0=y,r0=rA[x,y]/2.0, fn= int(rB[x,y])))
                f.write("{")
                f.write(s1.format(x0=x, y0=y, r0=rA[x, y]/2.0,fn=int(rB[x, y])))
                f.write("}\n")
                if rA[x,y] > 0.7 and rA[x,y] < 0.9:
                    Z[x,y]= 1
                else:
                    Z[x,y] =0
        f.write("}\n")
        f.close()
#if bstlmaking :
#    outfilename = strname +'.stl'
#    os.system("openscad -o"+ outfilename +" "+ strname+".scad")
#x = [0] * 10
#x = [0 for i in xrange(10)]