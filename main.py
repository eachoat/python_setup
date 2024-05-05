def hello():
    """Prints a greeting to the user."""
    print("Hello!")

def pack(item1, item2, item3):
    """Accepts three arguments and returns them packed in a list."""
    return [item1, item2, item3]

def eat_lunch(food_list):
    """Prints out the items in a food list."""
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for item in food_list[1:]:
            print("Next I eat", item)