shopping_list = list()

def main():
    while(True):
        whatToDo = input("help/instruction: ")
        if whatToDo=="help":
            print_help()
        elif whatToDo=="ca":
            add_category()
        elif whatToDo=="exit":
            break

def print_help():
    print("To add a category-> ca")
    print("To add number of items to a category-><category> <numberOfItems>  ex:fruit 4")
    print("To print the shopping list-> print")
    print("To exit-> exit")

def add_category():
    category = input("please type the name of the category: ")
    shopping_list.append({category:0})
    print(shopping_list)

main()