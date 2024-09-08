def inverte_caractere(value):
    value_list = list(value)
    reverse_list = []
    for i in range(len(value_list)-1, -1, -1):
        reverse_list.append(value_list[i])
    return "".join(reverse_list)


if __name__ == "__main__":
    result = inverte_caractere(input("Digite a string: "))
    print(result)