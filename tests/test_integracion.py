import  unittest


def calculadoratotal(precios):
    total= sum(precios)
    return total

def calculadoradescuento(total,descuento):
    descuento= total*(descuento/100)
    return descuento

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        precios = [10,20,30]
        total= calculadoratotal(precios)
        descuento=10
        descuento=calculadoradescuento(total,descuento)
        espera=6
        self.assertEqual(descuento,espera)