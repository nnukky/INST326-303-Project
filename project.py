"""
INST 326 Final Project
Purpose is to create a fictional warehouse and allow users to locate 
products and view other features associated with them.
"""

from argparse import ArgumentParser
import sys
from collections import Counter
import pandas as pd

class Helper:
    """
    Allows the user to filter through the store, add items to 
    their cart, and checkout 
    Attributes:
        warehouse (dict): Contains the items available in the store and its information
            - format: {Item ID: [Item Name, Price, Aisle #, Department, # in stock, item id]}
            - datatypes: {int: list[str, float, str, str, int, int]}
        cart (dict): dictionary wih a customers cart
            - format: {Item ID: [Item Name, Price, Aisle #, Department, # in stock, item id]}
            - datatypes: {int: list[str, float, str, str, int, int]}
        departments(list): list of departments in the store
            - datatypes: [str, str, str, str, str]
    """
    
    def __init__(self, store):
        """
        Purpose to initalize instance of Helper
        Parameters(dict): store - where all store data comes from
        Returns: none
        Side effects: 
            modifies warehouse, cart, and departments attributes
        """

        self.departments = ["Electronics", "Paper Products", "Dairy", "Bakery", "Furniture"]
        self.warehouse = store
        self.cart = {}    
        self.userDepartment={}
        
    def categories_search(self):
        """
        Purpose to allow the user to identify what item they are looking for
        Parameters: none
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
                self.userDepartment={1: ("iPhone 12", 999.99, "Aisle 1", "Electronics", 8, 1), 
            2: ("Macbook Pro", 1299.29, "Aisle 1", "Electronics", 2, 2),
            3: ('Samsung 60" TV', 799.99, "Aisle 2", "Electronics", 3, 3), 
            4: ("iPad Pro", 599.99, "Aisle 1", "Electronics", 2, 4),
            5: ("Apple Watch", 399.99, "Aisle 1", "Electronics", 1, 5),
            6: ("Samsung S20", 899.99, "Aisle 2", "Electronics", 6, 6)}
            elif selection==2:
                self.userDepartment={7: ("Blue Napkins", 6.99, "Aisle 4", "Paper Products", 10, 7),
            8: ("White Paper Towels", 4.99, "Aisle 3", "Paper Products", 4, 8),
            9: ("Birthday Paper Plates", 3.99, "Aisle 4", "Paper Products", 1, 9),
            10: ("Red Napkins", 6.99, "Aisle 4", "Paper Products", 10, 10),
            11: ("Brown Paper Bags", 2.99, "Aisle 3", "Paper Products", 5, 11)}
            elif selection==3:
                self.userDepartment={12: ("2% Milk", 2.99, "Aisle 5", "Dairy", 18, 12),
            13: ("Half & Half", 3.99, "Aisle 5", "Dairy", 6, 13),
            14: ("Mozzarella Cheese", 2.99, "Aisle 5", "Dairy", 8, 14),
            15: ("Yoplait Yogurt", 1.99, "Aisle 5", "Dairy", 28, 15),
            16: ("Ben & Jerry's Ice Cream", 6.99, "Aisle 6", "Dairy", 7, 16)}   
            elif selection==4:
                self.userDepartment={17: ("Thomas Bagels", 5.99, "Aisle 7", "Bakery", 10, 17),
            18: ("Glazed Donuts", 7.99, "Aisle 6", "Bakery", 6, 18),
            19: ("Birthday Cake", 27.99, "Aisle 6", "Bakery", 1, 19),
            20: ("French Baguette", 5.99, "Aisle 7", "Bakery", 8, 20),
            21: ("Sourdough Bread", 4.99, "Aisle 7", "Bakery", 6, 21)}   
            elif selection==5:
                self.userDepartment={22: ("Kitchen Chair", 64.99, "Aisle 8", "Furniture", 4, 22),
            23: ("Couch", 249.99, "Aisle 8", "Furniture", 2, 23),
            24: ("Dining Table", 129.99, "Aisle 9", "Furniture", 1, 24),
            25: ("Living Room Chair", 74.99, "Aisle 8", "Furniture", 8, 25),
            26: ("School Desk", 119.99, "Aisle 9", "Furniture", 2, 26)}              
            compare = self.departments[selection - 1]
            for key in self.warehouse:
                if compare == self.warehouse[key][3]:
                    nl = '\n'
                    print(f"Item:{self.warehouse[key][0]} (ID: {self.warehouse[key][5]}){nl}") 
            self.price_search(selection)        
    
    def price_search(self, selection):
        """
        Purpose to allow customer to search by price of items of chosen category
        Parameters:
            selection(int): category number they are searching in
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
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}:ID {self.userDepartment[item_price][5]}\n")
                elif price_range == 2 and 5.0<=self.userDepartment[item_price][1]<=29.99:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}:ID {self.userDepartment[item_price][5]}\n")
                elif price_range == 3 and 29.99<self.userDepartment[item_price][1]<=99.99:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}:ID {self.userDepartment[item_price][5]}\n")
                elif price_range == 4 and 100.0<self.userDepartment[item_price][1]<=800.0:
                    print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}:ID {self.userDepartment[item_price][5]}\n")            
                elif price_range == 5 and self.userDepartment[item_price][1] >800.0:
                  print(f"Item:{self.userDepartment[item_price][0]}:${self.userDepartment[item_price][1]}:ID {self.userDepartment[item_price][5]}\n")
        else:
            self.narrow_categories(selection)
          
                      
    def narrow_categories(self, selection):
        """
        Purpose to prompt the user with questions to help narrow down options even further
        Args: 
            selection(int): category number they are searching in
        Side effects: 
            prints list of possible items to browse determined by their answer to the questions to stdout
        """        
        narrow = input("Would you like to narrow down the category you are searching in? (yes/no) ")
        if narrow == "no" :
            self.item_attributes()
        if narrow == "yes" :
            if selection == 1 :
                brand = input("What brand are you looking for? ")
                if brand == "Apple" :
                    print(["iPhone 12 (ID 1)", "iPad (ID 4)", "Macbook Pro (ID 2)", "Apple Watch (ID 5)"])
                elif brand == "Samsung" :
                    print(["Samsung TV (ID 3)"])
                else :
                    print("We do not have this brand in our inventory.")
                
                electronic_type = input("What type of electronic are you looking for? ")
                if electronic_type == "phone":
                    print(["iPhone (ID 1)"])
                elif electronic_type == "TV": 
                    print(["Samsung TV  (ID 3)"])
                elif electronic_type == "Tablet" :
                    print(["iPad (ID 4)"])
                elif electronic_type == "Watch" :
                    print(["Apple Watch (ID 5)"])
                else :
                    print("We do not have this electronic type in our inventory.")
                
            if selection == 2 :
                color = input("What color of paper product are you looking for? ")
                if color == "Blue" :
                    print(["Blue Napkins (ID 7)"])
                elif color == "White" :
                    print(["White Paper Towels (ID 8)"])
                elif color == "Brown" :
                    print(["Brown Paper Bags (ID 11)"])
                elif color == "Red" :
                    print(["Red Napkins (ID 10)"])
                elif color == "Multicolor" :
                    print(["Birthday Paper Plates (ID 9)"])
                else :
                    print("We do not have this color in our inventory.")
                
                paper_product_type = input("What type of paper product are you looking for? ")
                if paper_product_type == "Napkins" :
                    print(["Blue Napkins (ID 7)", "Red Napkins (ID 10)"])
                elif paper_product_type == "Paper Towels":
                    print(["White Paper Towels (ID 8)"])
                elif paper_product_type == "Paper Bags" :
                    print(["Brown Paper Bags (ID 11)"])
                elif paper_product_type == "Plates" :
                    print(["Birthday Paper Plates (ID 9)"])
                else :
                    print("We do not have this paper product type in our inventory.")
                
                occasion = input("What type of occasion are you shopping for? ")
                if occasion == "Birthday" :
                    print(["Birthday Paper Plates (ID 9)"])
                else :
                    print("We do not have this occasion in our inventory.")
                
            if selection == 3 :
                dairy_type = input("What type of dairy are you looking for? ")
                if dairy_type == "Milk" :
                    print(["2% Milk (ID 12)", "Half and Half (ID 13)"])
                elif dairy_type == "Cheese" :
                    print(["Mozzarella Cheese (ID 14)"])
                elif dairy_type == "Yogurt" :
                    print(["Yoplait Yogurt (ID 15)"])
                elif dairy_type == "Ice Cream" :
                    print(["Ben and Jerry's Ice Cream (ID 16)"])
                else :
                    print("We do not have this dairy type in our inventory.")
                
                dairy_brand = input("What brand of dairy are you looking for? ")
                if dairy_brand == "Yoplait" :
                    print(["Yoplait Yogurt (ID 15)"])
                elif dairy_brand == "Ben and Jerry's" :
                    print(["Ben and Jerry's Ice Cream (ID 16)"])
                else :
                    print("We do not have this brand in our inventory.")
                
            if selection == 4 :
                bakery_type = input("What type of baked good are you looking for? ")
                if bakery_type == "Bagels" :
                    print(["Thomas Bagels (ID 17)"])
                elif bakery_type == "Donuts" :
                    print(["Glazed Donuts (ID 18)"])
                elif bakery_type == "Cake" :
                    print(["Birthday Cake (ID 19)"])
                elif bakery_type == "Bread" :
                    print(["French Baguette (ID 20)", "Sourdough Bread (ID 21)"])
                else :
                    print("We do not have this type of baked good in our inventory.")
            
                bakery_brand = input("What brand of baked good are you looking for? ")
                if bakery_brand == "Thomas" :
                    print(["Thomas Bagels (ID 17)"])
                else :
                    print("We do not have this brand in our inventory.")
            
                bakery_occasion = input("What occasion are you shopping for? ")
                if bakery_occasion == "Birthday" :
                    print(["Birthday Cake (ID 19)"])
                else :
                    print("We do not have this occasion in our inventory.")
                
            if selection == 5 :
                furniture_type = input("What furniture type are you looking for? ")
                if furniture_type == "Chair" :
                    print(["Kitchen Chair (ID 22)", "Living Room Chair (ID 25)"])
                elif furniture_type == "Couch" :
                    print(["Couch (ID 23)"])
                elif furniture_type == "Table" :
                    print(["Dining Table (ID 24)", "School Desk (ID 26)"])
                else :
                    print("We do not have this furniture type in our inventory.")
            
                room = input("What room are you shopping for furniture for? ")
                if room == "Kitchen" :
                    print(["Kitchen Chair (ID 22)"])
                elif room == "Dining Room" :
                    print(["Dining Table (ID 24)"])
                elif room == "Living Room" :
                    print(["Living Room Chair (ID 25)"])
                else :
                    print("We do not have this room in our inventory.")
                                    
    def item_attributes(self):
        """
        Purpose to ask the user what item they are searching for and shows the user the information of the item they chose
        Raises:
            ValueError: raised if an item doesn't exist in the store    
        Side effects:    
            prints string of item information to stdout
        """
        item = input("What item are you searching for? ")
        for key in self.warehouse:
            if item in self.warehouse[key][0] :
                print(f"{item} is ${self.warehouse[key][1]} with ID {self.warehouse[key][5]} and you can find it in {self.warehouse[key][2]} in the {self.warehouse[key][3]} Department. We currently have {self.warehouse[key][4]} in stock.")
                break 
        else: 
            raise ValueError("This item does not exist in the store.")
        
    def suggestions(self):
        """
        Looks at which department appears in their cart the most and recommends
        other items in the same department that are not in their cart yet
        Side effects: 
            prints suggested items depending on what is currently in their cart
            to the terminal
        """        
        count = []
        for i in self.cart:
            count.append(self.cart[i][3])
        x = Counter(count)
        maxdep = max(count, key=x.get)

        all_items = {}
        for i in self.warehouse:
            if maxdep == self.warehouse[i][3]:
                all_items[self.warehouse[i][5]] = self.warehouse[i][0]
        
        cart_items = {}
        for it in self.cart:
            if maxdep == self.cart[it][3]:
                cart_items[self.cart[it][5]] = self.cart[it][0]
        
        suggestions = {k: all_items[k] for k in set(all_items) - set(cart_items)}
        
        if len(suggestions) > 0:
            print("\nSUGGESTED ITEMS:")
            for s in suggestions:
                print(f"{suggestions[s]} (ID: {s})")
        
    def check_cart(self):
        """
        Purpose is to get a summary of what is currently in a user's cart and display to user
        Parameters: none
        Returns: (dict) self.cart
        Side effects: prints to console a message consisting of all items and prices currently in user's cart        
        """              
        print("Your cart currently has...")
        for item in self.cart:
            print (f"item: {self.cart[item][0]}, price: ${self.cart[item][1]}, ID:{self.cart[item][5]}") 
        return self.cart               
        
    def cart_total(self):
        """
        Adds up the cost of all items in a customer's cart and shows them
        Side effects: 
            prints total cost of a user's cart to the terminal
        Returns:
            float of the final total cost  
            """
        
        total = 0
        for i in self.cart:
            total += self.cart[i][1]
        
        print(f"\nYour total is ${round(total, 2)}")
        return round(total, 2)
        
    def add_to_cart(self, itemNum):
        """
        Purpose is to add item to cart
        Parameters: (int) itemNum - number for identifying item
        Returns: (dict) self.cart
        Side effects: updates self.cart
        """
        self.cart[int(itemNum)]=self.warehouse[int(itemNum)]  
        return self.cart[int(itemNum)]     
        
def create_store():
    """
    Purpose is to create the warehouse with items from CSV and store their information in a dictionary
    This is where all data comes from!
    Parameters: none
    Returns:  dictionary with warehouse items
    Side effects: none
    """    
    df=pd.read_csv("data.csv")
    return df.set_index('ID').T.to_dict('list')    

def find_location(store):
    """
    Purpose to guide the user to find the item they want
    Args:
        store (dict): warehouse items
    Returns: none
    Side effects: prints  to console    
        """
    
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
            finder[key] = (store[key][0], store[key][2])
    print("\n")        
    for k in finder:
        print(f"Check {finder[k][1].lower()} for {finder[k][0]} (ID: {k})")

def parse_args(arglist):
    """ 
    Purpose to parse command-line arguments.
    Parameters: (list) arglist - list of arguments
    Returns: namespace with action
    Side effects: none    
    """
    parser = ArgumentParser()
    parser.add_argument("action", type=str,
                        help="'find' to find an item location, 'store' to find items, or 'buy' to purchase items")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    store = create_store()
    user = Helper(store)
    if args.action == "find":
        find_location(store)
    elif args.action == "store":        
        user.categories_search()
    elif args.action == "buy":
        itemId=input("Enter the item ID you want to add to cart: ")
        user.add_to_cart(itemId) 
        user.check_cart()
        user.suggestions()
        buyAnother=input("\nBuy more? (yes/no): ")
        while buyAnother=="yes":            
            itemId=input("Enter the item ID you want to add to cart: ")
            user.add_to_cart(itemId) 
            user.check_cart()
            user.suggestions()
            user.cart_total()  
            buyAnother=input("Buy more? (yes/no): ")
        user.cart_total()
                
    else: 
        raise ValueError("Type either find, store, or buy")