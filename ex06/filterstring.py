import sys
from ft_filter import ft_filter

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = S.split()
        check_len = lambda word: len(word) > N  #lambda is a temp function
        result = [word for word in ft_filter(check_len, words)]
        
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()