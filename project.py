"""
INST 326 Final Project
Purpose is to create a warehouse and allow users to locate products and view other features associated with them.
"""

class Helper:
    """
    The purpose of this class is to help a user identify and locate items that they are looking for in our fictional warehouse.
    Attributes:
    
    """
    def __init__(self):
        """The Purpose of this method is to initilize new attributes"""
        
        
    def categories(self):
        """The purpose of this method is to help get the user to identitify 
        what item they are looking for
        
        Attributes:
            general_categories(list or dict): Gives the user an option to choose between 5 general categories of the warehouse store which consists of electronics, paper products, dairy, bakery, and furniture
            
         """
         #Ask user if they would like to search for a specific product or choose from our list of categories
         #If user answers yes to type in specific product, take them to the product
         #If user answers no, prompt user to pick from selected categories
         
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
    
    def item_attributes(self) :
        """ This method will return the attributes of the item that the user is searching for.
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
        """
        
    def cart_total(self):
        """
        
        """
    def create_store(self):
        """
        Purpose is to create the warehouse along with the items, prices, aisles, departments, and amount in stock
        Parameters: none
        Returns: (list) warehouse - list of tuples that contain each item, price, aisle, department, and amount in stock
        Side Effects: none
        """
    def check_cart(self, item, price):
        """
        Purpose is to get a summary of what is currently in user's cart
        Parameters:
            (str) item
            (float) price
        Returns: none
        Side Effects: Prints to console
        """    
     