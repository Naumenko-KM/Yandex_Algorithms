n = int(input())
resource = list(map(int, input().split()))
k = int(input())
press_num = list(map(int, input().split()))
resourse_dict = {key + 1: [res, 0] for key, res in enumerate(resource)}
for key in press_num:
    resourse_dict[key][1] += 1
for key in resourse_dict:
    if resourse_dict[key][1] > resourse_dict[key][0]:
        print('YES')
    else:
        print('NO')
