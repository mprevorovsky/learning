for i in range(17, 54):
    char = ""
    if i % 2 == 0:
        char += "foo"
    if i % 5 == 0:
        char += "bar"

    if char == "":
        print(i)
    else:
        print(char)
