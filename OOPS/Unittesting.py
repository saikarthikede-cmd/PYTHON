import unittest
def multiply(a,b):
    return a*b
class TestMath(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2,3),6) #checks if a and b are same or not assertequal(a,b)
if __name__=="__main__":
    unittest.main()
#output if correct prints ok
#if not failed