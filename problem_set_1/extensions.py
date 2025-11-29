"""implement a program that prompts the user for the name of a file and 
then outputs that file’s media type if the file’s name ends, case-insensitively, 
in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file’s name ends with some other suffix or has no suffix at all, 
output application/octet-stream instead, which is a common default."""


def main():
    file_name = input("Enter a file name: ").strip().lower()

    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        return "image/jpeg"
    elif file_name.endswith(".zip"):
        return "application/zip"
    elif file_name.endswith(".png"):
        return "image/png"
    else:
        return "application/octet-stream"
    
print(main())

