n = int(input())
first_freq = float(input())
notes = []
for i in range(1, n):
    freq, closer = input().split()
    closer = True if closer == 'closer' else False
    notes.append([float(freq), closer])

freq_min = 30
freq_max = 4000

for i in range(len(notes)):
    if i == 0:
        freq = first_freq

    freq_new = notes[i][0]
    closer = notes[i][1]
    dist = freq - freq_new
    if (closer and freq_new < freq) or (not closer and freq_new > freq):
        if freq_new + dist/2 < freq_max:
            freq_max = freq_new + dist/2
    else:
        if freq_new + dist/2 > freq_min:
            freq_min = freq_new + dist/2
    freq = freq_new

print(freq_min, freq_max)

        






