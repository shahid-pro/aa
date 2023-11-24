from sympy import symbols, Eq, solve
w,x,y,z,i,j,k,l,o,p=symbols('w,x,y,z,i,j,k,l,o,p')
print("Objective:- C=3x+5y, subject to:")
eq1=Eq(2*x+3*y,12)
print("Equation 1:")
print("2*x+3*y<=12")
eq2=Eq(-x+y,3)
print("Equation 2:")
print("-x+y<=3")
eq3=Eq(x,4)
print("Equation 3:")
print("x<=4")
eq4=Eq(y,3)
print("Equation 4:")
print("y>=3")
w1=solve((eq1,eq2),(x,y))
i1=w1[x]
j1=w1[y]
z1=3*i1+5*j1
print("Equation 1 intersects Equation 2 at",w1)
w2=solve((eq1,eq3),(x,y))
i2=w2[x]
j2=w2[y]
z2=3*i2+5*j2
print("Equation 1 intersects Equation 3 at",w2)
w3=solve((eq1,eq4),(x,y))
i3=w3[x]
j3=w3[y]
z3=3*i3+5*j3
print("Equation 1 intersects Equation 4 at",w3)
w4=solve((eq2,eq3),(x,y))
i4=w4[x]
j4=w4[y]
z4=3*i4+5*j4
print("Equation 2 intersects Equation 3 at",w4)
w5=solve((eq2,eq4),(x,y))
i5=w5[x]
j5=w5[y]
z5=3*i5+5*j5
print("Equation 2 intersects Equation 4 at",w5)
w6=solve((eq3,eq4),(x,y))
i6=w6[x]
j6=w6[y]
z6=3*i6+5*j6
print("Equation 3 intersects Equation 4 at",w6)
i1,j1= w1[x],w1[y]
if i1>4 or j1<3:
    print("C is infeasable")
else:
    print("For maximization, intersection points of x and y are as follows:")
    print(w1)
    z1=3*i1+5*j1
    print("C=",float(z1))
    w7=min(z1,z2,z3,z4,z5,z6)
    if w7==z1:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",i1,", y:",j1)
    elif w7==z2:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",i2,", y:",j2)
    elif w7==z3:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",i3,", y:",j3)
    elif w7==z4:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",i4,", y:",j4)
    elif w7==z5:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",i5,", y:",j5)
    elif w7==z6:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",i6,", y:",j6)
    print("C=",float(w7))
print("Objective:- C=2x+y, subject to:")
eq5=Eq(x+y,6)
print("Equation 1:")
print("2*x+3*y<=12")
eq6=Eq(x-y,3)
print("Equation 2:")
print("-x+y<=3")
eq7=Eq(x,0)
print("Equation 3:")
print("x<=4")
eq8=Eq(y,0)
print("Equation 4:")
print("y>=3")
o1=solve((eq5,eq6),(x,y))
k1=o1[x]
l1=o1[y]
p1=2*k1+l1
print("Equation 1 intersects Equation 2 at",o1)
o2=solve((eq5,eq7),(x,y))
k2=o2[x]
l2=o2[y]
p2=2*k2+l2
print("Equation 1 intersects Equation 3 at",o2)
o3=solve((eq5,eq8),(x,y))
k3=o3[x]
l3=o3[y]
p3=2*k3+l3
print("Equation 1 intersects Equation 4 at",o3)
o4=solve((eq6,eq7),(x,y))
k4=o4[x]
l4=o4[y]
p4=2*k4+l4
print("Equation 2 intersects Equation 3 at",o4)
o5=solve((eq6,eq8),(x,y))
k5=o5[x]
l5=o5[y]
p5=2*k5+l5
print("Equation 2 intersects Equation 4 at",o5)
o6=solve((eq7,eq8),(x,y))
k6=o6[x]
l6=o6[y]
p6=2*k6+l6
print("Equation 3 intersects Equation 4 at",o6)
k1,l1= o1[x],o1[y]
if k1>0 or l1<0:
    print("C is infeasable")
else:
    print("For maximization, intersection points of x and y are as follows:")
    print(o1)
    o1=2*k1+l1
    print("C=",float(z2))
    o7=min(p1,p2,p3,p4,p5,p6)
    if o7==p1:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",k1,", y:",l1)
    elif o7==p2:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",k2,", y:",l2)
    elif o7==p3:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",k3,", y:",l3)
    elif o7==p4:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",k4,", y:",l4)
    elif o7==p5:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",k5,", y:",l5)
    elif o7==p6:
        print("For minimization, intersection points of x and y are as follows:")
        print("x:",k6,", y:",l6)
    print("C=",float(o7))