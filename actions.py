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
    print('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
    print('Type "back" to go back to the main menu where you can checkout.')
        
    

    user_product = input()
    while user_product != "back":
        flag = False
        for product in picked_store.products:
            if user_product == product.name:
                cart.add_to_cart(product)
                flag = True

        if(flag == False):
            print('No product with that name. Please try again.')
        
        user_product = input()

    else:
        return shop()


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()

    #your code goes here!
    pick_store()

    picked_store = input()

    while picked_store != "checkout":
        while get_store(picked_store) == False:
            picked_store = input('No store with that name. Please try again.\n')
            get_store(picked_store)

        else:
            store = get_store(picked_store)

            print("--------------------------------")
            pick_products(cart, store)

        return cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
