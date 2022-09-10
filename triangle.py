
def triangle (a,b,c):
    equilateral = a > 0 and b > 0 and c > 0 and a == b and a == c and b == c and b == a and c == a and c == a
    isosceles = a > 0 and b > 0 and c > 0 and a == b and b == a and a != c and b != c or a == c and c == a and b != a and b != c or b == c and c == b and b != a and c != a
    scalene = a > 0 and b > 0 and c > 0 and a != b and a != c and b != c and b != a and c != a and c != a
    if isinstance(a,str) or isinstance(b,str) or isinstance(c,str):
         return "Invalid"   
    else:
        if equilateral == True:
            return "Equilateral"
        elif isosceles == True:
            return "Isosceles"
        elif scalene == True:
            return "Scalene"
        else:
            return "Invalid"





        


