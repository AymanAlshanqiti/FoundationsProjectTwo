# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Ocean"  # Give your site a name

def welcome():
    print("\nWelcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)


def print_stores():

    print("\nOur stores: ")
    for store in stores:
        print("- %s" % store.name)


def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:

        if store_name.lower() == store.name.lower():
            return store

    return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()

    my_store = input('\nPick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.\n')

    while my_store.lower() != "checkout":
        if get_store(my_store.lower()):
            return get_store(my_store)
        else:
            my_store = input("Invalid store! Please try again .. \n")

    return "checkout"


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
    user_product = input('Type "back" to go back to the main menu where you can checkout.\n')
          
    while user_product.lower() != "back":

        for product in picked_store.products:
            if user_product.lower() == product.name.lower():
                cart.add_to_cart(product)
        
        else:
            user_product = input()


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()

    store = pick_store()
    while store != "checkout":
        print("\n   --------------------------------")
        pick_products(cart, store)
        store = pick_store()

    print("\n   # -------------------------------- #\n")
    print("Here's your receipt:\n")
    cart.checkout()
    

def thank_you():
    print("Thank you for shopping with us at %s\n" % site_name)
