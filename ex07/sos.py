import sys

# Dictionary
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",

    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. "
}

def main():
    try:
        assert len(sys.argv) == 2

        text = sys.argv[1]
        for char in text:
            assert char.upper() in NESTED_MORSE

        result = ""
        for char in text:
            result += NESTED_MORSE[char.upper()]

        print(result.strip())

    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()