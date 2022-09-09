
def triangle (a,b,c):
    if isinstance(a,str) or isinstance(b,str) or isinstance(c,str):
         return "Invalid"   
    else:
        if a > 0 and b > 0 and c > 0 and a == b and a == c and b == c and b == a and c == a and c == a:
            return "Equilateral"
        elif a > 0 and b > 0 and c > 0 and a == b and b == a and a != c and b != c or a == c and c == a and b != a and b != c or b == c and c == b and b != a and c != a:
            return "Isosceles"
        elif a > 0 and b > 0 and c > 0 and a != b and a != c and b != c and b != a and c != a and c != a:
            return "Scalene"
        else:
            return "Invalid"





        


