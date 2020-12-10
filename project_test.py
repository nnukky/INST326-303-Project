#Pytest script for project.py

import project as p

def test_cart_total():
    test = p.Helper(p.create_store())
    test.add_to_cart(2)
    test.add_to_cart(23)
    test.add_to_cart(26)
    test.add_to_cart(19)    
    assert test.cart_total() == 1299.29 + 249.99 + 119.99 + 27.99
    
    assert test.cart_total() == 1299.29 + 249.99 + 119.99 + 27.99
    
def test_narrow_categories() :
    test = p.Helper(p.create_store())
    if narrow == "yes"  :
        assert test.narrow_categories(1) == brand
    
def test_item_attributes() :
    test = p.Helper(p.create_store())
    
def test_add_to_cart():
    test2 = p.Helper(p.create_store())
    assert test2.add_to_cart(1)==("iPhone 12 (item id 1)", 999.99, "Aisle 1", "Electronics", 8)
    assert test2.add_to_cart(8)==("White Paper Towels (item id 8)", 4.99, "Aisle 3", "Paper Products", 4)
    assert test2.add_to_cart(13)==("Half & Half (item id 13)", 3.99, "Aisle 5", "Dairy", 6)
    assert test2.add_to_cart(21)==("Sourdough Bread (item id 21)", 4.99, "Aisle 7", "Bakery", 6)
    assert test2.add_to_cart(26)==("School Desk (item id 26)", 119.99, "Aisle 9", "Furniture", 2)
    
def test_check_cart():
    test3=p.Helper(p.create_store())   
    test3.add_to_cart(1)
    test3.add_to_cart(8)
    test3.add_to_cart(13)
    test3.add_to_cart(21)
    test3.add_to_cart(26)
    assert test3.check_cart()=={1:("iPhone 12 (item id 1)", 999.99, "Aisle 1", "Electronics", 8), 
                                8: ("White Paper Towels (item id 8)", 4.99, "Aisle 3", "Paper Products", 4),
                                13: ("Half & Half (item id 13)", 3.99, "Aisle 5", "Dairy", 6),
                                21: ("Sourdough Bread (item id 21)", 4.99, "Aisle 7", "Bakery", 6),
                                26: ("School Desk (item id 26)", 119.99, "Aisle 9", "Furniture", 2)}     
        
    