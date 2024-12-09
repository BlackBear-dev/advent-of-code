def main():
    registros = get_registro()
    safe_registered = 0
    safe_registered_extra = 0

    for registro in registros:
        if rules(registro):
            safe_registered += 1
        if rules(registro, extra_rule=True):
            safe_registered_extra += 1

    print(f"Safe registered: {safe_registered}")
    print(f"Safe registered extra: {safe_registered_extra}")


def get_registro() -> list[list[int]]:
    with open("input.txt", "r") as fichero:

        registros = []
        registro = fichero.readline()
        while registro != "":
            levels = list(map(int, registro.split(" ")))
            registros.append(levels)
            registro = fichero.readline()
        return registros


def rules(registro: list[int], extra_rule=False) -> bool:
    incremento = None
    previos = None
    for index, level in enumerate(registro):

        if previos is None:
            previos = level
            continue

        if incremento is None:
            incremento = True if previos < level else False

        if (
            (incremento and level < previos)
            or (not incremento and level > previos)
            or (level == previos)
        ):
            if extra_rule:
                registro2 = registro.copy()
                del registro2[index]
                if rules(registro2):
                    return True
                del registro[index - 1]
                if rules(registro):
                    return True
            else:
                return False

        if 1 < abs(previos - level) > 3:
            return False
        previos = level

    return True


if __name__ == "__main__":
    main()
