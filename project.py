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
    
    def categories_search(self, store):
        """
        Allow the user to identify what item they are looking for
        Raises:
            Type Error: raised if value isn't in correctly
        Returns:
            returns a list of products from each category OR
            returns specific item detail of that option is selected
        """
        
        specific_search = input("Do you want to search for a specific item? (yes/no)").strip().lower()
        if specific_search == "yes":
            product = input("What product do you wish to search for?")
            for key in store:
                if product == [store[key][0]]:
                    print(f"{product}: cost={[store[key][1]]}, aisle={[store[key][2]]}, department={[store[key][3]]}")
        
        if specific_search == "no":
            num = 0
            print("\nWhich department would you like to search")
            for item in self.departments:
                num += 1
                print(f"{num}: {item}")
            selection = int(input("Insert a number: "))
            compare = self.departments[selection - 1]
            for key in store:
                if compare == [store[key][3]]:
                    nl = '\n'
                    print(f"item:{nl}{[store[key][0]]}") 
        
            

        
    def narrow_categories(self, category):
        """
        Prompts the user with questions to help narrow down options even further
        Args: 
            category(str): category name they are searching in
        Returns:
            wouldn't this return an item?*** not sure though - luis
        """
        
        # First asks a user if they would like to search for a specific product after they browsed their options returned in the last method
        # If the user answers yes, take them to that item
        # If the user answers no, they will be prompted with different questions based on the category they have chosen
        # Electronics: What brand? What type?
        # Paper Products: Color? What type? Special Event?
        # Dairy: What type? Brand?
        # Bakery: What type? Brand?
        # Furniture: What size? Color? Room type?
        
        if category == "Electronics":
            brand = input("What brand are you looking for? ")
            if brand == "Apple" :
                return ["iPhone", "iPad", "Macbook"]
            electronic_type = input("What type of electronic are you looking for? ")
            if electronic_type == "phone":
                return ["iPhone", "Android", "Blackberry"]
        
    def item_attributes(self, item):
        """
        Show the user the information of the item they chose
        Args:
            item(str): name of the item they searched
        Raises:
            ValueError: raised if an item doesn't exist in the store
        Returns:
            str of item information
        """
        
        return self.warehouse[item]
        
        # pull information such as price, aisle, department and amount in stock related to the searched item from the database
        # will return this information to the user
        
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
        Get a summary of what is currently in a user's cart
        you dont need a cart parameter, u could just use self.cart - luis
        """
        
        #example format: Item#: toilet paper, Price: $2:99, Aisle: 6, Department: example, # In Stock: 5
        
        for item in self.cart:
            print (f"item: {self.cart[item][0]}, price: {self.cart[item][1]}, aisle: ") 
            print (f"{self.cart[item][2]}, department: {self.cart[item][3]}, stock: {self.cart[item][4]}")
        
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


def create_store():
    """Creates the warehouse with items and it's 
    information in a dictionary
    Returns: 
        dictionary with warehouse items"""
    
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
        user.categories_search
    else: 
        raise ValueError("Type either find or store")