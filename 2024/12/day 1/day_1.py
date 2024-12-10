with open("datos.txt") as datos:
    lineas = datos.readlines()
    left_list, right_list = [], []
    for linea in lineas:
        left, right = linea.split("   ")
        left_list.append(int(left))
        right_list.append(int(right.strip("\n")))
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    # parte 1
    suma = 0
    for left, right in zip(left_list, right_list):
        suma += abs(left - right)
    print("Resultado parte 1:", suma)

    # parte 2

    suma = 0
    left_unique = set(left_list)
    left_dict = {}
    for right in right_list:
        if right not in left_unique:
            continue

        if right in left_dict:
            left_dict[right] += 1
        else:
            left_dict[right] = 1

    suma = 0
    for left in left_dict:
        suma += left_dict[left] * left
    print("Resultado parte 2:", suma)
