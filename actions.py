# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Ocean"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    for store in stores:
        print("- %s" % store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:

        if store_name == store.name:
            return store

    return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print("--------------------------------")
    print_stores()

    my_store = input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.\n')
    while my_store.lower() != "checkout":
        if get_store(my_store):
            return get_store(my_store)
        else:
            print("Invalid! Please try again ... ")


    return "checkout"

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
    user_product = input('Type "back" to go back to the main menu where you can checkout.\n')
        
    
    while user_product.lower() != "back":

        for product in picked_store.products:
            if user_product == product.name:
                cart.add_to_cart(product)
        
        user_product = input()


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()

    #your code goes here!
    store = pick_store()
    while store != "checkout":
        print("--------------------------------")
        pick_products(cart, store)
        store = pick_store()

    print("Here's your receipt:")
    cart.checkout()
    

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
