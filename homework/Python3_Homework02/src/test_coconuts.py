"""
Tests for the classes and methods in the 
coconuts.py module
"""
import unittest

import coconuts

class Test_coconuts(unittest.TestCase):
    """
    Validate the possible coconut varieties.
    """
    def setUp(self):
        """
        Create some coconut object for use later
        """
        self.coconut_weights = {"south_asian": 3.0,
                            "middle_eastern": 2.5,
                            "american": 3.5}
        self.south_asian = coconuts.Coconut(type="south_asian")
        self.middle_eastern = coconuts.Coconut(type="middle_eastern")
        self.american = coconuts.Coconut(type="american")
        self.coconut_inventory = coconuts.Inventory()
                
    def test_Coconut(self):
        """
        Make sure coconuts.Coconut() only handles
        known coconut types and does so accurately.
        """
        with self.assertRaises(TypeError):
            coconuts.Coconut()
        with self.assertRaises(TypeError):
            coconuts.Coconut(type=10)
        with self.assertRaises(AttributeError):
            coconuts.Coconut(type="antarctic_coconut")

        self.assertEqual(self.south_asian.get_weight(), self.coconut_weights["south_asian"])
        self.assertEqual(self.middle_eastern.get_weight(), self.coconut_weights["middle_eastern"])
        self.assertEqual(self.american.get_weight(), self.coconut_weights["american"])
    
    def test_Inventory(self):
        """
        Validate coconuts.Inventory() works as advertised.
        """
        # Inventory starts at 0
        self.assertEqual(self.coconut_inventory.total_weight(), 0, "Inventory should be empty (0 weight)")
        # basic methods produce expected results
        self.coconut_inventory.add_coconut(self.south_asian)
        self.assertEqual(self.coconut_inventory.total_weight(), self.coconut_weights["south_asian"])
        self.coconut_inventory.add_coconut(self.middle_eastern)
        self.assertEqual(self.coconut_inventory.total_weight(), self.coconut_weights["south_asian"] + self.coconut_weights["middle_eastern"])
        self.coconut_inventory.add_coconut(self.american)
        self.assertEqual(self.coconut_inventory.total_weight(), 
                         self.coconut_weights["south_asian"] + self.coconut_weights["middle_eastern"] + self.coconut_weights["american"])
        # We handle error conditionsand bad data
        with self.assertRaises(AttributeError):
            self.coconut_inventory.add_coconut("notacoconut")
        # Inventory adds up as expected with specified coconut varieties and
        # numbers    
        self.mycoconuts = coconuts.Inventory()
        for i in range(2):
            self.mycoconuts.add_coconut(self.south_asian)
        self.mycoconuts.add_coconut(self.middle_eastern)
        for i in range(3):
            self.mycoconuts.add_coconut(self.american)
        self.assertEqual(self.mycoconuts.total_weight(), 19)

if __name__ == "__main__":
    unittest.main()    