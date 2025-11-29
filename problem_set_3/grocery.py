"""Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, 
sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively."""

def main():
    groceries = {}

    while True:
        try:
            item = input().lower()
            groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            break

    for item in sorted(groceries):
        print(groceries[item], item.upper())

main()
