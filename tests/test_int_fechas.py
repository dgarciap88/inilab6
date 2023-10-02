import  unittest
from datetime import date

def day_since_birth(d0,d1):
    delta = d1 - d0
    return delta.days
def mounths_since_birth(d0,d1):
    delta = d1 - d0
    return int(delta.days/30)
def years_since_birth(d0,d1):
    delta = d1 - d0
    return int(delta.days/365)

def calcule_age(d0):
    d1 =date.today()
    return {
        'years':years_since_birth(d0,d1),
        'mounths':mounths_since_birth(d0,d1),
        'days':day_since_birth(d0,d1)
    }

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        d0 = date(2008, 8, 18)
        total= calcule_age(d0)
        print(total)
        self.assertEqual(15,total.get('years'))