shopping_list = dict()

def main():
    while(True):
        whatToDo = input("help/instruction: ")
        if whatToDo=="help":
            print_help()
        elif whatToDo=="ca":
            add_category()
        elif whatToDo=="item":
            add_item()
        elif whatToDo=="print":
            print_shopping_list()
        elif whatToDo=="exit":
            break

def print_help():
    print("To add a category-> ca")
    print("To add number of items to a category->item")
    print("To print the shopping list-> print")
    print("To exit-> exit")

def add_category():
    category = input("please type the name of the category: ")
    shopping_list[category] = 0
    print(shopping_list)

def print_shopping_list():
    print(shopping_list)

def add_item():
    category = input("enter category: ")
    number_items = input("number of items: ")
    shopping_list[category] = number_items



main()