#Pytest script for project.py

import project as p
from unittest import mock
import builtins

def test_categories_search():
    test = p.Helper(p.create_store())
    if specific_search == "yes" and selection==1:
        assert test.categories_search(1) ==("iPhone 12", 999.99, "Aisle 1", "Electronics", 8)
    if specific_search == "yes" and selection==5:
        assert test.categories_search(25) ==("Living Room Chair", 74.99, "Aisle 8", "Furniture", 8)

#def test_price_search():
    #test = p.Helper(p.create_store())
    #if price == "yes":
        #assert test.price_search(1) == "Item:2% Milk:$2.99"


def test_cart_total():
    test = p.Helper(p.create_store())
    test.add_to_cart(2)
    test.add_to_cart(23)
    test.add_to_cart(26)
    test.add_to_cart(19)    
    
    assert test.cart_total() == 1299.29 + 249.99 + 119.99 + 27.99
    
def test_narrow_categories() :
    test = p.Helper(p.create_store())
    while test.narrow_categories(1) == True :
        with mock.patch("builtins.input",
                side_effect = ["yes", "Apple", "phone"]):
            s = test.narrow_categories(selection)
            x = ["iPhone 12", "iPad", "Macbook Pro", "Apple Watch"]
            y = ["iPhone", "Android"]
            assert s == x, y
            captured = capsys.readouterr()
            assert captured.out == ""
    
def test_item_attributes() :
    test = p.Helper(p.create_store())
    with mock.patch("builtins.input",
                    side_effect = "")
    
def test_add_to_cart():
    test = p.Helper(p.create_store())
    assert test.add_to_cart(1)==("iPhone 12 (item id 1)", 999.99, "Aisle 1", "Electronics", 8)
    assert test.add_to_cart(8)==("White Paper Towels (item id 8)", 4.99, "Aisle 3", "Paper Products", 4)
    assert test.add_to_cart(13)==("Half & Half (item id 13)", 3.99, "Aisle 5", "Dairy", 6)
    assert test.add_to_cart(21)==("Sourdough Bread (item id 21)", 4.99, "Aisle 7", "Bakery", 6)
    assert test.add_to_cart(26)==("School Desk (item id 26)", 119.99, "Aisle 9", "Furniture", 2)
    
def test_check_cart():
    test=p.Helper(p.create_store())   
    test.add_to_cart(1)
    test.add_to_cart(8)
    test.add_to_cart(13)
    test.add_to_cart(21)
    test.add_to_cart(26)
    assert test.check_cart()=={1:("iPhone 12 (item id 1)", 999.99, "Aisle 1", "Electronics", 8), 
                                8: ("White Paper Towels (item id 8)", 4.99, "Aisle 3", "Paper Products", 4),
                                13: ("Half & Half (item id 13)", 3.99, "Aisle 5", "Dairy", 6),
                                21: ("Sourdough Bread (item id 21)", 4.99, "Aisle 7", "Bakery", 6),
                                26: ("School Desk (item id 26)", 119.99, "Aisle 9", "Furniture", 2)}     
        
    