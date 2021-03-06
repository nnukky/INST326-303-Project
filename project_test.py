#Pytest script for project.py

import project as p
from unittest import mock
import builtins


def test_categories_search(capsys):
    captured = capsys.readouterr()
    test = p.Helper(p.create_store())
    if captured.out == "no":
        if specific_search == "no" and selection==1:
            assert test.categories_search(1) ==("iPhone 12", 999.99, "Aisle 1", "Electronics", 8)
        if specific_search == "no" and selection==5:
            assert test.categories_search(25) ==("Living Room Chair", 74.99, "Aisle 8", "Furniture", 8)
    elif captured.out == "yes":
        test.item_attributes()


def test_cart_total():
    #Case 1
    test = p.Helper(p.create_store())
    test.add_to_cart(2)
    test.add_to_cart(23)
    test.add_to_cart(26)
    test.add_to_cart(19)    
    assert test.cart_total() == round(1299.29 + 249.99 + 119.99 + 27.99, 2)
    
    #Case 2
    test2 = p.Helper(p.create_store())
    test2.add_to_cart(25)
    test2.add_to_cart(17)
    test2.add_to_cart(5)
    test2.add_to_cart(15)    
    assert test2.cart_total() == round(74.99 + 5.99 + 399.99 + 1.99, 2)
    
def test_narrow_categories(capsys) :
    captured = capsys.readouterr()
    test = p.Helper(p.create_store())
    if captured.out == "yes":
    # happy path case 1
        while test.narrow_categories(1) == True :
            with mock.patch("builtins.input",
                    side_effect = ["Apple", "phone"]):
                s = test.narrow_categories(selection)
                x = ["iPhone 12 (ID 1)", "iPad (ID 4)", "Macbook Pro (ID 2)", "Apple Watch (ID 5)"]
                y = ["iPhone (ID 1)"]
                assert s == x, y
    # happy path case 2
        while test.narrow_categories(5) == True :    
            with mock.patch("builtins.input",
                    side_effect = ["Chair", "Kitchen"]):
                s = test.narrow_categories(selection)
                x = ["Kitchen Chair (ID 22)", "Living Room Chair (ID 25)"]
                y = ["Kitchen Chair (ID 22)"]
                assert s == x, y
    # invalid inputs
        while test.narrow_categories(1) == True :    
            with mock.patch("builtins.input",
                    side_effect = ["T-Mobile", "laptop"]):
                s = test.narrow_categories(selection)
                x = "We do not have this brand in our inventory."
                y = "We do not have this electronic type in our inventory."
                assert s == x, y
    
def test_item_attributes(capsys) :
    captured = capsys.readouterr()
    test = p.Helper(p.create_store())
    # happy path case 1
    if captured.out == "iPhone 12":
        if item == "iPhone 12" :
            assert test.item_attributes() == ("iPhone 12 is $999.99 with ID 1 and you can find it in Aisle 1 in the Electronics Department. We currently have 8 in stock.")
    # happy path case 2
    if captured.out == "Kitchen Chair" :
        if item == "Kitchen Chair" :
            assert test_item_attributes() == ("Kitchen Chair is $64.99 with ID 22 and you can find it in Aisle 8 in the Furniture Department. We currently have 4 in stock.")
    # invalid input
    if captured.out == "Cheese Balls":
        if item == "Cheese Balls" :
            assert test.item_attributes() ==("This item does not exist in the store.")
             
    
def test_add_to_cart():
    test = p.Helper(p.create_store())
    assert test.add_to_cart(1)==["iPhone 12", 999.99, "Aisle 1", "Electronics", 8, 1]
    assert test.add_to_cart(8)==["White Paper Towels", 4.99, "Aisle 3", "Paper Products", 4, 8]
    assert test.add_to_cart(13)==["Half & Half", 3.99, "Aisle 5", "Dairy", 6, 13]
    assert test.add_to_cart(21)==["Sourdough Bread", 4.99, "Aisle 7", "Bakery", 6, 21]
    assert test.add_to_cart(26)==["School Desk", 119.99, "Aisle 9", "Furniture", 2, 26]
    
def test_check_cart():
    test=p.Helper(p.create_store())   
    test.add_to_cart(1)
    test.add_to_cart(8)
    test.add_to_cart(13)
    test.add_to_cart(21)
    test.add_to_cart(26)
    assert test.check_cart()=={1:["iPhone 12", 999.99, "Aisle 1", "Electronics", 8, 1], 
                                8: ["White Paper Towels", 4.99, "Aisle 3", "Paper Products", 4, 8],
                                13: ["Half & Half", 3.99, "Aisle 5", "Dairy", 6, 13],
                                21: ["Sourdough Bread", 4.99, "Aisle 7", "Bakery", 6, 21],
                                26: ["School Desk", 119.99, "Aisle 9", "Furniture", 2, 26]}     
        
    