from random import randint

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("Elements: ", *elements)

# def funct_name():
#     return True
# def say_greeting(name, message="hi"):
#     print(f" {message}, {name}")
# say_greeting("Maziar")
# say_greeting("Maziar", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer value.")
            continue

try:
    element_selected = get_valid_int_input("Enter the number of elements you want to select: ")

    # Roll dice
    element_roll = randint(0, len(elements)-1)
    total_num = element_selected + element_roll

    if element_roll <= 2:
        print("You rolled a weak element")
    elif element_roll <= 4:
        print("You rolled a moderate element")
    else:
        print("Nice element.")
except IndexError:
    print("Error: Invalid element index!")        
except Exception as e:
    print(f"An unexpected error occurred: {e}") 