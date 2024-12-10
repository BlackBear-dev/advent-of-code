def main():
    registros = get_registro()
    safe_registered = 0
    safe_registered_extra = 0

    for registro in registros:
        if rules_registros(registro):
            safe_registered += 1
        else:
            if rules_registros(registro, extra_rule=True):
                safe_registered_extra += 1

    print(f"Safe registered: {safe_registered}")
    print(f"Safe registered extra: {safe_registered_extra+safe_registered}")


def get_registro() -> list[list[int]]:
    with open("input.txt", "r") as fichero:

        registros = []
        registro = fichero.readline()
        while registro != "":
            levels = list(map(int, registro.split(" ")))
            registros.append(levels)
            registro = fichero.readline()
        return registros


def rules_registros(registro: list[int], extra_rule=False) -> bool:
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
            or (1 < abs(previos - level) > 3)
        ):
            if extra_rule:
                bandera = True
                index_control = 0
                while bandera:
                    registro_copy = registro.copy()
                    del registro_copy[index - index_control]
                    if rules_registros(registro_copy):
                        return True

                    if index_control == len(registro):
                        bandera = False
                    index_control += 1
            return False
        previos = level
    return True


if __name__ == "__main__":
    main()
