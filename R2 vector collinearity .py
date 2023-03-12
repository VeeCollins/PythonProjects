import math
def triangle():
    """ Assess linear dependence using vector triangle inequality for R2 vectors.
    Input two tuples
    Add two vectors and calculate length = C
    Calculate length of each vector and add =  AB
    If C=AB then dependent, if C<AB, independent"""

    
    V1 = input("Vector 1 seperated by commas: ").split(",")
    V2 = input("Vector 2 seperated by commas: ").split(",")
    V1a,V1b = V1
    V2a,V2b = V2
    V1a,V1b,V2a,V2b = int(V1a),int(V1b),int(V2a),int(V2b)
    
    def dotprod (val1,val2):
        return math.sqrt(val1 **2 + val2 **2)

    AB = round(dotprod(V1a,V1b)+ dotprod(V2a,V2b),4)
    C= round(dotprod(V1a+V2a, V1b+V2b),4)
    
    print("C= ",C)
    print("AB= ",AB)

    if C < AB:
        print("Independent")
    else:
        print("Colinear")
    return

triangle()
