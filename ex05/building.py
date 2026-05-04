import sys


def analyze_text(text):
    """Counting character types in argv[1]"""

    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif not char.isalnum() and not char.isspace():
            punctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Checking if its a valid prompt"""
    argc = len(sys.argv)

    if argc == 1:
        try:
            text = input("What is the text to count?\n")
        except EOFError:
            text = ""
        else:
            text += "\n"  # only runs if NO exception occurred
    elif argc == 2:
        text = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return

    analyze_text(text)


if __name__ == "__main__":
    main()
