import os


def ft_tqdm(lst: range):
    total = len(lst)
    width = os.get_terminal_size().columns

    """space for text --> 333/333"""
    bar_size = width - 30

    for i, item in enumerate(lst):
        progress = (i + 1) / total
        percent = int(progress * 100)
        filled = int(bar_size * progress)

        bar = "=" * filled
        if filled < bar_size:
            bar += ">"
            bar += " " * (bar_size - filled - 1)

        print(f"\r{percent}%|[{bar}]| {i+1}/{total}", end="")
        yield item

    print()
