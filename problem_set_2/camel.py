"""implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case."""

def main():
    camel = input("camelCase: ")
    print("snake_case:", in_snake_case(camel))


def in_snake_case(name):
    snake = ""
    for letter in name:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    return snake

main()
