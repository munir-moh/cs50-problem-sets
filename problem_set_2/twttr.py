"""implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase."""

def main():
    text = input("Input a text: ")
    print("Output:", shorten(text))

def shorten(s):
    result = ""
    for char in s:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            result += char
    return result

main()
