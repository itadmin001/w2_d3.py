
list = {}
categories = ['drink','meat','snacks','dairy','seafood','produce','poultry']

def take_input():
    item_count = 0
    j=1
    item=''
    print(item)
    while True:
        item = input("Enter List Item or 'quit' to exit: ")
        if item != '' and item.lower() != 'quit':
            item_count+=1
            quantity = input("Enter item quantity: ")
            price = input("Enter item price: ")
            print("Item Categories: ")
            j=1
            for i in categories:
                print(f"{int(j)}. {i}")
                j+=1
            choice = input("Choose item cagtory: ")
            match choice: 
                case '1': category = 'drink'
                case '2': category = 'meat'
                case '3': category = 'snacks'
                case '4': category = 'dairy'
                case '5': category = 'seafood'
                case '6': category = 'produce'
                case '7': category = 'poultry'

            list.update({"item"+str(item_count):{
                'item':item,
                'quantity':quantity,
                'price':price,
                'category':category
            }})
        
        else:
            if item.lower() != 'quit':
                input("Invalid entry, please try again, ENTER to continue")
            events()

def events():
    choices = ['Add another item', 'Delete an item', 'Display the list','Quit']
    
    while True:
        for index, choice in enumerate(choices):
            print(f"{index+1}. {choice}")
        this_choice = input("What would like to do? ")
        match this_choice:
            case '1': take_input()
            case '2': delete_items()
            case '3': show_list()
            case '4': quit()
            case _: print("Invalid choice, please try again"); continue

def show_list():
    for k,v in list.items():
        print("\n")
        for key,value in v.items():
            print(f"{key}: {value}")
    take_input()

def delete_items():
    for k,v in list.items():
        print(f"Item ID: {k} Item name: {v['item']}")
    to_remove = input("\nType the item ID of the item you would like to remove: ")
    removed = list.pop(to_remove)
    print(f"\nremoved {removed['item']} from the list")

    show_list()

def quit():
    exit()

take_input()






# Remove dupes from list
nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]
print(set(nums_list))

#Output intersection of the sets
set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}
print((set1 & set2).intersection())


#Output diff between sets
set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}

print((set3 & set4).difference())