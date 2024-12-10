import re


def main():
    corrupted_memory = get_registro()
    print(corrupted_memory)
    print()
    print("################################################################")
    print()
    corrupted_memory = re.sub(
        r"don't\(\).*?(?=do\(\)|$)", "", corrupted_memory, flags=re.DOTALL
    )
    print(corrupted_memory)
    non_corrupted_memory = re.findall(r"mul\((\d+),(\d+)\)", corrupted_memory)
    print(sum((int(x) * int(y)) for x, y in non_corrupted_memory))


def get_registro() -> str:
    with open("input.txt", "r") as fichero:
        return fichero.read()


if __name__ == "__main__":
    main()
