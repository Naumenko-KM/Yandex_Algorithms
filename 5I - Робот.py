# don't understand the task
# too much to do

K = int(input())
operations = input()


def is_economically_viable(K, operaion, *args):
    pass


def find_robot_nums(K, operations):
    prev_len = 0
    num = 0
    for i in range(K, len(operations)):
        if operations[i] == operations[i - K]:
            prev_len += 1
            num += prev_len
        else:
            prev_len = 0
    return num


print(find_robot_nums(K, operations))
