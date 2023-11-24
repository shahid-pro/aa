import pulp as p
Lp_prob01=p.LpProblem('Maximization_Problem',p.LpMaximize)
x1=p.LpVariable("x1",lowBound=0)
y1=p.LpVariable("y1",lowBound=0)
Lp_prob01+=3*x1+5*y1
Lp_prob01+=2*x1+3*y1<=12
Lp_prob01+=-x1+y1<=3
Lp_prob01+=x1<=4
Lp_prob01+=y1>=3
status01=Lp_prob01.solve()
p.LpStatus[status01]
if status01!=p.LpStatusInfeasible:
    print("For maximization of equation 1, value of x1:",p.value(x1),", y1:",p.value(y1),", Maximized value:",p.value(Lp_prob01.objective))
    Lp_prob02 = p.LpProblem('Minimization_Problem',p.LpMinimize)
    x2=p.LpVariable("x2",lowBound=0)
    y2=p.LpVariable("y2",lowBound=0)
    Lp_prob02+=3*x2+5*y2
    Lp_prob02+=2*x2+3*y2<=12
    Lp_prob02+=-x2+y2<=3
    Lp_prob02+=x2<=4
    Lp_prob02+=y2>=3
    status02=Lp_prob02.solve()
    print("For minimization of equation 1, value of x2:",p.value(x2),", y2:",p.value(y2),", Minimized value:",p.value(Lp_prob02.objective))
else:
    print("C is infeasable for equation 1")
Lp_prob11=p.LpProblem('Maximization_Problem',p.LpMaximize)
x3=p.LpVariable("x3",lowBound=0)
y3=p.LpVariable("y3",lowBound=0)
Lp_prob11+=2*x3+y3
Lp_prob11+=x3+y3>=6
Lp_prob11+=x3-y3>=3
Lp_prob11+=x3<=0
Lp_prob11+=y3>=0
status11=Lp_prob11.solve()
p.LpStatus[status11]
if status11!=p.LpStatusInfeasible:
    print("For maximization of equation 2, value of x3:",p.value(x3),", y3:",p.value(y3),", Maximized value:",p.value(Lp_prob11.objective))
    Lp_prob12 = p.LpProblem('Minimization_Problem',p.LpMinimize)
    x4=p.LpVariable("x4",lowBound=0)
    y4=p.LpVariable("y4",lowBound=0)
    Lp_prob12+=2*x4+y4
    Lp_prob12+=x4+y4>=6
    Lp_prob12+=x4-y4>=3
    Lp_prob12+=x4<=0
    Lp_prob12+=y4>=0
    status12=Lp_prob12.solve()
    print("For minimization of equation 2, value of x4:",p.value(x4),", y4:",p.value(y4),", Minimized value:",p.value(Lp_prob12.objective))
else:
    print("C is infeasable for equation 2")