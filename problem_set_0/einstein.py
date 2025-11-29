"""implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer."""

def main():
    mass = int(input("Input mass in (kg): "))

    c = 3e8
    E = mass * c**2

    print(int(E))

main()