"""
INST 326 Final Project
Purpose is to create a fictional warehouse and allow users to locate products and view other features associated with them.
"""

class Helper:
    """
    The purpose of this class is to help a user identify and locate items that they are looking for in our fictional warehouse.
    Attributes:
        warehouse (dict) : This is a dictionary that identifies the item name (ex: whole milk) as the key and a tuple of its attributes (ex: $2.99, 3 in stock, dairy, aisle 5) as the value.
        cart (dict) : This dictionary contains item information of the items currently on user's cart
        price (float) : price of item
        category (str) : category of item (electronics, paper products, dairy, bakery, or furniture)
        item (str) : name of item
    
    """
    def __init__(self):
        """
        The Purpose of this method is to initilize new attributes
        Parameters: none
        Returns: none
        Side effects: none
        """
        #self.warehouse = {}
        #self.cart = {}
        #self.price = price
        #self.category = category
        #self.item = item
        
    def categories_search(self):
        """
        The purpose of this method is to help get the user to identitify 
        what item they are looking for
        
        Parameters:
            warehouse(dict): Gives the user an option to choose between 5 general categories of the warehouse store which consists of electronics, paper products, dairy, bakery, and furniture

        Return:
            #return list of 4 products from each category
            or
            #return specific item detail of that option is selected
        Side effects: none    
         """
         #Ask user if they would like to search for a specific product or choose from our list of categories
         #If user answers yes to type in specific product, take them to the product
         #If user answers no, prompt user to pick from selected categories
         #return 4 products from the specific category
         
    def price_search(self):
        """The purpose of this funtion is to allow a customer to search by price of items
        
        Parameters:
            self.price(dict): Dictionary mapped to price of goods
        
        Raises:
            ValueError: Value error is price is entered correctly
        
        Returns:
            #items at specific price    
        """     
        #optional price option from list of products from specific category
        #return all items at that price within the specific category
        #if they don't wish to search by price it will go to next method
         
         
    def narrow_categories(self, category) :
        """ 
        Purpose is to prompt the user with questions to help narrow down their item options even farther
        Parameters: 
            category (str) : the name of the category they are searching in
        Returns: none
        Side effects: 
            prints to console         
        """
        # First asks a user if they would like to search for a specific product after they browsed their options returned in the last method
        # If the user answers yes, take them to that item
        # If the user answers no, they will be prompted with different questions based on the category they have chosen
        # Electronics: What brand? What type?
        # Paper Products: Color? What type? Special Event?
        # Dairy: What type? Brand?
        # Bakery: What type? Brand?
        # Furniture: What size? Color? Room type?
    
    def item_attributes(self, item) :
        """ 
        Purpose is to return the attributes of the item that the user is searching for.
        Parameters :
            item (str) : the name of the item being searched
        Raises :
            ValueError: raised if an item does not exist in the store
        Returns: 
            (str) item information   
        """
        # pull information such as price, aisle, department and amount in stock related to the searched item from the database
        # will return this information to the user
        
    
    def suggestions(self):
        """
        Purpose is to look at items in the customer's cart and recommend them 
        items to purchase that are frequently bought together
        Parameters: none
        Raises:
            ValueError: Value error if a suggested item is out of stock
        Returns:
            (list) List of suggested items to purchase
        """
        #Looks at the department of items in their cart and recommend items based on what's in their cart.
        
    def create_store(self):
        """
        Purpose is to create the warehouse along with the items, prices, aisles, departments, and amount in stock
        Parameters: none
        Returns: 
            (dict) warehouse - dict of tuples that contain with key as item name and values (price, aisle, department, #in stock) in tuple
        Side Effects: none
        """
        #example format: {item1:(price, aisle, department, # in stock), item2:...}
    def check_cart(self, cart):
        """
        Purpose is to get a summary of what is currently in user's cart
        Parameters: 
            (dict) cart - items on cart, along with their corresponding attributes (price, aisle, department, # in stock) 
        Returns: none
        Side Effects: 
            Prints to console
        """    
        #example format: Item: toilet paper, Price: $2:99, Aisle: 6, Department: example, # In Stock: 5
        
    def cart_total(self):
        """
        Purpose is to add up the cost of all items in a customer's cart and show them
        Parameters: none
        Raises:
            ValueError: if total cost is less than 0
        Returns:
            float of the final total cost"""
            
        #Look at the items(and quantity) of a customer's cart to find out the total price