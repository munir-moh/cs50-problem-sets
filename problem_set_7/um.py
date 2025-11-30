import re

def main():
    text = input("Text: ")
    print(count(text))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
