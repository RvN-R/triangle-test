import unittest
import triangle

class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(triangle.triangle(2,2,2),"Equilateral")
        self.assertEqual(triangle.triangle(6,6,6),"Equilateral")
        self.assertEqual(triangle.triangle(8,8,8),"Equilateral")

    def test_isosceles(self):
        self.assertEqual(triangle.triangle(2,2,3),"Isosceles")
        self.assertEqual(triangle.triangle(3,2,2),"Isosceles")
        self.assertEqual(triangle.triangle(2,3,2),"Isosceles")
    
    def test_scalene(self):
        self.assertEqual(triangle.triangle(4,5,6),"Scalene")
        self.assertEqual(triangle.triangle(3,4,5),"Scalene")
        self.assertEqual(triangle.triangle(10,20,30),"Scalene")

    def test_invalid(self):
        self.assertEqual(triangle.triangle("4",5,6),"Invalid")
        self.assertEqual(triangle.triangle(4,"5",6),"Invalid")
        self.assertEqual(triangle.triangle(4,5,"6"),"Invalid")
        self.assertEqual(triangle.triangle("4","5","6"),"Invalid")
        self.assertEqual(triangle.triangle(0,5,6),"Invalid")
        self.assertEqual(triangle.triangle(4,0,6),"Invalid")
        self.assertEqual(triangle.triangle(4,0,6),"Invalid")
        self.assertEqual(triangle.triangle(0,0,0),"Invalid")
        

if __name__ == '__main__':
    unittest.main()