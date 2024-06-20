import time #Import time module was used because time and date will be shown in the checkout function

class User:     #Created a class definiton for a user with attributes username,password,wrong attempts,blocked and basket.
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.wrong_attempts = 0
        self.blocked = False
        self.basket = []


#Created a dictionary based on usernames and passwords
users = {'ahmet': User('ahmet', '1234'), 'zeynep': User('zeynep', '4444'),'mert':User('mert','2003'),'admin': User('admin', 'qwerty')}
inventory = [{'name':'Asparagus','stock':10,'price':5},
             {'name':'Broccoli','stock':15,'price':6},
             {'name':'Carrots','stock':18,'price':7},
             {'name':'Apples','stock':20,'price':5},
             {'name':'Banana','stock':10,'price':8},
             {'name':'Berries','stock':30,'price':3},          # Inventory of products available in the market.
             {'name':'eggs','stock': 50,'price': 2},
             {'name': 'Mixed fruit juice','stock':0,'price':8},
             {'name':'Fish sticks','stock':25,'price':12},
             {'name':'Ice Cream','stock':32,'price':6},
             {'name':'AppleJuice','stock':40,'price':7},
             {'name':'Orange Juice','stock':30,'price':8},
             {'name':'Grape Juice','stock':10,'price':9}]
print("**** Welcome to Medipol Online Market ****")
print('Please log in by providing your user credentials ')


def show_menu():   # This function to show the main menu options to the user.
    print("Please choose one of the following options: ")
    print("1. Search for a product\n2. See Basket\n3. Check Out\n4. Logout\n5. Exit")

def search_product(): #This function to search product in the inventory
    searching_item = input('What are you searching for? ').lower()
    matching_items = []
    for item in inventory:
        if searching_item in item['name'].lower() and item['stock'] > 0:
            matching_items.append(item)    #Adds products matching the search result
    while not matching_items:
        searching_item = input("No matching item found. Try another word: (Enter 0 for main menu) ").lower()
        if searching_item == '0':
            break
        matching_items = []
        for item in inventory:
            if searching_item in item['name'].lower() and item['stock'] > 0 :
                matching_items.append(item)
    if matching_items:
        print(f"Found {len(matching_items)} similar items:")
        for i in range(len(matching_items)):
            element = i + 1
            item = matching_items[i]
            print(f"{element}. {item['name']} ${item['price']}") #Created select options for user
            print()
        while True:
            choice = input("Select item to add (Enter 0 for main menu): ")
            if choice == '0':
                break
            elif choice.isdigit() and 0 < int(choice) <= len(matching_items):
                selected_item = matching_items[int(choice) - 1]
                amount = int(input(f"How many {selected_item['name']} would you like to add? "))
                #Check amount is available or not
                if 0< amount <= selected_item['stock']:
                    users[username].basket.append(
                        {'name': selected_item['name'], 'price': selected_item['price'], 'amount': amount})
                    print(f"{amount} {selected_item['name']} added to your basket.")
                    print('Going back to main menu...')
                    print()
                    selected_item['stock'] -= amount
                    break
                elif amount < 0:
                    print('Sorry amount cannot be negative!!!')
                else:
                    print(f"Sorry! The amount exceeds the stock limit. Available stock: {selected_item['stock']}")
            else:
                print("Invalid selection. Please enter a new number.")

def show_basket():  # Function to display the user's basket.
    print("Your basket contains:")
    total_price = 0
    basket = users[username].basket
    for i in range(len(basket)):
        item = basket[i]
        element = i + 1
        item_total = item['amount'] * item['price']
        total_price += item_total
        print(f"{element}.{item['name']} price={item['price']}$ amount={item['amount']} total={item_total:}$")
    print(f"Total: {total_price:}$")
    # This code for showing the basket content and total price.


def basket_sub_menu():  # Function for sub-menu operations on the basket
    while True:
        print(f"1.Update Amount\n2.Remove on item\n3.Checkout\n4.Go back to the main menu")
        choice = input("Your selection: ")
        if choice == '1':
            show_basket()

            while True:
                selected_item = int(input('Select item to change its amount:  '))
                # Check if the selected item is within the range
                if 1 <= selected_item <= len(users[username].basket):
                    item_name = users[username].basket[selected_item - 1]['name']
                    search_key = item_name
                    item_index = -1
                    element = 0
                    # Searching for the item in the inventory to find its index.
                    for my_dict in inventory:
                        if search_key in my_dict['name']:
                            print('//////')
                            item_index = element
                            break
                        element += 1
                    # Check if a valid item was found in the inventory.
                    if 0 <= item_index < 13:
                        items_basket_index = -1
                        new_amount = int(input("Enter the new amount: (Enter 0 for sub menu) "))
                        search_key2 = inventory[item_index]['name']
                        # Finding the index of the item in the user's basket.
                        for index in range(len(users[username].basket)):
                            if users[username].basket[index]['name'] == search_key2:
                                print('Processing***')
                                itemsBasketIndex = index
                                break
                        else:
                            print()

                        amount_of_ıtem_in_basket = users[username].basket[items_basket_index]['amount']
                        inventory[item_index]['stock'] += amount_of_ıtem_in_basket

                        while new_amount > inventory[item_index]['stock']:
                            print(
                                f"Sorry! The new amount exceeds the stock limit. Available stock: {inventory[item_index]['stock']}")
                            new_amount = int(input("Enter the new amount (Enter 0 for the main menu): "))
                        # Updating the basket if the new amount is greater than zero.
                        if new_amount > 0:
                            users[username].basket[items_basket_index]['amount'] = new_amount
                            inventory[item_index]['stock'] -= new_amount
                            print('Your basket is changed')
                            show_basket()
                            break
                        # Resetting the stock if an invalid amount is entered
                        if new_amount < 0:
                            print("you made a mistake")
                            inventory[item_index]['stock'] -= amount_of_ıtem_in_basket
                            break
                        if new_amount == 0 :
                            print('Going back to menu...')
                            break
                    else:
                        print(print("Invalid item selection."))
                else:
                    print("Invalid item selection. Please try again.")

        elif choice == '2':
            while True:
                show_basket()
                item_index = int(input("Select item to remove:(Enter 0 for submenu) ")) - 1


                if item_index == -1:
                    print('Going back to sub menu..')
                    break


                if 0 <= item_index < len(users[username].basket):
                    removed_item = users[username].basket[item_index]
                    amount_of_item_in_basket = removed_item['amount']
                    item_found_in_inventory = False

                    for inventory_item in inventory:
                        # Check if the item's name matches the removed item's name.
                        if inventory_item['name'] == removed_item['name']:
                            # If found, add the quantity back to the inventory stock.
                            inventory_item['stock'] += amount_of_item_in_basket
                            item_found_in_inventory = True
                            break

                    # If the item was found in the inventory, remove it.
                    if item_found_in_inventory:
                        users[username].basket.pop(item_index)
                        print(f"{removed_item['name']} removed from your basket.")
                        print('Your basket now:')
                        show_basket()
                        break
                    else:
                        print("Error: Item not found in inventory.")
                else:
                    print("Invalid item selection.")

        elif choice == '3':
            checkout()

            break
        elif choice == '4':
            return

        else:
            print("Invalid selection. Please choose a valid option.")

def checkout():
    print("Processing your receipt...")
    print("******* Medipol Online Market ********")
    print("**************************************")
    print("444 8 544")
    print("medipol.edu.tr")
    print("————————————")
    total_price = 0
    for item in users[username].basket:
        item_total = item['amount'] * item['price']
        total_price += item_total
        print(f"{item['name']} ${item['price']} amount={item['amount']} total=${item_total}")

    print("————————————")
    print(f"Total: $ {total_price:}")
    print("————————————")
    print(time.strftime("%Y/%m/%d %H:%M")) # Strftime function used for display time and date
    print("Thank You for using our Market!")
    users[username].basket = []  #After checkout reset user's basket


def admin_menu(): # Function to display admin menu options.
    while True:
        print("Please choose one of the following options:")
        print("1. Activate User Account\n2. Deactivate User Account\n3. Add User\n4. Remove User\n5. Logout\n6. Exit")
        admin_choice = input("Your Choice: ")
        if admin_choice == '1':
            activate_user_account()
        elif admin_choice == '2':
            deactivate_user_account()
        elif admin_choice == '3':
            add_user()
        elif admin_choice == '4':
            remove_user()
        elif admin_choice == '5':
            print("Logging out. Goodbye, Admin!")
            break
        elif admin_choice == '6':
            print("Exiting the program. Goodbye, Admin!")
            exit()
        else:
            print("Invalid admin menu entry. Please provide a valid menu number.")

def activate_user_account():
    while True:
        user_to_activate = input("Enter the username to activate: (enter 0 for admin menu) ")
        if user_to_activate == '0':
            break
        # Check if the entered username exists in the users dictionary and blocked
        if user_to_activate in users and users[user_to_activate].blocked:
            users[user_to_activate].blocked = False  #Admin activate user and reset attempt count
            users[user_to_activate].wrongAttempts = 0
            print(f"{user_to_activate}'s account has been activated.")
            break
        elif user_to_activate in users and not users[user_to_activate].blocked:
            print(f"{user_to_activate}'s account is not blocked.")
        else:
            print(f"No user found with the username {user_to_activate}.")

def deactivate_user_account():
    while True:
        user_to_deactivate = input("Enter the username to deactivate:(enter 0 for admin menu) ")
        if user_to_deactivate == '0':
            break
        # Check if the entered username exists in the users dictionary and if the account is not already blocked.
        if user_to_deactivate in users and not users[user_to_deactivate].blocked:
            users[user_to_deactivate].blocked = True  #Admin blocked account.
            print(f"{user_to_deactivate}'s account has been deactivated.")
            break
        elif user_to_deactivate in users and users[user_to_deactivate].blocked:
            print(f"The username {user_to_deactivate} already blocked.")
        else:
            print('invalid username try again!!! ')

def add_user():
    while True:
        new_username  = input("Enter the new username: (enter 0 for admin menu) ")
        if new_username == '0':
            break
        new_password = input("Enter the new password: ")
        # Check if the entered username does not already exist in the users
        if new_username not in users:
            # Create a new User object and add it to the users dictionary.
            users[new_username] = User(new_username, new_password)
            print(f"{new_username} has been added as a new user.")
            break
        else:
            print(f"The username {new_username} already exists.")

def remove_user():
    while True:
        user_to_remove = input("Enter the username to remove: (enter 0 for admin menu) ")
        if user_to_remove == '0':
            break
        # Check if the entered username exists in the users dictionary and is not the admin account.
        if user_to_remove in users and user_to_remove != 'admin':
            del users[user_to_remove]  #Admin remove user
            print(f"{user_to_remove} has been removed.")
            break
        elif user_to_remove == 'admin':
            print("Cannot remove the admin user.")
        else:
            print(f"No user found with the username {user_to_remove}.")

while True:   #Main loop starts.
    username = input('Username: ')
    while username not in users:
        username = input("No username matched. Try another one: ")
    if users[username].blocked:   # Check if the user account is blocked.
        print("User blocked!")
    else:
        password = input('Password: ')
    if username == 'admin' and password == 'qwerty':
        admin_menu()
    # Check for regular user login credentials.
    elif username in users and users[username].password == password and not users[username].blocked:
        print('Successfully logged in')
        print(f"Welcome {username}")
        users[username].wrong_attempts = 0
        while True:
            show_menu()
            choice = input("Your Choice: ")
            if choice == '1':
                search_product()
            elif choice == '2':
                show_basket()
                print()
                basket_sub_menu()
            elif choice == '3':
                checkout()
            elif choice == '4':
                print("Logging out. Goodbye!")
                break
            elif choice == '5':
                print("Exiting the program. Goodbye!")
                exit()
            else:
                print("Invalid menu entry. Please provide a valid menu number.")

    elif username in users and users[username].blocked:
        print("Account is blocked. Contact administrator.")

    elif username in users and not users[username].password == password:
        users[username].wrong_attempts += 1
        print("Your password is incorrect")
        # Block the account after 3 wrong attempts.
        if users[username].wrong_attempts >= 3:
            users[username].blocked = True
            print("Account Blocked!")
    else:
        print("Invalid credentials.")

