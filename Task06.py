def maximum(*args):
    highest_num = args[0]
    for i in args:
        if i > highest_num:
            highest_num = i

    return highest_num

print(maximum(2, 8, 25, 451))
