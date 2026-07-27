import sys
from ft_filter import ft_filter


def main():
    """Verify arguments. And call ft_filter()"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = S.split()

        def check_len(word):
            """Check if length is bigger than N"""
            return len(word) > N
        result = [word for word in ft_filter(check_len, words)]

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
