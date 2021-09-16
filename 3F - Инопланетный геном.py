gen_a = input()
gen_b = input()

pairs_b = set([gen_b[i:i+2] for i in range(len(gen_b)-1)])
cnt = 0
for i in range(len(gen_a)-1):
    if gen_a[i:i+2] in pairs_b:
        cnt += 1
print(cnt)