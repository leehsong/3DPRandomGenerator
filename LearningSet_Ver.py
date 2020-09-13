import numpy as np
import sys
import os
print('Number of arguments:'+ str(len(sys.argv))+ 'arguments.')
print('Argument List:'+ str(sys.argv))

if len(sys.argv) < 5:
    print('Usage: [size] [number of type] [RandomSeed] [stl making] ')
    sys.exit(1)

## parameter
Xsize = int(sys.argv[1])
Ysize = Xsize
nTotal = Xsize*Ysize
nType = int(sys.argv[2])
nSeed = int(sys.argv[3])
np.random.seed(nSeed)

strname =  "S{size}_T{type}_R{seed}".format(size = Xsize, type = nType, seed=nSeed )
bstlmaking = int(sys.argv[4])

A = np.random.normal(loc=0.8, scale=0.1, size=nTotal)
rA = np.reshape(A, (Xsize, Ysize))

## Type Selection ( 0: circle , 1:Triangle, 2:Square, 3:Pentagon, 4: Hexagon)
B = np.random.random(nTotal)
for i in range(nTotal) :
    B[i] = int(B[i]*nType)
    if B[i] == 0:
        B[i]= 20
    else:
        B[i] = B[i] + 2

rB = np.reshape(B, (Xsize, Ysize))
print(rB)
#with open('test.dat', 'w') as f:
#    rB.tofile(f)
#with open('test.dat', 'r') as f:
#    b.fromfile(f, 2)

#print(b)
## openscad file write
# EXAMPLE
#union(){
#    translate(v=[0, 0, 0]){
#        cylinder(h=10, r=0.3678141596318536, $fn=4);
#    };
Z = rB

f = open(strname+'.scad', 'w')
f.write("union(){\n")
for x in range(0,Xsize):
    for y in range(0,Ysize):
        s0 = 'translate(v=[{x0}, {y0}, 0]) '
        s1 = ' cylinder(h=1, r={r0}, $fn={fn} ) ;'
        f.write(s0.format(x0=x, y0=y,r0=rA[x,y]/2.0, fn= int(rB[x,y])))
        f.write("{")
        f.write(s1.format(x0=x, y0=y, r0=rA[x, y]/2.0,fn=int(rB[x, y])))
        f.write("}\n")
        if rA[x,y] > 0.7 and rA[x,y] < 0.9:
            Z[x,y]= 1
        else:
            Z[x, y] =0

f.write("}\n")
f.close()
print(Z)

if bstlmaking :
    outfilename = strname +'.stl'
    os.system("openscad -o"+ outfilename +" "+ strname+".scad")
#x = [0] * 10
#x = [0 for i in xrange(10)]