#Pytest script for project.py

import project as p

def test_cart_total():
    test = p.Helper(p.create_store())
    test.add_to_cart(2)
    test.add_to_cart(23)
    test.add_to_cart(26)
    test.add_to_cart(19)
    
    assert test.cart_total() == 1299.29 + 249.99 + 119.99 + 27.99
    
def test_narrow_categories() :
    test = p.Helper(p.create_store())
    if narrow == "yes"  :
        assert test.narrow_categories(1) == brand
    
def test_item_attributes() :
    test = p.Helper(p.create_store())
    