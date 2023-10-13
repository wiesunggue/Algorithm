from math import acos,sqrt,pi

def chk_trianglity(point):
    p1,p2,p3 = point
    X,Y= ((p2[0]-p1[0],p2[1]-p1[1]),(p3[0]-p1[0],p3[1]-p1[1]))
    #x1 y1 z1
    #x2 y2 z2
    #x3 y3 z3
    
    return X[0]*Y[1]-X[1]*Y[0]
def Mangle(point):
    p1,p2,p3 = point
    v1 = ((p2[0]-p1[0],p2[1]-p1[1]),(p3[0]-p1[0],p3[1]-p1[1]))
    v2 = ((p1[0]-p2[0],p1[1]-p2[1]),(p3[0]-p2[0],p3[1]-p2[1]))
    v3 = ((p1[0]-p3[0],p1[1]-p3[1]),(p2[0]-p3[0],p2[1]-p3[1]))
    ang=0
    for v in [v1,v2,v3]:
        x,y = v
        ang = max(ang,acos((x[0]*y[0]+x[1]*y[1])/sqrt(dist2(x,[0,0])*dist2(y,[0,0]))))
    ang = (ang/pi)*180
    return ang

def triangle(point):
    m_ang = Mangle(point)
    p1,p2,p3 = point
    d1 = dist2(p1,p2)
    d2 = dist2(p1,p3)
    d3 = dist2(p2,p3)
    sd1,sd2,sd3 = sorted([d1,d2,d3])
    rec=False
    if sd1+sd2==sd3:
        rec=True
        
    if d1==d2==d3:
        return ' JungTriangle'
    if d1==d2 or d1==d3 or d2==d3:
        if rec:
            return 'Jikkak2Triangle'
        elif m_ang>90:
            return 'Dunkak2Triangle'
        else:
            return 'Yeahkak2Triangle'
    else:
        if rec:
            return 'JikkakTriangle'
        elif m_ang>90:
            return 'DunkakTriangle'
        else:
            return 'YeahkakTriangle'
def dist2(x,y):
    return (x[0]-y[0])**2+(x[1]-y[1])**2

p1=list(map(int,input().split()))+[0]
p2=list(map(int,input().split()))+[0]
p3=list(map(int,input().split()))+[0]

point =(p1,p2,p3)
if chk_trianglity(point)==0:
    print('X')
else:
    print(triangle(point))