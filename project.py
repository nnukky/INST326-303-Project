"""
INST 326 Final Project
Purpose is to create a warehouse and allow users to locate products and view other features associated with them.
"""

class Helper:
    """
    The purpose of this class is to help a user identify and locate items that they are looking for in our fictional warehouse.
    Attributes:
        warehouse (dict) : This is a dictionary that identifies the item name (ex: whole milk) as the key and a tuple of its attributes (ex: $2.99, 3 in stock, dairy, aisle 5) as the value.
    
    """
    def __init__(self):
        """The Purpose of this method is to initilize new attributes"""
        #self.warehouse = {}
        #self.cart = {}
        #self.price = float
        #self.category = category
        #self.item = item
        
    def categories_search(self):
        """The purpose of this method is to help get the user to identitify 
        what item they are looking for
        
        Attributes:
            categories(dict): Gives the user an option to choose between 5 general categories of the warehouse store which consists of electronics, paper products, dairy, bakery, and furniture

        Return:
            #retun list of 4 products from each category
         """
         #Ask user if they would like to search for a specific product or choose from our list of categories
         #If user answers yes to type in specific product, take them to the product
         #If user answers no, prompt user to pick from selected categories
         #return 4 products from the specific category
         
    def price_search(self):
        """The purpose of this funtion is to allow a customer to search by price of items
        
        Attributes:
            self.price(dict): Dictionary mapped to price of goods
        
        Raises:
            ValueError: Value error is price is entered correctly
        """     
        #optional price option from list of 4 products from specific category
        #return all items at that price
         
         
    def narrow_categories(self, category) :
        """ Prompts the user with questions to help narrow down their item options even farther
        Args: 
            category (str) : the name of the category they are searching in
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
        """ This method will return the attributes of the item that the user is searching for.
        Args :
            item (str) : the name of the item being searched
        Raises :
            ValueError: raised if an item does not exist in the store
        """
        # pull information such as price, aisle, department and amount in stock related to the searched item from the database
        # will return this information to the user
        
    
    def suggestions(self):
        """
        This method will look at items in the customer's cart and recommend them 
        items to purchase that are frequently bought together
        Raises:
            ValueError: Value error if a suggested item is out of stock
        Returns:
            List of suggested items to purchase
        """
        
    def cart_total(self):
        """
        Add up the cost of all items in a customer's cart and show them
        Raises:
            ValueError: if total cost is less than 0
        Returns:
            float of the final total cost
        """
    def create_store(self):
        """
        Purpose is to create the warehouse along with the items, prices, aisles, departments, and amount in stock
        Returns: (dict) warehouse - dict of tuples that contain with key as item name and values (price, aisle, department, #in stock) in tuple
        Side Effects: none
        """
        #example format: {item1:(price, aisle, department, # in stock), item2:...}
    def check_cart(self, item, price):
        """
        Purpose is to get a summary of what is currently in user's cart
        Parameters:
            (str) item
            (float) price
        Returns: none
        Side Effects: Prints to console
        """    
        #example format: Item: toilet paper, Price: $2:99, Aisle: 6, Department: example, # In Stock: 5