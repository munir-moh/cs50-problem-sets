"""Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, 
wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()

Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py"""

import re

def main():
    print(convert(input("Hours: ")))

def convert(text):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, text)

    if not match:
        raise ValueError("Invalid format")

    start_h, start_m, start_p, end_h, end_m, end_p = match.groups()

    start_h = int(start_h)
    end_h = int(end_h)
    start_m = int(start_m) if start_m else 0
    end_m = int(end_m) if end_m else 0

    if start_h not in range(1, 13) or end_h not in range(1, 13):
        raise ValueError("Invalid hour")
    if start_m not in range(60) or end_m not in range(60):
        raise ValueError("Invalid minute")
    
    start_24 = convert_hour(start_h, start_p)
    end_24 = convert_hour(end_h, end_p)

    return f"{start_24}:{start_m:02d} to {end_24}:{end_m:02d}"

def convert_hour(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else: 
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()


