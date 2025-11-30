import sys
import os
from PIL import Image, ImageOps

def main():

    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file, output_file = sys.argv[1], sys.argv[2]

    allowed = (".jpg", ".jpeg", ".png")

    in_ext = os.path.splitext(input_file)[1].lower()
    out_ext = os.path.splitext(output_file)[1].lower()

    if in_ext not in allowed:
        sys.exit("Invalid input")
    if out_ext not in allowed:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt, shirt)

    photo.save(output_file)

if __name__ == "__main__":
    main()
