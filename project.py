"""
INST 326 Final Project
Purpose is to create a fictional warehouse and allow users to locate 
products and view other features associated with them.
"""

from argparse import ArgumentParser
import sys
from collections import Counter

class Helper:
    """
    Allows the user to filter through the store, add items to 
    their cart, and checkout 
    Attributes:
        warehouse (dict): Contains the items available in the store and it's information
        cart (dict): empty dictionary wih a customers cart
        departments(list): list of departments in the store
    """
    
    def __init__(self, store):
        """
        Initalize instance of Helper
        Side effects: 
            modifies warehouse, cart, and departments attributes
        """

        self.departments = ["Electronics", "Paper Products", "Dairy", "Bakery", "Furniture"]
        self.warehouse = store
        self.cart = {}    
        self.userDepartment={}
        
    def categories_search(self):
        """
        Allow the user to identify what item they are looking for

        Returns:
            returns a list of products from each category OR
            returns specific item detail of that option is selected
        Side Effects:
            prints different department selections
            prints each of the 6 items in chosen department   
        """        
        specific_search = input("Do you want to search for a specific item? (yes/no): ").strip().lower()
        if specific_search == "yes":
            self.item_attributes()
        if specific_search == "no":
            num = 0
            print("\nWhich department would you like to search")
            for item in self.departments:
                num += 1
                print(f"{num}: {item}")
            selection = int(input("Insert a number: "))
            if selection==1:
                self.userDepartment={1: ("iPhone 12", 999.99, "Aisle 1", "Electronics", 8), 
            2: ("Macbook Pro", 1299.29, "Aisle 1", "Electronics", 2),
            3: ('Samsung 60" TV', 799.99, "Aisle 2", "Electronics", 3), 
            4: ("iPad Pro", 599.99, "Aisle 1", "Electronics", 2),
            5: ("Apple Watch", 399.99, "Aisle 1", "Electronics", 1),
            6: ("Samsung S20", 899.99, "Aisle 2", "Electronics", 6)}
            elif selection==2:
                self.userDepartment={7: ("Blue Napkins", 6.99, "Aisle 4", "Paper Products", 10),
            8: ("White Paper Towels", 4.99, "Aisle 3", "Paper Products", 4),
            9: ("Birthday Paper Plates", 3.99, "Aisle 4", "Paper Products", 1),
            10: ("Red Napkins", 6.99, "Aisle 4", "Paper Products", 10),
            11: ("Brown Paper Bags", 2.99, "Aisle 3", "Paper Products", 5)}
            elif selection==3:
                self.userDepartment={12: ("2% Milk", 2.99, "Aisle 5", "Dairy", 18),
            13: ("Half & Half", 3.99, "Aisle 5", "Dairy", 6),
            14: ("Mozzarella Cheese", 2.99, "Aisle 5", "Dairy", 8),
            15: ("Yoplait Yogurt", 1.99, "Aisle 5", "Dairy", 28),
            16: ("Ben & Jerry's Ice Cream", 6.99, "Aisle 6", "Dairy", 7)}   
            elif selection==4:
                self.userDepartment={17: ("Thomas Bagels", 5.99, "Aisle 7", "Bakery", 10),
            18: ("Glazed Donuts", 7.99, "Aisle 6", "Bakery", 6),
            19: ("Birthday Cake", 27.99, "Aisle 6", "Bakery", 1),
            20: ("French Baguette", 5.99, "Aisle 7", "Bakery", 8),
            21: ("Sourdough Bread", 4.99, "Aisle 7", "Bakery", 6)}   
            elif selection==5:
                self.userDepartment={22: ("Kitchen Chair", 64.99, "Aisle 8", "Furniture", 4),
            23: ("Couch", 249.99, "Aisle 8", "Furniture", 2),
            24: ("Dining Table", 129.99, "Aisle 9", "Furniture", 1),
            25: ("Living Room Chair", 74.99, "Aisle 8", "Furniture", 8),
            26: ("School Desk", 119.99, "Aisle 9", "Furniture", 2)}              
            compare = self.departments[selection - 1]
            for key in self.warehouse:
                if compare == self.warehouse[key][3]:
                    nl = '\n'
                    print(f"Item:{self.warehouse[key][0]}{nl}") 
            self.price_search(selection)        
    
    def price_search(self, selection):
        """Allows customer to search by price of items of chosen category
        Parameters:
            selection(int): category number they are searching in
        Raises:
            ValueError: Value error is price is entered correctly
        Returns:
            items at given price within chose category OR
            proceeds onto narrow_categories    
        Side Effects:
            prints price range options    
        """     
        price_range_list = [ "<$5" , "$5-$29.99", "$30-$99.99", "$100-$800", ">$800"]
        price = input("Do you wish to narrow down your results by searching by price? (yes/no): ").strip().lower()
        num = 0
        if price == "yes":
            for number in price_range_list:
                num += 1
                print(f"{num}: {number}")
            price_range = int(input("Insert a number: "))            
            for item_price in self.userDepartment:
                if price_range == 1 and self.userDepartment[item_price][1] <5.0:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}\n")
                elif price_range == 2 and 5.0<=self.userDepartment[item_price][1]<=29.99:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}\n")
                elif price_range == 3 and 29.99<self.userDepartment[item_price][1]<=99.99:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}\n")
                elif price_range == 4 and 100.0<self.userDepartment[item_price][1]<=800.0:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}\n")            
                elif price_range == 5 and self.userDepartment[item_price][1] >800.0:
                  print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}\n")
        else:
            self.narrow_categories(selection)
        
                    
                      
    def narrow_categories(self, selection):
        """
        Prompts the user with questions to help narrow down options even further
        Args: 
            selection(int): category number they are searching in
        Returns:
            (list): list of possible items to browse determined by their answer to the questions
        """
        
        narrow = input("Would you like to narrow down the category you are searching in?(yes/no)")
        if narrow == "no" :
            self.item_attributes()
        if narrow == "yes" :
            if selection == 1 :
                brand = input("What brand are you looking for? ")
                if brand == "Apple" :
                    print(["iPhone 12", "iPad", "Macbook Pro", "Apple Watch"])
                elif brand == "Android" :
                    print(["Android"])
                elif brand == "Samsung" :
                    print(["Samsung TV"])
                else :
                    print("We do not have this brand in our inventory.")
                
                electronic_type = input("What type of electronic are you looking for? ")
                if electronic_type == "phone":
                    print(["iPhone", "Android"])
                elif electronic_type == "TV": 
                    print(["Samsung TV"])
                elif electronic_type == "Tablet" :
                    print(["iPad"])
                elif electronic_type == "Watch" :
                    print(["Apple Watch"])
                else :
                    print("We do not have this electronic type in our inventory.")
                
            if selection == 2 :
                color = input("What color of paper product are you looking for?")
                if color == "Blue" :
                    print(["Blue Napkins"])
                elif color == "White" :
                    print(["White Paper Towels"])
                elif color == "Brown" :
                    print(["Brown Paper Bags"])
                elif color == "Red" :
                    print(["Red Napkins"])
                elif color == "Multicolor" :
                    print(["Birthday Paper Plates"])
                else :
                    print("We do not have this color in our inventory.")
                
                paper_product_type = input("What type of paper product are you looking for?")
                if paper_product_type == "Napkins" :
                    print(["Blue Napkins", "Red Napkins"])
                elif paper_product_type == "Paper Towels":
                    print(["White Paper Towels"])
                elif paper_product_type == "Paper Bags" :
                    print(["Brown Paper Bags"])
                elif paper_product_type == "Plates" :
                    print(["Birthday Paper Plates"])
                else :
                    print("We do not have this paper product type in our inventory.")
                
                occasion = input("What type of occasion are you shopping for?")
                if occasion == "Birthday" :
                    print(["Birthday Paper Plates"])
                else :
                    print("We do not have this occasion in our inventory.")
                
            if selection == 3 :
                dairy_type = input("What type of dairy are you looking for?")
                if dairy_type == "Milk" :
                    print(["2% Milk", "Half and Half"])
                elif dairy_type == "Cheese" :
                    print(["Mozzarella Cheese"])
                elif dairy_type == "Yogurt" :
                    print(["Yoplait Yogurt"])
                elif dairy_type == "Ice Cream" :
                    print(["Ben and Jerry's Ice Cream"])
                else :
                    print("We do not have this dairy type in our inventory.")
                
                dairy_brand = input("What brand of dairy are you looking for?")
                if dairy_brand == "Yoplait" :
                    print(["Yoplait Yogurt"])
                elif dairy_brand == "Ben and Jerry's" :
                    print(["Ben and Jerry's Ice Cream"])
                else :
                    print("We do not have this brand in our inventory.")
                
            if selection == 4 :
                bakery_type = input("What type of baked good are you looking for?")
                if bakery_type == "Bagels" :
                    print(["Thomas Bagels"])
                elif bakery_type == "Donuts" :
                    print(["Glazed Donuts"])
                elif bakery_type == "Cake" :
                    print(["Birthday Cake"])
                elif bakery_type == "Bread" :
                    print(["French Baguette", "Sourdough Bread"])
                else :
                    print("We do not have this type of baked good in our inventory.")
            
                bakery_brand = input("What brand of baked good are you looking for?")
                if bakery_brand == "Thomas" :
                    print(["Thomas Bagels"])
                else :
                    print("We do not have this brand in our inventory.")
            
                bakery_occasion = input("What occasion are you shopping for?")
                if bakery_occasion == "Birthday" :
                    print(["Birthday Cake"])
                else :
                    print("We do not have this occasion in our inventory.")
                
            if selection == 5 :
                furniture_type = input("What furniture type are you looking for?")
                if furniture_type == "Chair" :
                    print(["Kitchen Chair", "Living Room Chair"])
                elif furniture_type == "Couch" :
                    print(["Couch"])
                elif furniture_type == "Table" :
                    print(["Dining Table", "School Desk"])
                else :
                    print("We do not have this furniture type in our inventory.")
            
                room = input("What room are you shopping for furniture for?")
                if room == "Kitchen" :
                    print(["Kitchen Chair"])
                elif room == "Dining Room" :
                    print(["Dining Table"])
                elif room == "Living Room" :
                    print(["Living Room Chair"])
                else :
                    print("We do not have this room in our inventory.")
                                    
    def item_attributes(self):
        """
        Ask the user what item they are searching for and shows the user the information of the item they chose
        Raises:
            ValueError: raised if an item doesn't exist in the store
        Returns:
            str of item information
        """
        item = input("What item are you searching for?")
        for key in self.warehouse :
            if item == self.warehouse[key][0] :
                print(f"{item} is ${self.warehouse[key][1]} and you can find it in {self.warehouse[key][2]} in the {self.warehouse[key][3]} Department. We currently have {self.warehouse[key][4]} in stock.")
            else: 
                raise ValueError("This item does not exist in the store.")
        
    def suggestions(self):
        """
        Purpose is to look at items in the customer's cart and recommend them 
        items to purchase that are frequently bought together
        Parameters: (dict) cart - items on cart, along with their corresponding attributes (price, aisle, department, # in stock) 
        Raises:
            ValueError: Value error if a suggested item is out of stock
        Returns:
            (list) List of suggested items to purchase
        """        
        count = []
        for i in self.cart:
            count.append(self.cart[i][3])
        x = Counter(count)
        maxdep = max(count, key=x.get)

        all_items = [self.warehouse[item][0] for item in self.warehouse
                        if maxdep == self.warehouse[item][3]]
        all_items = set(all_items)

        cart_items = [self.cart[c][0] for c in self.cart 
                        if maxdep == self.cart[c][3]]
        cart_items = set(cart_items)

        suggestions = all_items.difference(cart_items)

        if len(suggestions) > 0:
            print("SUGGESTED ITEMS:\n")
            for s in suggestions:
                print(f"{s}")
        
    def check_cart(self):
        """
        Purpose is to get a summary of what is currently in a user's cart and display to user
        Parameters: none
        Returns: none
        Side effects: prints to console        
        """        
        #example format: Item#: toilet paper, Price: $2:99, Aisle: 6, Department: example, # In Stock: 5
        
        for item in self.cart:
            print (f"item: {self.cart[item][0]}, price: {self.cart[item][1]}") 
            print (f"aisle: {self.cart[item][2]}, department: {self.cart[item][3]}, stock: {self.cart[item][4]}")
        
    def cart_total(self):
        """
        Purpose is to add up the cost of all items in a customer's cart and show them
        Parameters: (dict) cart - items on cart, along with their corresponding attributes (price, aisle, department, # in stock) 
        Raises:
            ValueError: if total cost is less than 0
        Returns:
            float of the final total cost"""
        
        total = 0
        for i in self.cart:
            total += self.cart[i][1]
        
        print(f"Your total is {total}")
        
    def add_to_cart(self, itemNum):
        """
        Purpose is to add item to cart
        Parameters: (int) itemNum - number for identifying item
        Returns: none
        Side effects: changes self.cart
        """
        self.cart[len(self.cart)+1]=store[itemNum] 
        
        
    
        
def create_store():
    """
    Purpose is to create the warehouse with items and their information in a dictionary
    Parameters: none
    Returns:  dictionary with warehouse items
    Side effects: none
    """    
    return {1: ("iPhone 12", 999.99, "Aisle 1", "Electronics", 8), 
            2: ("Macbook Pro", 1299.29, "Aisle 1", "Electronics", 2),
            3: ('Samsung 60" TV', 799.99, "Aisle 2", "Electronics", 3), 
            4: ("iPad Pro", 599.99, "Aisle 1", "Electronics", 2),
            5: ("Apple Watch", 399.99, "Aisle 1", "Electronics", 1),
            6: ("Samsung S20", 899.99, "Aisle 2", "Electronics", 6),
            7: ("Blue Napkins", 6.99, "Aisle 4", "Paper Products", 10),
            8: ("White Paper Towels", 4.99, "Aisle 3", "Paper Products", 4),
            9: ("Birthday Paper Plates", 3.99, "Aisle 4", "Paper Products", 1),
            10: ("Red Napkins", 6.99, "Aisle 4", "Paper Products", 10),
            11: ("Brown Paper Bags", 2.99, "Aisle 3", "Paper Products", 5),
            12: ("2% Milk", 2.99, "Aisle 5", "Dairy", 18),
            13: ("Half & Half", 3.99, "Aisle 5", "Dairy", 6),
            14: ("Mozzarella Cheese", 2.99, "Aisle 5", "Dairy", 8),
            15: ("Yoplait Yogurt", 1.99, "Aisle 5", "Dairy", 28),
            16: ("Ben & Jerry's Ice Cream", 6.99, "Aisle 6", "Dairy", 7),
            17: ("Thomas Bagels", 5.99, "Aisle 7", "Bakery", 10),
            18: ("Glazed Donuts", 7.99, "Aisle 6", "Bakery", 6),
            19: ("Birthday Cake", 27.99, "Aisle 6", "Bakery", 1),
            20: ("French Baguette", 5.99, "Aisle 7", "Bakery", 8),
            21: ("Sourdough Bread", 4.99, "Aisle 7", "Bakery", 6),
            22: ("Kitchen Chair", 64.99, "Aisle 8", "Furniture", 4),
            23: ("Couch", 249.99, "Aisle 8", "Furniture", 2),
            24: ("Dining Table", 129.99, "Aisle 9", "Furniture", 1),
            25: ("Living Room Chair", 74.99, "Aisle 8", "Furniture", 8),
            26: ("School Desk", 119.99, "Aisle 9", "Furniture", 2)}         

def find_location(store):
    """Guides the user to find the item they want
    Args:
        store (dict): warehouse items"""
    
    departments = ["Electronics", "Paper Products", "Dairy", "Bakery", "Furniture"]
    num = 0
    print("\nWhich department would you like to search")
    for item in departments:
        num += 1
        print(f"{num}: {item}")
    selection = int(input("Insert a number: "))
    
    compare = departments[selection - 1]
    finder = {}
    for key in store:
        if compare == store[key][3]:
            finder[store[key][0]] = store[key][2]
    print("\n")        
    for k in finder:
        print(f"Check {finder[k].lower()} for {k}")

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("action", type=str,
                        help="'find' to find an item or 'store' to purchase items")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    store = create_store()
    if args.action == "find":
        find_location(store)
    elif args.action == "store":
        user = Helper(store)
        user.categories_search()
    else: 
        raise ValueError("Type either find or store")