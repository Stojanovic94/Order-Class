import unittest
# Uveri se da je import tačan pod obavezno
from order import Order

class TestOrder(unittest.TestCase):

        def test_calculate_total_positive(self):
                """Testira da li metoda pravilno računa iznos kada je cena i količina pozitivna"""
        
                # Cena po komadu je 100, a količina 3
                # Očekivana ukupna cena je 300
                order = Order(100, 3) 
                self.assertEqual(order.calculate_total(), 300)

        def test_calculate_total_zero_quantity(self):
                """Testira da li metoda pravilno vraća 0 kada je količina 0"""
        
                # Cena po komadu je 100, a količina je 0
                # Ukupna cena treba biti 0
                order = Order(100, 0)
                self.assertEqual(order.calculate_total(), 0)

        def test_calculate_total_negative_price(self):
                """Testira kako metoda reaguje na negativnu cenu"""
        
                # Cena po komadu je -100, a količina je 3
                # Očekivana ukupna cena je -300
                order = Order(-100, 3)
                self.assertEqual(order.calculate_total(), -300)

        def test_calculate_total_invalid_input(self):
                """Testira kako metoda reaguje na nevalidne ulaze"""
        
                # Cena je string, a ne broj
                order = Order("100", 3)
            
                # Očekivana greška: TypeError
                with self.assertRaises(TypeError):  
                order.calculate_total()
            
        def test_order_items_in_list(self):
                """Testira da li je stavka u listi proizvoda"""
                order = Order(100, 3)
        
                # Proverava da li 'product1' postoji u listi
                self.assertIn('product1', order.get_items())  

        def test_order_items_not_in_list(self):
               """Testira da li stavka nije u listi proizvoda"""
               order = Order(100, 3)
        
               # Proverava da li 'product4' nije u listi
               self.assertNotIn('product4', order.get_items()) 

        def test_order_item_count_equal(self):
               """Testira da li dve liste proizvoda imaju iste stavke, nezavisno od reda"""
                order = Order(100, 3)
        
               # Proverava da li lista proizvoda sadrži iste stavke kao u drugoj listi
               self.assertCountEqual(order.get_items(), ['product1', 'product2', 'product3'])  
   
               def test_calculate_total_greater_than_zero(self):
               """Testira da li ukupna cena bude veća od 0"""
               order = Order(100, 3)
        
               # Proverava da li je ukupna cena veća od 0
               self.assertGreater(order.calculate_total(), 0) 

        def test_calculate_total_less_than_max(self):
                """Testira da li ukupna cena bude manja od 500"""
                order = Order(100, 3)
        
                # Proverava da li je ukupna cena manja od 500
                self.assertLess(order.calculate_total(), 500)  
        
        def test_calculate_total_with_invalid_quantity(self):
                """Testira da li metoda vraća grešku ako je količina nevalidna"""
        
                # Nevalidan tip za količinu
                order = Order(100, "nevalidna količina") 
        
                # Očekujemo da TypeError bude podignut
                with self.assertRaises(TypeError): 
                order.calculate_total()

if __name__ == '__main__':
        unittest.main()
