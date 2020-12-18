# INST326-303-Project

Our peoject represents a warehouse store where a user will be able to 
find an items location, search the store for a specific item, or add
items to your cart.

There is a required argument when running the project.py file from the 
terminal. You can either type 'store', 'find', or 'buy'. The explanation
of what each argument will do is provided below

-- BUY -- 
To buy an item after knowing its item ID, simply type 'python project.py buy'. Next, enter the item ID you would like to purchase. After entering an item ID, you will be shown what is in your cart along with the total price, as well as a list of suggested items. You may continue to buy items until you do not wish to buy anymore.
-- STORE --
To search for specific items, type 'python project.py store'. Next, you can either search an item directly by name, or search inside a department. If you choose a department, you can narrow your search results even further by price range. If you choose not to narrow your search results by price, you are asked if you would like to narrow down your product using other methods. If you choose to do so, you are prompted with questions such as brand and type of product.
-- FIND --
To find the general item list based on department, type 'python project.py find'. Next, enter the number of the department you are looking for in the list that pops up. You will then be shown a list of the aisles where you can find the items in your chosen department.

Annotated Bibliography

Lynn, S. (2019, February 13). Python Pandas read_csv – Load Data from CSV Files. Retrieved December 16, 2020, from https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/ This source was used to help us convert a CSV file into a dataframe using Pandas. This was used in create_store

Lopez, O. (2015, September 28). How to get the difference between two dictionaries in Python? Retrieved from https://stackoverflow.com/questions/32815640/how-to-get-the-difference-between-two-dictionaries-in-python
This source was used to help find the difference between two dictionaries. It was used in suggestions. 

Riley, A. (2014, November 03). Convert a Pandas DataFrame to a dictionary. Retrieved December 16, 2020, from https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary This source was used to help us convert a dataframe into a dictionary. This was used in create_store.