shopping_list = list()

def main():
    whatToDo = input("type help in any stage to get help/type the instruction:")
    if whatToDo=="help":
        printHelp()

def printHelp():
    print("To add a category-> ca")
    print("To add number of items to a category-><category> <numberOfItems>  ex:fruit 4")
    print("To print the shopping list-> print")

main()