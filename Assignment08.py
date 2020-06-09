# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# cleung,06.06.2020, Modified code to complete assignment 8
# cleung,06.07.2020, Added main body of script of assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        """
    # --Fields--
    ProductName = ""
    ProductPrice = ""

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.ProductName = product_name
        self.ProductPrice = product_price

    # -- Properties --
    # product_name
    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, name):
        if name.isnumeric() == False:
            self.__product_name = name
        else:
            raise Exception("Product can't be Numbers")

    # product_price
    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        if value.isalpha() == False:
            self.__product_price = value
        else:
            raise Exception("Price can't be Letters")

    # -- Methods --
    # End of class

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)
    """

    @staticmethod
    def read_data_from_file(file_name):
        list_of_product_objects = []
        try:
            file = open(file_name,"r")
            for line in file:
                data = line.split('\t')
                product_name = data[0]
                product_price = data[1]
            file.close()
            return list_of_product_objects
        except FileNotFoundError:
            print("File", file_name, "Currently doesn't exist.")
            return list_of_product_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name,'w')
        for objProduct in list_of_product_objects:
            file.write("Product: " + objProduct.ProductName + "\t Price: $" + str(objProduct.ProductPrice))
        file.close()
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    def DisplayMenu():
        """ Display menu to user
        :return: none
        """
        print('''
    *************************************
               Menu Options
       1) Display Current Data
       2) Add New Product & Price
       3) Save Product & Price and Exit
    *************************************
            ''')

    @staticmethod
    def UserChoice():
        """ Asks for User's Choice
        :return: (str) user choice
        """
        strChoice = input("Choose an Option [1 to 3]: ")
        return strChoice

    @staticmethod
    def DisplayProductandPrice(list_of_product_objects):
        """ Displays Current Data
        :return: nothing
        """
        print("\t***** Current Products & Prices *****")
        for objProduct in list_of_product_objects:
            print("Product: " + objProduct.ProductName + "\t Price: $" + str(objProduct.ProductPrice))
        print("\t*************************************")

    @staticmethod
    def AddProductandPrice():
        """ User Adds New Product and Price
        :return: (str) Product Name & Price
        """
        product = input("Enter Product: ")
        while True:
            try:
                price = float(input("Enter Price: $"))
                break
            except ValueError:
                print("Try Again: price must use numbers")
                continue
        return Product(product,price)
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts\

# Show user a menu of options
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
while True:
    IO.DisplayMenu()
    # Get user's menu option choice
    strChoice = IO.UserChoice()
    # Show user current data in the list of product objects
    if (strChoice.strip() == "1"):
        try:
            IO.DisplayProductandPrice(lstOfProductObjects)
        except ValueError as e:
            print(e)
        continue

    # Let user add data to the list of product objects
    elif (strChoice.strip() == "2"):
        try:
            newline = IO.AddProductandPrice()
            lstOfProductObjects.append(newline)
        except ValueError as e:
            print(e)
        continue

    # Let user save current data to file and exit program
    elif (strChoice.strip() == "3"): #save
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        input("Product & Price saved. Press [Enter] to Exit")
        break
    else:
        print("Try Again")
        continue
# Main Body of Script  ---------------------------------------------------- #