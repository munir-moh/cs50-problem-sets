"""implement a program in Python that prompts the user for input and then outputs that same input, 
replacing each space with ... (i.e., three periods)."""
def main():
    text = input("Enter a text: ")
    new_text = text.replace(" ", "...")

    print(new_text)

main()