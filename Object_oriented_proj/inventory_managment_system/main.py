class Inventory:
    total_items = 0
    total_stock = {}
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity
        Inventory.total_stock[product_name] = {'quantity':quantity, 
                                        'price' : price
                                        }
    
    # Instance Method : Show Product Details 
    def show_product_details(self):
        print('\n--- Product Details ---')
        print(f'Product Name : {self.product_name}')
        print(f'Price : {self.price}')
        print(f'Quantity : {self.quantity}')
    
    # Instance Method : Sell Product
    def sell_product(self, amount):
        if amount <=self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount 
            Inventory.total_stock[self.product_name]['quantity'] -= amount
            print(f'{amount} {self.product_name} sold successfully')
        else:
            print('Insufficient quantity')
    
    # Stati Method : Calculate Discount
    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price * (1 - discount_percentage/100) 


    @classmethod
    def total_items_report(cls):
        print('\n--- Total Items Report ---')
        for idx, (name, data) in enumerate(cls.total_stock.items(), start=1):
            print(f'{idx}.Product name : {name} \nQuantity : {data["quantity"]} \nPrice : {data["price"]}rs')

# gloabal list
all_products_list = []      

def get_num(prompt, num_type=int):
    """Prevents the program from crashing if a user types letters instead of numbers."""
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a number for this field.")

# Add product to Inventory
def add_product():
    product_name = input('Enter product name : ').strip()

    # We look through the list to see if the name already exists.
    for p in all_products_list:
        if p.product_name.lower() == product_name.lower():
            print(f"Error: '{product_name}' is already in the system.")
            return # Stops the function so we don't create a duplicate object

    # Use the helper function here to prevent crashes
    price = get_num('Enter product price : ', float)
    quantity = get_num('Enter product quantity : ', int)

    product = Inventory(product_name, price, quantity)
    all_products_list.append(product)
    product.show_product_details() 
    print(f'\n"{product_name}" added successfully')

# display all products
def view_products():
    Inventory.total_items_report()

# sell product
def sell_product_logic():
    product_name = input('Enter product name to sell : ')
    
    found = False
    for product_obj in all_products_list:
        if product_obj.product_name.lower() == product_name.lower():
            # Apply the helper function here too
            amount = get_num('Enter quantity to sell : ', int)
            product_obj.sell_product(amount)
            found = True
            break
            
    if not found:
        print('Product not found.')

# .calculate discount
def discount_price():
    price = get_num('Enter product price : ', float)
    discount_percentage = get_num('Enter discount percentage : ', float)
    
    result = Inventory.calculate_discount(price, discount_percentage)
    print(f'Discounted price : {result:.2f}') 

# main program
while True:
    print('\n--- Inventory Management System ---')
    print('1. Add Product')
    print('2. View Products')
    print('3. Sell Product')
    print('4. Calculate Discount')
    print('5. Total Items Report')
    print('6. Exit')

    choice = input('Enter your choice (1-6) : ')

    if choice == '1':
        product = add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        sell_product_logic()
    elif choice == '4':
        discount_price()
    elif choice == '5':
        Inventory.total_items_report()
    elif choice == '6':
        print('Exiting the program')
        break
    else:
        print('Invalid choice. Please try again')