"""
Created on Mon Mar 27 12:31:17 2017

@author: Will Burke
"""

O = (0, 0, 0)
A = (.25, 1, 0)
B = (1, .1, 0)
C = (.2, .2, 1)

def PlaneCheck(C1, C2, C3, P):
    """
    in: C1, C2, C3 <tuples> of 3 space coordinates, tet vertices
    P = <tuple> of xyz coordinates for random space in X,Y,Z bounding box of tetrahedron
    out: <bool>, returns True if P is below the plane defined by C1, C2, C3
    """
    V1 = ((C2[0] - C1[0]), (C2[1] - C1[1]), (C2[2] - C1[2]))    # vectors that
    V2 = ((C3[0] - C1[0]), (C3[1] - C1[1]), (C3[2] - C1[2]))    # define plane
    
    a = (V1[1]*V2[2] - V1[2]*V2[1])
    b = (V1[2]*V2[0] - V1[0]*V2[2])
    c = (V1[0]*V2[1] - V1[1]*V2[0])
    n = (a, b, c)                                               # normal vector
    
    d = -((a*C1[0] + b*C1[1] + c*C1[2]))
    
    z_p = -(a*P[0] + b*P[1] + d)/c   # calculates z value on plane for associated Px, Py
    
    if P[2] <= z_p:
        return True
    else:
        return False
    
def TetCheck(O, A, B, C, P):
    P1_bool = PlaneCheck(O, B, C, P)
    P2_bool = PlaneCheck(O, A, C, P)
    P3_bool = PlaneCheck(A, B, C, P)
    
    if P1_bool == True:
        if P2_bool == True:
            if P3_bool == True:
                return True
            
    else:
        return False
    
    
def TetCompute
    
    
x = PlaneCheck(O,A,B,(0,0,0))
