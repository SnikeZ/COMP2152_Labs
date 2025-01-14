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