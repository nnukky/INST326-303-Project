#Pytest script for project.py

import project as p

def cart_total_test(self):
    test = p.Helper(p.create_store)
    self.cart = {2: ('Macbook Pro (item id 2)', 1299.29, 'Aisle 1', 'Electronics', 2), 
                 3: ('Samsung 60 (item id 3)" TV', 799.99, 'Aisle 2', 'Electronics', 3),
                 7: ("Blue Napkins (item id 7)", 6.99, "Aisle 4", "Paper Products", 10)}
    
    test.cart_total() == 1299.29 + 799.99 + 6.99